# Building APIs with Python
Lab Objective
The objective of this lab is to explore building APIs with Flask. Before we start, review the following terms:

Web Application Framework (Web Framework) - A collection of libraries and modules that enables a web application developer to write applications without having to bother about low-level details such as protocols, thread management, etc.

Flask - Web application framework written in Python. It is developed by Armin Ronacher, who leads an international group of Python enthusiasts named Pocco. Flask is based on the Werkzeug WSGI toolkit and Jinja2 template engine. Both are Pocco projects. Flask is often referred to as a micro framework. It aims to keep the core of an application simple yet extensible. Flask does not have a built-in abstraction layer for database handling, nor does it have a form of validation support. Instead, Flask supports the extensions to add such functionality to the application.

Web Server Gateway Interface (WSGI) - Adopted as a standard for Python web application development, WSGI is a specification for a universal interface between the web server and the web applications.

Werkzeug - WSGI toolkit, implements requests, response objects, and other utility functions. This enables building a web framework on top of it. The Flask framework uses Werkzeug as one of its bases.

Jinja2 - A popular templating engine for Python. A web templating system combines a template with a certain data source to render dynamic web pages.

Procedure
Open a new terminal.

Install the software library "Flask", which we will need for this script. This will allow us to create APIs.

student@bchd:~$ python3 -m pip install flask

Create a new directory to work in, /home/student/mycode/flaskapi/

student@bchd:~$ mkdir ~/mycode/flaskapi/

Move into the new directory.

student@bchd:~$ cd ~/mycode/flaskapi/

Create a new script, myflask01.py

student@bchd:~/mycode/flaskapi$ vim myflask01.py

Copy and paste the following into your script:


#!/usr/bin/python3
# An object of Flask class is our WSGI application
from flask import Flask

# Flask constructor takes the name of current
# module (__name__) as argument
app = Flask(__name__)

# route() function of the Flask class is a
# decorator, tells the application which URL
# should call the associated function
@app.route("/")
def hello_world():
   return "Hello World"

if __name__ == "__main__":
   app.run(host="0.0.0.0", port=2224) # runs the application
   # app.run(host="0.0.0.0", port=2224, debug=True) # DEBUG MODE
Save and exit with :wq

Run the script myflask01.py

student@bchd:~/mycode/flaskapi$ python3 myflask01.py

Along the right hand side of the screen, choose aux1 in your dropdown selector.

The aux1 connection is a view of what is happening at http://0.0.0.0:2224/. Therefore, the Hello World should be returned.

Select your tmux environment again.

Stop your Flask app by clicking on the terminal window it is running in and pressing CTRL + C

Modern web frameworks use the routing technique to help a user remember application URLs. It is useful to access the desired page directly without having to navigate from the home page. The route() decorator in Flask is used to bind URL to a function. For example, consider the following:


@app.route("/hello")
def hello_world():
    return "hello world"
Above, the URL /hello rule is bound to the hello_world() function. As a result, if a user visits the http://0.0.0.0:2224/hello URL, the output of the hello_world() function will be rendered in the browser.

The add_url_rule() function of an application object is also available to bind a URL with a function. As in the above example, route() is used. A decorator’s purpose is also served by the following representation (again, just for your reading pleasure):


def hello_world():
   return "hello world"
app.add_url_rule("/hello", "hello", hello_world)
Create a new script, myflask02.py

student@bchd:~/mycode/flaskapi$ vim myflask02.py

It is possible to build a URL dynamically by adding variable parts to the rule parameter. This variable part is marked as <variable-name>. It is passed as a keyword argument to the function with which the rule is associated. In your next script, the rule parameter of route() decorator contains <name> variable part attached to URL /hello. Hence, if the http://localhost:5000/hello/Zuul is entered as a URL in the browser, Zuul will be supplied to hello() function as argument.

Copy and paste the following into myflask02.py


#!/usr/bin/python3
from flask import Flask
app = Flask(__name__)

@app.route("/hello/<name>")
def hello_name(name):
    return f"Hello {name}"
    ## V2 STYLE STRING FORMATTER - return "Hello {}".format(name)
    ## OLD STYLE STRING FORMATTER - return "Hello %s!" % name

if __name__ == "__main__":
   app.run(host="0.0.0.0", port=2224) # runs the application
Save and exit with :wq

Run your script, myflask02.py

student@bchd:~/mycode/flaskapi$ python3 myflask02.py

With your script running click to "Group Dashboard" within the Alta3 Interface.

In the Student Environments dropdown, find your name, and then click your aux1. This should open a new tab within your current browser.

The current url is showing what is running at https://0.0.0.0:2224/, therefore, append your current URL with hello/Worf%20Son%20of%20Mogh

The Hello Worf Son of Mogh should be returned. Notice that we used ASCII characters, %20 to indicate blank spaces.

Return to your tmux session by moving back to Your Content.

Stop your Flask app by clicking on the terminal window it is running in and pressing CTRL + C

The url_for() function is very useful for dynamically building a URL for a specific function. The function accepts the name of a function as first argument and one or more keyword arguments, each corresponding to the variable part of URL.

Let's write a script to demonstrate the url_for() function.

student@bchd:~/mycode/flaskapi$ vim myflask03.py

Copy and paste the following into myflask03.py


#!/usr/bin/python3
from flask import Flask, redirect, url_for
app = Flask(__name__)

@app.route("/admin")
def hello_admin():
    return "Hello Admin"

@app.route("/guest/<guesty>")
def hello_guest(guesty):
    return f"Hello {guesty} Guest"
    #V2 FORMATTER - return "Hello {} Guest".format(guesty)
    #OLD FORMATTER - return "Hello %s as Guest" % guesty

@app.route("/user/<name>")
def hello_user(name):
    ## if you go to hello_user with a value of admin
    if name =="admin":
        # return a 302 response to redirect to /admin
        return redirect(url_for("hello_admin"))
    else:
        # return a 302 response to redirect to /guest/<guesty>
        return redirect(url_for("hello_guest",guesty = name))

if __name__ == "__main__":
   app.run(host="0.0.0.0", port=2224) # runs the application
Save and exit with :wq

Run the script myflask03.py.

student@bchd:~/mycode/flaskapi$ python3 myflask03.py

The above script has a function user(name) which accepts a value to its argument from the URL. The user() function checks if an argument received matches admin or not. If it matches, the application is redirected to the hello_admin() function using url_for(), otherwise to the hello_guest() function passing the received argument as guest parameter to it.

This time, let's try splitting the screen with tmux. To do a screen split, press (CTRL + b) then (SHIFT + ").

In the newly opened terminal, let's try using CURL to access our links. CURL is short for 'see-URL', and allows us to access HTTP resources from the CLI. It likely is installed, but it won't hurt to double-check.

student@bchd:~/mycode/flaskapi$ sudo apt install curl

Now that the server is running, try to curl against your API. The -L is required to follow the 3xx HTTP responses (forwarded).

student@bchd:~/mycode/flaskapi$ curl http://0.0.0.0:2224/user/admin -L

Did you follow what happened? If not, the following might help:


            http
curl                        flask
GET --------------------> /user/admin
<-----------------------  302 (go to /admin)
GET --------------------> /admin
<-----------------------  200 + plaintext
Try it again, only this time, supply the value /Wolverine

student@bchd:~/mycode/flaskapi$ curl http://0.0.0.0:2224/user/Wolverine -L

Consider what just happened:


            http
curl                        flask
GET --------------------> /user/wolverine
<-----------------------  302 (go to /guest/wolverine)
GET --------------------> /guest/wolverine
<-----------------------  200 + plaintext
Type exit to close your second window and return to your Flask app.

Stop the program with CTRL + C

Now let's try returning a separate HTML document. By default, documents are rendered from a sub directory called templates, so start by creating that directory.

student@bchd:~/mycode/flaskapi$ mkdir templates/

By default, the Flask route responds to the GET requests. However, this preference can be altered by providing methods argument to route() decorator. In order to demonstrate the use of POST method in URL routing, first let us create an HTML form and use the POST method to send form data to a URL. Create a new script called postmaker.html

student@bchd:~/mycode/flaskapi$ vim templates/postmaker.html

Create the following within postmaker.html


<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Sign in with your name</title>
    <form action = "/login" method = "POST">
        <p>Enter Name:</p>
        <p><input type = "text" name = "nm"></p>
        <p><input type = "submit" value = "submit"></p>
    </form>
</head>
<body>

</body>
</html>
Save and exit with :wq

Create a new script called myflask04.py

student@bchd:~/mycode/flaskapi$ vim myflask04.py

Create the following within myflask04.py


#!/usr/bin/python3
"""Alta3 APIs and HTML"""

## best practice says don't use commas in imports
# use a single line for each import
from flask import Flask
from flask import redirect
from flask import url_for
from flask import request
from flask import render_template

app = Flask(__name__)
## This is where we want to redirect users to
@app.route("/success/<name>")
def success(name):
    return f"Welcome {name}\n"
# This is a landing point for users (a start)
@app.route("/") # user can land at "/"
@app.route("/start") # or user can land at "/start"
def start():
    return render_template("postmaker.html") # look for templates/postmaker.html
# This is where postmaker.html POSTs data to
# A user could also browser (GET) to this location
@app.route("/login", methods = ["POST", "GET"])
def login():
    # POST would likely come from a user interacting with postmaker.html
    if request.method == "POST":
        if request.form.get("nm"): # if nm was assigned via the POST
            user = request.form.get("nm") # grab the value of nm from the POST
        else: # if a user sent a post without nm then assign value defaultuser
            user = "defaultuser"
    # GET would likely come from a user interacting with a browser
    elif request.method == "GET":
        if request.args.get("nm"): # if nm was assigned as a parameter=value
            user = request.args.get("nm") # pull nm from localhost:5060/login?nm=larry
        else: # if nm was not passed...
            user = "defaultuser" # ...then user is just defaultuser
    return redirect(url_for("success", name = user)) # pass back to /success with val for name
if __name__ == "__main__":
   app.run(host="0.0.0.0", port=2224) # runs the application
Save and exit with :wq

Run the script myflask04.py

student@bchd:~/mycode/flaskapi$ python3 myflask04.py

This time, let's try splitting the screen with tmux. To do a screen split, press (CTRL + b) then (SHIFT + ").

Now that the server is running, try to curl against your API. The -L is required to follow the 3xx HTTP responses (forwarded). This will send a GET to /login

student@bchd:~/mycode/flaskapi$ curl http://0.0.0.0:2224/login?nm=Wolverine -L

You should receive back, "Hello Wolverine"

Try it again, only this time, do not supply a value for nm=

student@bchd:~/mycode/flaskapi$ curl http://0.0.0.0:2224/login -L

You should receive back, "Hello defaultuser"

Our service is also set up to accept a POST. To use the curl application to send a POST, include the -d flag, along with the query=param values you want afterwards.

student@bchd:~/mycode/flaskapi$ curl http://0.0.0.0:2224/login -L -d nm=Conan%20the%20Librarian

The application should respond back, "Hello Conan the Librarian". However, if you look at the Flask service, you'll see a POST was sent, and not a GET.

Type exit to close the split screen session.

Stop your Flask app by clicking on the terminal window it is running in and pressing CTRL + C

That's it for this lab!

If you're tracking your code in GitHub, issue the following commands:

cd ~/mycode
git add *
git commit -m "My first Flask apps"
git push origin main

