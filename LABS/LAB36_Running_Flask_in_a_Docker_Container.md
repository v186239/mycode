Running Flask in a Docker Container
Lab Objective
The objective of this lab is to give students an idea of how to run Flask application within a Docker container. Think of containers as light-weight virtualization (as opposed to a virtual machine).

Docker is easy to get started with. Most Linux operating systems install with, or give the option to install, Docker. Applications to run on your Docker platform can be found at: https://hub.docker.com

Procedure
Ensure you are in the home directory.

student@bchd:~$ cd

Confirm docker is installed by listing the various commands.

student@bchd:~$ docker --help

Imagine you’re trying to deploy the following Python code, contained in ~/dune.py The application is a simple "Hello Arrakis" app that uses Flask.

Create a directory to work in:

student@bchd:~$ mkdir mycode/dune && cd mycode/dune

Create the following file, dune.py

student@bchd:~/mycode/dune$ vim dune.py


#!/usr/bin/python3
"""By Chad Feeser | Alta3 Research
To use, try:
    curl localhost:5000/
    curl localhost:5000/atreides/
"""

from flask import Flask
app = Flask(__name__)

# if user sends HTTP GET to /
@app.route("/")
def index():
    return "In Frank Herbert's Dune, the Spice Melange makes space travel possible."

# if user sends HTTP GET to /atreides
@app.route("/atreides")
def atreides():
    return "As Dune opens, House Atreides is transitioning their rule to Arrakis, a desert planet."
    
# bind to all IP addresses port 5000
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
Exit with :wq

You'll need Flask to run this script, if you haven't installed it yet. Use pip to install flask.

student@bchd:~/mycode/dune$ python3 -m pip install flask

Great! Let's test our application.

student@bchd:~/mycode/dune$ python3 dune.py

Split your screen with Ctrl + b and then Shift + "

In the new tmux pane, curl your endpoints. The following command sends an HTTP GET to localhost:5000.

student@bchd:~$ curl http://localhost:5000/


In Frank Herbert's Dune, the Spice Melange makes space travel possible.
Great! Now send an HTTP GET to the second one.

student@bchd:~$ curl http://localhost:5000/atreides


As Dune opens, The House Atreides is transitioning their rule to Arrakis, a desert planet.
Looks like our Python Flask application is running just fine. Exit the current tmux pane.

student@bchd:~$ exit

Stop your Python Flask application by pressing Ctrl + c... if you leave it running it might attract sandworms!

To transform our application into a containerized app, we need to create a Dockerfile. The name Dockerfile is actually standardized, so don't try to rename it to something else. This file will tell Docker 'what to do' in order to create our container image.

student@bchd:~/mycode/dune$ vim Dockerfile


# This base image container is avail on hub.docker.com
# it has python 3.7 avail on Alpine Linux, a minimalist Linux distro
FROM python:alpine3.7
COPY . /app
WORKDIR /app
# Use Python package installer to install the Flask library to our image
RUN pip install -r requirements.txt
# container is exposed on port 5000
EXPOSE 5000
CMD python ./dune.py
Note that FROM directive is pointing to python:alpine3.7. This is telling Docker what base image to use for the container, and implicitly selecting what Python version to use, which in this case is 3.7. Docker Hub has base images for almost all supported versions of Python including 2.7. This example is using Python installed on Alpine Linux, a minimalist Linux distro, which helps keep the images small.

Also note the RUN directive that is calling PyPi (pip) and pointing to the requirements.txt file. This file contains a list of the dependencies that the application needs to run. Create that file now.

student@bchd:~/mycode/dune$ vim requirements.txt


# python dependencies
flask
The remaining directives in the Dockerfile are pretty straightforward. The CMD directive tells the container what to execute to start the application. In this case, it is telling Python to run dune.py. The COPY directive simply moves the application into the container image, WORKDIR sets the working directory, EXPOSE exposes a port that is used by Flask.

To build the image, run docker build from a command line or terminal that is in the root directory of the application. Including -t will "tag" our image as dune-app. Including -f Dockerfile instructs Docker to look to the file named Dockerfile for instructions on how to build the image.

student@bchd:~/mycode/dune$ sudo docker build -t dune-app -f Dockerfile .


...
Successfully built 4ffb50d3874c
Successfully tagged dune-app:latest
Now that our application is built, we can run the image, dune-app, within a Docker container named scifi.

student@bchd:~/mycode/dune$ sudo docker run --name scifi -p 5000:5000 dune-app


 * Serving Flask app "dune" (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: on
 * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 332-352-297    
This starts the application as a container. The --name parameter names the container and the -p parameter maps the host’s port 5000 to the container's port of 5000. Lastly, the dune-app is the image to run (we tagged it with this name). After it starts, you should be able to curl to the container. Try interacting with your endpoints as you did before.

Split your screen with Ctrl + b and then Shift + "

Now try to curl your first endpoint.

student@bchd:~$ curl http://localhost:5000/


In Frank Herbert's Dune, the Spice Melange makes space travel possible.
Great! Now send an HTTP GET to the second one.

student@bchd:~$ curl http://localhost:5000/atreides


As Dune opens, The House Atreides is transitioning their rule to Arrakis, a desert planet.
We can look at the containers Docker is currently running with docker ps. Issuing this command should show the container scifi running the image dune-app on port 5000.

student@bchd:~$ sudo docker ps


CONTAINER ID        IMAGE               COMMAND                  CREATED             STATUS              PORTS                    NAMES
31bb91f27ecf        dune-app            "/bin/sh -c 'python …"   4 minutes ago       Up 4 minutes        0.0.0.0:5000->5000/tcp   scifi
Start ANOTHER instance of your app. The code has been "hardened" to listen on port 5000. We may "only" have a single instance of port 5000 locally, but we can make Docker port forward any local port into the network namespace's port 5000 (where our new Flask application will be running). This time, use port 34727 (locally) and forward to port 5000 (within the container).

student@bchd:~/mycode/dune$ sudo docker run --name sandworm -p 34727:5000 dune-app


sudo docker run --name sandworm -p 34727:5000 dune-app
 * Serving Flask app "dune" (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: on
 * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 115-903-280
Look at that! One docker system running two applications, both using port 5000! Amazing.

Split your screen with Ctrl + b and then Shift + "

Now try to curl your first Dune application (listening on local port 5000 and the container port 5000).

student@bchd:~$ curl http://localhost:5000/


In Frank Herbert's Dune, the Spice Melange makes space travel possible.
Great! Now send an HTTP GET to the second one (Docker knows to send local port 34727 to the container port 5000)

student@bchd:~$ curl http://localhost:34727/


In Frank Herbert's Dune, the Spice Melange makes space travel possible.
Both application should be sending back the same response. Imagine a load balancer in front of a bunch of applications, and you're starting to realize the power of containers and microservice architectures.

Because Docker is running our container, we can't 'just' issue a (CTRL + c) on our Flask app to stop it. Any command we would issue will result in Docker simply re-launching the container (Docker's job is to keep applications running). Therefore, we need to tell Docker to stop the container named scifi.

student@bchd:~$ sudo docker stop scifi

Now also stop sandworm

student@bchd:~$ sudo docker stop sandworm

Now that our image has been built, it has been cached by Docker locally. To run it, we no longer need to docker build the image. We can now simply deploy the built image. Where dune-app is the name of the image we created, docker will randomly spawn a name for our container.

student@bchd:~$ sudo docker run dune-app

You should still have two tmux panes open. Switch back to an unoccupied tmux pane by first pressing CTRL + b and then following with the directional arrow in the direction you wish to move the cursor.

Get some details about the container you just ran.

student@bchd:~$ sudo docker ps


CONTAINER ID        IMAGE               COMMAND                  CREATED              STATUS              PORTS               NAMES
0ee8c74c52eb        dune-app            "/bin/sh -c 'python …"   About a minute ago   Up About a minute   5000/tcp            friendly_hugle
The only changes should be a new CONTAINER ID, as well as a new (randomly created) NAMES. In the previous example, we supplied the name via --name scifi for our container. This time, Docker created one randomly for us. The following command is a shortcut to stop all containers docker is currently running, regardless of how they are named (WARNING: this will also close Bender, Fry, Zoidberg, and Farnsworth. You'll need to rebuild those if you plan to use them again)

student@bchd:~$ sudo docker stop $(sudo docker ps -aq)

Naturally, more complex scenarios will require more attention to details, but the basic flow is the same for containerizing most applications.

Answer the following questions:

Q1: How many times does Docker need to create the image?
A1: Just once. Building images takes time, to create the container image more than once is wasteful
Q2: Could the build process fail? Why or why not?
A2: Of course! In our example, an application dev could fail to produce the correct requirements.txt file, or point to the wrong base images to construct the image from, or any number of things!
Q3: Where does Docker fit into this?
A3: When code gets pushed into a repository, we want to turn it into an image and run it. Ideally, we want to isolate that code (application) and give it ONLY what it needs to do the job it was designed to do.
CHALLENGE 01 (OPTIONAL)- An Alta3 instructor has put together a GitHub repository that will allow students to practice building API microservices with Flask and Docker containers: https://github.com/rzfeeser/simpleflaskservice

Your challenge is to clone this repository and instantiate a working Flask server (simpleflaskservice.py)
You can try this on your own or refer to the README.md inside the repository for help.
Build an image with this Flask app and run a container.
You'll know you have succeeded when you have the Flask server running inside of a Docker container and can curl the endpoints provided by this Flask application.
CHALLENGE 02 (OPTIONAL)- Write a Python client using the requests library to connect to your new microservices.

CHALLENGE 03 (OPTIONAL)- Add at least one more route that will return the Dune quotes in JSON format! This will require you to rebuild the image, give it a new tag.
