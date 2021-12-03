Flask Sessions
Lab Objective
The objective of this lab is to explore Flask's ability to leverage sessions. A Flask Session is yet another way to store user-specific data between requests. This is similar to cookies, but with a different intended case use.

Cookies are intended to be long-term. Case use could be tracking a users location, or perhaps a preference for JSON versus CSV being returned from an API.

Flask sessions (which are implemented as cookies) are intended for temporary storage of session data. Generally, the session data includes a way to invalidate itself once the browser closes, or after a short period of time (say a half hour). A good use of session cookies could be items in a user's cart.

To create a session, you must set a secret key within Flask. While Flask does perform a basic encryption of session data, it is not secure (YouTube has lots of videos of people decoding session cookies). One created, the session object of the flask package is used to set and get session data. The session object works like a dictionary but it can also keep track of modifications.

For example, to set a 'username' session variable use the statement session["username"] = "admin". To release a session variable use the pop() method, as in, session.pop("username", None).

Procedure
Move into (or create) a new directory to work in, /home/student/mycode/flaskapi/

student@bchd:~$ mkdir ~/mycode/flaskapi/

Move into the new directory.

student@bchd:~$ cd ~/mycode/flaskapi/

Now create a script called session01.py

student@bchd:~/mycode/flaskapi$ vim session01.py

The following code is a simple demonstration of session works in Flask. URL / simply prompts user to log in, as session variable "username" is not set. Copy the following into your Python script, session01.py:


#!/usr/bin/python3

from flask import Flask
from flask import session
from flask import render_template
from flask import redirect
from flask import url_for
from flask import escape
from flask import request

app = Flask(__name__)
app.secret_key = "any random string"

## If the user hits the root of our API
@app.route("/")
def index():
  ## if the key "username" has a value in session
  if "username" in session:
    username = session["username"]
    return "Logged in as " + username + "<br>" + \
      "<b><a href = '/logout'>click here to log out</a></b>"

  ## if the key "username" does not have a value in session
  return "You are not logged in <br><a href = '/login'></b>" + \
      "click here to log in</b></a>"

## If the user hits /login with a GET or POST
@app.route("/login", methods = ["GET", "POST"])
def login():
   ## if you sent us a POST because you clicked the login button
   if request.method == "POST":

      ## request.form["xyzkey"]: use indexing if you know the key exists
      ## request.form.get("xyzkey"): use get if the key might not exist
      session["username"] = request.form.get("username")
      return redirect(url_for("index"))

   ## return this HTML data if you send us a GET
   return """
   <form action = "" method = "post">
      <p><input type = text name = username></p>
      <p><input type = submit value = Login></p>
   </form>
  """

@app.route("/logout")
def logout():
   # remove the username from the session if it is there
   session.pop("username", None)
   return redirect(url_for("index"))

if __name__ == "__main__":
  app.run(host="0.0.0.0", port=2224)
Save and exit with :wq

If a user browses to the root, /, they will be notified they are not logged in, and be prompted to click on a link directing them to, "/login". Upon this click, the user is returned HTML containing a web form. When the returned form is submitted, it is sent to "/login" with a POST. This causes a session variable to be set. The application is then redirected to /, however, this time session variable username is found.

The application also contains a logout() view function, which pops out username session variable. / URL again shows the opening page.

Run your script, session01.py

student@bchd:~/mycode/flaskapi$ python3 session01.py

Split your screen with (CTRL + B) then (SHIFT + ")

Start by sending a cURL to the root. Notice that we get back HTML that would ask us to click a link to go to /login

student@bchd:~$ curl http://0.0.0.0:2224/ -L

Mimic clicking the link to follow /login

student@bchd:~$ curl http://0.0.0.0:2224/login -L

Notice we were returned a web form. Mimic filling out this form, and submitting it via a POST. We also want to accept our session cookie and write the data in session-cookie.txt.

student@bchd:~$ curl http://0.0.0.0:2224/login -L -d "username=Homer" -c session-cookie.txt

Try viewing session-cookie.txt the data should have basic encryption that prevents effortless tampering.

student@bchd:~$ cat session-cookie.txt

Use cURL to access the root again. You should be logged in as the name you assigned yourself within this session.

student@bchd:~$ curl http://0.0.0.0:2224/ -L -b session-cookie.txt

Unfortunately, a small limitation of cURL is that our logout function will not work. However, it does work with browsers! Ask your instructor if you'd like to see a demo of the functionality.

Exit your second window.

student@bchd:~$ exit

Stop your Flask app by clicking on the terminal window it is running in and pressing CTRL + C

Helpful Hint The secret key (random string) within your script should be as random as possible. Your operating system can generate random data if you run the following command:

student@bchd:~/mycode/flaskapi$ python3 -c "import os; print(os.urandom(16))"

Remember, if the random string changes between runs, then all previous session cookies will be invalidated!

Treat session cookies like they have the same limitations of regular cookies. That is to say, don't store sensitive data in a session cookie. It's just not good practice. So what WOULD be a good practice for session data? Hmm, remember our lab where we design an RPG from JSON? Well, Alta3 RPG is back! This time, the game has been broken into two pieces. The server side is handled with Flask, whereas the client is your browser (or CURL). The 'state' of your character within the game is stored as a session cookie. The 'stable' version of the game is available from Alta3. Try cloning and running that project now. To start, move into home.

student@bchd:~$ cd ~/

Clone the project (the project is maintained by the course author).

student@bchd:~$ git clone https://github.com/rzfeeser/api-quest

Move into the new directory.

student@bchd:~$ cd ~/api-quest

You'll be on the master branch. Start on the branch stable-1.0, which mimics the game you made previously.

student@bchd:~/api-quest$ git checkout stable-1.0

Review the code that makes this Flask RPG possible.

student@bchd:~/api-quest$ vim rpgserver.py

This code is best demoed from a tool such as PyCharm (run locally). PyCharm offers special support for Flask, and makes coding APIs in Windows quite easy (although it is also supported on Apple IOS). If you cannot run the code locally, cannot install PyCharm, or have never used PyCharm, ask the instructor to demonstrate it for you.

If you do get the game running, try creating a new feature! If you come up with something, be sure to commit and issue a pull request to https://github.com/rzfeeser/api-quest Maybe your feature will become part of the game.

If you're tracking your code in GitHub, issue the following commands:

cd ~/mycode
git add *
git commit -m "Flask sessions"
git push origin main
