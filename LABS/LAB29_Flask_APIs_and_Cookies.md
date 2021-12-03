Flask APIs and Cookies
Lab Objective
The objective of this lab is to explore Flask APIs and interacting with cookies. A cookie is stored on a client’s computer in the form of a text file. Its purpose is to remember and track data pertaining to a client’s usage for better visitor experience and site statistics.

A Request object contains a cookie’s attribute. It is a dictionary object of all the cookie variables and their corresponding values that a client has transmitted. In addition to that, a cookie also stores its expiry time, path, and domain name of the site.

In Flask, cookies are set on response object. Use make_response() function to get response object from return value of a view function. After that, use the set_cookie() function of response object to store a cookie.

Reading back a cookie is easy. The get() method of request.cookies attribute is used to read a cookie.

On the client side, cookies are typically managed by browsers. However, in this lab, we're going to learn to use curl to interact with the cookies returned by APIs. Before you begin, you should read about how curl manages cookies: https://curl.haxx.se/docs/http-cookies.html

Procedure
Open a new terminal.

Move into (or create) a new directory to work in, /home/student/mycode/flaskapi/

student@bchd:~$ mkdir -p /home/student/mycode/flaskapi/

Move into your new directory

student@bchd:~$ cd ~/mycode/flaskapi/

Now create a script called milkncookies.py

student@bchd:~/mycode/flaskapi$ vim milkncookies.py

Copy the following into your Python script, milkncookies.py


#!/usr/bin/env python3
from flask import Flask
from flask import make_response
from flask import request
from flask import render_template
from flask import redirect
from flask import url_for

app = Flask(__name__)

# entry point for our users
# renders a template that asks for their name
# login.html points to /setcookie
@app.route("/login")
@app.route("/")
def index():
    return render_template("login.html")

# set the cookie and send it back to the user
@app.route("/setcookie", methods = ["POST", "GET"])
def setcookie():
    # if user generates a POST to our API
    if request.method == "POST":
        if request.form.get("nm"): # if nm was assigned via the POST
        #if request.form["nm"] <-- this also works, but returns ERROR if no nm
            user = request.form.get("nm") # grab the value of nm from the POST
        else: # if a user sent a post without nm then assign value defaultuser
            user = "defaultuser"

        # Note that cookies are set on response objects.
        # Since you normally just return strings
        # Flask will convert them into response objects for you
        resp = make_response(render_template("readcookie.html"))
        # add a cookie to our response object
                        #cookievar #value
        resp.set_cookie("userID", user)

        # return our response object includes our cookie
        return resp
        
    if request.method == "GET": # if the user sends a GET
        return redirect(url_for("index")) # redirect to index

# check users cookie for their name
@app.route("/getcookie")
def getcookie():
    # attempt to read the value of userID from user cookie
    name = request.cookies.get("userID") # preferred method
    
    # name = request.cookies["userID"] # <-- this works but returns error
                                       # if value userID is not in cookie
    
    # return HTML embedded with name (value of userID read from cookie) 
    return f'<h1>Welcome {name}</h1>'

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=2224)
Save and exit with :wq

When you run your application, flask will look for templates within the folder, templates/, by default.

student@bchd:~/mycode/flaskapi/$ mkdir templates/

Within the templates folder, create a template called login.html.

student@bchd:~/mycode/flaskapi$ vim templates/login.html

Copy and paste the following into your template, login.html.


<!doctype html>
<html>
   <body>          
      <form action = "/setcookie" method = "POST">
         <p><h3>Enter userID</h3></p>
         <p><input type = "text" name = "nm"/></p>
         <p><input type = "submit" value = 'Login'/></p>
      </form>
   </body>
</html>
Save and exit with :wq

We are also going to need a template called readcookie.html. This will contain a simple redirection link to our getcookie resource.

student@bchd:~/mycode/flaskapi$ vim templates/readcookie.html

Copy and paste the following into your template, readcookie.html.


<!doctype html>
<html>
   <body>
      <h1> <p> A cookie has been set on your system! </p>
           <p> <a href="/getcookie">Click here to Read The Cookie</a> </p>
      </h1>
   </body>
</html>
Save and exit with :wq

Run your script, milkncookies.py

student@bchd:~/mycode/flaskapi$ python3 milkncookies.py

Split your screen with (CTRL + B) then (SHIFT + ")

In the new screen cURL your API. The page asking for you name should be displayed.

student@bchd:~$ curl http://0.0.0.0:2224/ -L

Rework the cURL command to send a POST. This behavior mimics a user filling in their name Larry, and pressing the 'Submit' button.

student@bchd:~$ curl http://0.0.0.0:2224/setcookie -d "nm=Larry" -L

Looks like a cookie has been set on our system! Great. Let's try following that link to read the cookie on our system.

student@bchd:~$ curl http://0.0.0.0:2224/getcookie -L

Hmm, it looks like we're "Nobody". Time to dive a bit deeper into how cookies work.

cURL has a built in "cookie engine" that mimics the Netscape navigator standard. In order to write a cookie to a file, we just use -c followed by the name of the cookie we want to create. The following command will accept the cookie information returned from the server, and write it into cookie-jar.txt (the name of the file is not important).

student@bchd:~$ curl http://0.0.0.0:2224/setcookie -d "nm=larry" -L -c cookie-jar.txt

Review cookie-jar.txt.

student@bchd:~$ cat cookie-jar.txt

Looks like information was recorded on our system (in our cookie) that we are larry. Notice the IP address of the server was also provided (in production, we'd likely see a domain).

Once again, let's try access /getcookie, only this time, we'll make our cookie, cookie-jar.txt available to Flask.

student@bchd:~$ curl http://0.0.0.0:2224/getcookie -L -b cookie-jar.txt

And there you go! The system should now recognize you as Larry! If you had used a browser, the browser would of managed the cookie, and made it available to the API (website) you were visiting.

Try changing the value found in your cookie. You can make nm= to anything you would like.

student@bchd:~$ curl http://0.0.0.0:2224/setcookie -d "nm=Frodo%20Baggins" -L -c cookie-jar.txt

Review cookie-jar.txt. Notice it has been updated.

student@bchd:~$ cat cookie-jar.txt

Try to access /getcookie. Make the cookie, cookie-jar.txt, available to Flask.

student@bchd:~$ curl http://0.0.0.0:2224/getcookie -L -b cookie-jar.txt

The system should send a greeting to your new user.

CHALLENGE: Manually hack your cookie, and then have the new user returned by the API /getcookie. HINT: Within cookie-jar.txt, replace the value represented by userID to something else. When you finish, try to cURL /getcookie. Be sure to include your cookie!

Close the new window by typing exit.

student@bchd:~$ exit

Stop your Flask app with (CTRL + C)

If you're tracking your code in GitHub, issue the following commands:

cd ~/mycode
git add *
git commit -m "serving cookies"
git push origin main
Type username and password
