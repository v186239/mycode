Flask APIs and Jinja2
Lab Objective
The objective of this lab is to continue to explore building APIs with Flask. In this example, we'll leverage the use of a Jinja2 template. Our API will first render an HTML template and return that in the HTTP request. This is an 'older' method of transmitting data. Today it's much more popular just to return JSON. The client can then parse out that JSON and display the data.

Jinja2 - A popular templating engine for Python. A web templating system combines a template with a certain data source to render dynamic web pages. The offical Jinja2 documentation can be found here: http://jinja.pocoo.org/docs/2.10/

Procedure
Open a new terminal.

Move into (or create) a new directory to work in, /home/student/mycode/flaskapi/

student@bchd:~$ mkdir -p /home/student/mycode/flaskapi/

Move into the new directory:

student@bchd:~$ cd ~/mycode/flaskapi/

We can now take advantage of Jinja2 template engine on which Flask is based. Instead of returning hardcoded HTML from the function, a HTML file can be rendered by the render_template() function.

Now create a script called jinja2temp01.py

student@bchd:~/mycode/flaskapi$ vim jinja2temp01.py

Copy the following into your Python script, jinja2temp01.py


#!/usr/bin/env python3
from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("hellobasic.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=2224)
Save and exit with :wq

Create a directory called ~/mycode/flaskapi/templates/

student@bchd:~/mycode/flaskapi$ mkdir ~/mycode/flaskapi/templates/

Move into the new directory. When you run your application from ~/mycode/flaskapi/ it will look for templates in the folder ~/mycode/flaskapi/template by default.

student@bchd:~/mycode/flaskapi$ cd ~/mycode/flaskapi/templates/

Now create a script called hellobasic.html

student@bchd:~/mycode/templates/$ vim hellobasic.html

Copy and paste the following into your Jinja2 template, hellobasic.html


<!doctype html>
<html>
   <body>
      <h1>Hello!</h1>
   </body>
</html>
Save and exit with :wq

Move back into your application directory.

student@bchd:~/mycode/flaskapi/templates$ cd ~/mycode/flaskapi/

Run your script, jinja2temp01.py

student@bchd:~/mycode/flaskapi$ python3 jinja2temp01.py

Split your screen with (CTRL + B) then (SHIFT + ")

In the new screen cURL your API.

student@bchd:~$ curl http://0.0.0.0:2224 -L

Your screen should display the following:


<!doctype html>
<html>
   <body>
       <h1>Hello!</h1>
   </body>
</html>
Alternatively, you may visit aux1 where the screen should display Hello! in bold.

Close the new window by typing exit.

student@bchd:~$ exit

Stop your Flask app by clicking on the terminal window it is running in and pressing CTRL + C

Now create a script called jinja2temp02.py

student@bchd:~/mycode/flaskapi$ vim jinja2temp02.py

Copy the following into your Python script, jinja2temp02.py


#!/usr/bin/env python3
from flask import Flask
from flask import render_template

app = Flask(__name__)

#grab the value 'username'
@app.route("/<username>")
def index(username):
    # render the jinja template "helloname.html"
    # apply the value of username for the var name
    return render_template("helloname.html", name = username)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=2224)
Save and exit with :wq

Now create a template called templates/helloname.html

student@bchd:~/mycode/flaskapi$ vim templates/helloname.html

Copy and paste the following into your Jinja2 template, helloname.html


<!doctype html>
<html>
   <body>
      <h1>Hello {{ name }}!</h1>
   </body>
</html>
Save and exit with :wq

Flask uses Jinja2 template engine. A web template contains HTML syntax interspersed with placeholders for variables and expressions (in these case Python expressions) which are replaced values when the template is rendered. In the above example, the variable {{name}} will be replaced. Read about Jinja2 here: http://jinja.pocoo.org/docs/2.10/ you may want to pay sepecial attention to the templates section: https://jinja.palletsprojects.com/en/2.10.x/templates/

Run your script, jinja2temp02.py

student@bchd:~/mycode/flaskapi$ python3 jinja2temp02.py

Split your screen with (CTRL + B) then (SHIFT + ")

In the new screen cURL your API. The %20 is ASCII for whitespace.

student@bchd:~$ curl http://0.0.0.0:2224/James%20Bond -L

The screen should display the following:


<!doctype html>
<html>
   <body>
      <h1>Hello James Bond!</h1>
   </body>
</html>
Close the new window by typing exit.

student@bchd:~$ exit

Stop your Flask app by clicking on the terminal window it is running in and pressing CTRL + C

Now create a script called jinja2temp03.py

student@bchd:~/mycode/flaskapi$ vim jinja2temp03.py

Copy the following into your Python script, jinja2temp03.py


#!/usr/bin/python3
from flask import Flask
from flask import render_template

app = Flask(__name__)

# pull in the value of score as an int
@app.route("/scoretest/<int:score>")
def hello_name(score):
    # render the template with the value of score for marks
    # marks is a jinja var in the template
    return render_template("highscore.html", marks = score)

if __name__ == "__main__":
   app.run(host="0.0.0.0", port=2224)
Save and exit with :wq

Now create a template called templates/highscore.html

student@bchd:~/mycode/flaskapi$ vim templates/highscore.html

Copy and paste the following into your Jinja2 template, highscore.html


<!doctype html>
<html>
   <body>
   
      {% if marks>50 %}
      <h1> You passed! Well done :)</h1>
      {% else %}
      <h1>You failed :(</h1>
      {% endif %}
      
   </body>
</html>
Save and exit with :wq

Note that the conditional statements if-else and endif are enclosed in delimiter {%..%}. Read about Jinja2 conditionals here http://jinja.pocoo.org/docs/2.10/templates/

Run your script, jinja2temp03.py

student@bchd:~/mycode/flaskapi$ python3 jinja2temp03.py

Split your screen with (CTRL + B) then (SHIFT + ")

In the new screen cURL your API.

student@bchd:~$ curl http://0.0.0.0:2224/scoretest/101 -L

The screen should display <h1> You passed! Well done :)</h1>

Now, try to cURL http://0.0.0.0:2224/scoretest/42.

student@bchd:~$ curl http://0.0.0.0:2224/scoretest/42 -L

<h1>You failed :(</h1> should be returned.

Finally, try to cURL http://0.0.0.0:2224/scoretest/99.

student@bchd:~$ curl http://0.0.0.0:2224/scoretest/99 -L

<h1> You passed! Well done :)</h1> should be returned.

Close the new window by typing exit.

student@bchd:~$ exit

Stop your Flask app by clicking on the terminal window it is running in and pressing CTRL + C

HTML documents are not the ONLY thing we could render with Jinja. For many, it might be more practical to render something like a switch config. Create a new template that will contain a Cisco IOS switch configuration template.

student@bchd:~/mycode/flaskapi$ vim templates/baseIOS.conf.j2

Create the following Jinja template within baseIOS.conf.j2


!=== {{ switchname }} ===!

!--- IOS config ---!
enable
configure terminal
hostname {{ switchname }}

!--- MGMT ---!
username {{ username }} secret alta3
ip route 0.0.0.0 0.0.0.0 {{ defaultgateway }}
interface Management 1
ip address {{ switchIP }} {{ netmask }}
mtu {{ mtusize }}
exit

!--- SSH ---!
management ssh
  idle-timeout 0
  authentication mode keyboard-interactive
  server-port 22
  no fips restrictions
  no hostkey client strict-checking
  no shutdown
  login timeout 120
  log-level info
exit
exit
write memory
Save and exit with :wq

Let's write a new Flask application that can return a completed switch config.

student@bchd:~/mycode/flaskapi$ vim ciscoios.py

If you only need to support GET requests, no need to include the methods in your route decorator (such as POST). Everything beyond the "?" in your request is called a query parameter. Flask will take those query parameters out of the URL and place them into an ImmutableDict. You can access it with request.args, either with the key, request.args["switchname"] or with the get method. If you do use the get method, you expose an added ability to pass a default value (such as None), in the event it is not present. This is common for query parameters since they are often optional. Okay, now create the following Flask application:


#!/usr/bin/python3
from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)

@app.route("/ciscoios/")
def ciscoios():
    try:
        qparms = {}
        # user passes switchname= or default "bootstrapped switch"
        qparms["switchname"]  = request.args.get("switchname", "bootstrapped switch")
        # user passes username= or default "admin"
        qparms["username"]  = request.args.get("username", "admin")
        # user passes gateway= or default "0.0.0.0"
        qparms["defaultgateway"] = request.args.get("gateway", "0.0.0.0")
        # user passes ip= or default "0.0.0.0"
        qparms["switchIP"] = request.args.get("ip", "0.0.0.0")
        # user passes mask= or default "255.255.255.0"
        qparms["netmask"] = request.args.get("mask", "255.255.255.0")
        # user passes mtu= or default "1450"
        qparms["mtusize"] = request.args.get("mtu", "1450")

        # render template and save as baseIOS.conf
        return render_template("baseIOS.conf.j2", **qparms)

    except Exception as err:
        return "Uh-oh! " + err

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=2224)
Save and exit with :wq

Run your script, ciscoios.py

student@bchd:~/mycode/flaskapi$ python3 ciscoios.py

Split your screen with (CTRL + B) then (SHIFT + ")

In the new screen cURL your API.

student@bchd:~$ curl http://0.0.0.0:2224/ciscoios/ -L

The default Cisco IOS config should be returned.

Issue the following command. The command is long, so it wraps in the manual, however, the only space in the command is after curl. Customize yours to include query parameters with your lookup. Query parameters are separated with the ampersand, which also is a shell command, therefore, it is important that you quote the URI you construct.


 curl "http://0.0.0.0:2224/ciscoios/?switchname=hal9000&username=dreadpirateroberts&ip=192.168.0.1&mtu=1450&gateway=172.0.0.1" -L
Try reworking the curl command. Each time, check the file returned to see that it is being customized to your liking.

Close the new window by typing exit.

student@bchd:~$ exit

Stop your Flask app with (CTRL + C)

Question: If you include erroneous query parameters in your lookup, do you still get back a CiscoIOS config?

Answer: YES! The parameters that are not needed are simply ignored
If you're tracking your code in GitHub, issue the following commands:

cd ~/mycode
git add *
git commit -m "Jinja templating for HTML and configs"
git push origin main

