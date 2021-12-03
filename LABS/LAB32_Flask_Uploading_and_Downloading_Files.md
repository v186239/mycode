# Flask Redirection, Errors, and API Limiting
Lab Objective
The objective of this lab is to explore redirection, errors and API limiting. Flask class has a redirect() function. When called, it returns a response object and redirects the user to another target location with specified status code.

Consider Flask.redirect(location, statuscode, response). The location parameter is the URL where response should be redirected. The statuscode is sent to the browser’s header, which defaults to 302. The response parameter is used to instantiate response.

The following status codes are standardized: HTTP_300_MULTIPLE_CHOICES, HTTP_301_MOVED_PERMANENTLY, HTTP_302_FOUND, HTTP_303_SEE_OTHER, HTTP_304_NOT_MODIFIED, HTTP_305_USE_PROXY, HTTP_306_RESERVED, HTTP_307_TEMPORARY_REDIRECT

Limiting is a way to throttle our users from over-consuming data. This may be unintentional, or malicious in nature (think DOS attacking). Flask API limiting is best handled by the following package.

Flask Limiter:
https://flask-limiter.readthedocs.io/en/stable/

Procedure
Open a new terminal.

Move into (or create) a new directory to work in, /home/student/mycode/flaskapi/

student@bchd:~$ mkdir -p /home/student/mycode/flaskapi/

You'll also need a templates directory for our jinja template.

student@bchd:~$ mkdir -p /home/student/mycode/flaskapi/templates/

Now create the template.

student@bchd:~$ vim ~/mycode/flaskapi/templates/log_in.html

Copy and paste the following into the template:


<html>
        <body>
            <form action = "/login" method = "POST">
            <p><h3>Enter your login credential</h3></p>
            <p><input type = "text" name = "username"/></p>
            <p><input type = "submit" value = "Login"/></p>
            </form>
        </body>
</html>
Save and exit with :wq

Move into the new directory.

student@bchd:~$ cd ~/mycode/flaskapi/

Now create a script called redirect01.py

student@bchd:~/mycode/flaskapi$ vim redirect01.py

In the following example, the redirect() function is used to display the login page again when a login attempt fails. The failure will occur if anyone except admin tries to log in. Copy the following into your Python script, redirect01.py:


#!/usr/bin/python3
"""
Making use of HTTP non-200 type responses.
https://tools.ietf.org/html/rfc2616 # rfc spec describing HTTP
1xx - informational
2xx - success / ok
3xx - redirection
4xx - errors
5xx - server errors
"""

from flask import Flask
from flask import redirect
from flask import url_for
from flask import render_template
from flask import request
from flask import abort

app = Flask(__name__)

# if user sends GET to / (root)
@app.route("/")
def index():
    return render_template("log_in.html")   # found in templates/

# if user sends GET or POST to /login
@app.route("/login", methods = ["POST", "GET"])
def login():
    # if user sent a POST
    if request.method == "POST":
        # if the POST contains 'admin' as the value for 'username'
        if request.form["username"] == "admin" :
            return redirect(url_for("success")) # return a 302 redirect to /success
        else:
            abort(401)  # if they didn't supply the username 'admin' send back a 401
    elif request.method == "GET":
        return redirect(url_for("index")) # if they sent a GET to /login send 302 redirect to /

@app.route("/success")
def success():
    return "logged in successfully"

if __name__ == "__main__":
   app.run(host="0.0.0.0", port=2224)
Save and exit with :wq

Run your script, redirect01.py

student@bchd:~/mycode/flaskapi$ python3 redirect01.py

Split your screen with (CTRL + B) then (SHIFT + ")

In the new screen cURL your API with a GET. The root should return a webform, which would be of interest to users accessing your API with a browser. Notice that use of this form will result in sending a POST to /login

student@bchd:~$ curl http://0.0.0.0:2224 -L

In the new screen cURL your API by generating a POST. This step mimics using a browser to click the "Submit" button. This should NOT work, as cupcake is not a valid user. You will get a 401 response.

student@bchd:~$ curl http://0.0.0.0:2224/login -d "username=cupcake" -L

In the new screen cURL your API by generating a POST. This should SHOULD work, as admin is a valid user.

student@bchd:~$ curl http://0.0.0.0:2224/login -d "username=admin" -L

Close the new window by typing exit.

student@bchd:~$ exit

Stop your Flask app by clicking on the terminal window it is running in and pressing CTRL + C

If you want to try out some other error codes, try the following in place of the 401:


400 for Bad Request

401 for Unauthenticated

403 for Forbidden

404 for Not Found

406 for Not Acceptable

415 for Unsupported Media Type

429 for Too Many Requests
API limiting is a way to throttle how fast a user can consume our API resources. There is good reason to do this, after all, lockups aren't free! Flask API limiting is best handled by Flask limiter. First, install Flask Limiter.

student@bchd:~/mycode/flaskapi$ python3 -m pip install Flask-Limiter

Create a new script:

student@bchd:~/mycode/flaskapi$ vim limitedapis.py

Great. Now write the following script. Be sure to read the comments:


from flask import Flask
## from python3 -m pip install Flask-Limiter
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

# create an app object from Flask
app = Flask(__name__)

# create a limiter object from Limiter
# limits are being performed by tracking the
# REMOTE ADDRESS of the clients
limiter = Limiter(
    app,
    key_func=get_remote_address,
    default_limits=["200 per day", "50 per hour"]
)

# we now have TWO decorators on our function
# app.route() describes WHEN to trigger the function
# limiter.limit() describes HOW OFTEN to trigger the function
@app.route("/slow")
@limiter.limit("1 per day")
def slow():
    return "Enjoy this message. It will only display once per day."

# No limiter decorator is needed, this function STILL is limited
# by 200 lookups per day, and 50 per hour
@app.route("/fast")
def fast():
    return "I inherit the default limits of 200 per day and 50 per hour."

## limiter().exempt removes all limits on this API
@app.route("/ping")
@limiter.exempt
def ping():
    return "PONG FOREVER!"
    
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=2224)
Save and exit with :wq

Try running your server.

student@bchd:~/mycode/flaskapi$ python3 limitedapis.py

Split your screen with (CTRL + B) then (SHIFT + ")

In the new screen cURL your API with a GET to /slow. This will work once.

student@bchd:~$ curl http://0.0.0.0:2224/slow

Try it again. This time the limiter will cause a fail.

student@bchd:~$ curl http://0.0.0.0:2224/slow

Try out the other endpoints, /fast. This will work 200 times per day, 50 times per hour.

student@bchd:~$ curl http://0.0.0.0:2224/fast

The other endpoint was /ping. This is excluded from our limiting. Therefore, /ping works forever.

student@bchd:~$ curl http://0.0.0.0:2224/ping

Close the new window by typing exit.

student@bchd:~$ exit

Stop your Flask app by clicking on the terminal window it is running in and pressing CTRL + C

CHALLENGE: Write a client that can issue 51 lookups to /fast. The last lookup should fail.

If you're tracking your code in GitHub, issue the following commands:

cd ~/mycode
git add *
git commit -m "Errors redirects and limits"
git push origin main
Type in username and password
