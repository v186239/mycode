#!/usr/bin/python3
"""Alta3 APIs and HTML"""
## best practice says don't use commas in imports
# use a single line for each import
from flask import Flask
from flask import redirect
from flask import url_for
from flask import request
from flask import render_template
from flask import jsonify

app = Flask(__name__)

jsondata= []

## This is where we want to redirect users to

@app.route("/post", methods=["POST"])
def post():
    #request.form   # accessing form data from the post (submitted via HTML)
    #request.args   # accessing data from query params (?name=Chad)
    #request.method # accessing what type of request method was used (GET, POST)
    #request.json   # accessing json attached to the post
    data= request.json
    # data now contains the JSON submitted by the client

    # if JSON was actually sent:
    if data:
        # treat "data" like a dictionary!
        nm= data["name"]
        jsondata.append({"nm":nm,})
    return redirect("/")

@app.route("/success/<name>")
def success(name):
    return f"{name}\n"
# This is a landing point for users (a start)
@app.route("/") # user can land at "/"
@app.route("/start") # or user can land at "/start"
def start():
    return render_template("trivia.html") # look for templates/postmaker.html
# This is where postmaker.html POSTs data to
# A user could also browser (GET) to this location
@app.route("/login", methods = ["POST"])
def login():
        if request.json:
            data= request.json
            if data["nm"] == "chicken":
                return redirect("/correct")

#@app.route("/login", methods = ["POST", "GET"])
#def login():
    # POST would likely come from a user interacting with postmaker.html
#    if request.method == "POST":
#        if request.form.get("nm"): # if nm was assigned via the POST
#            answer = request.form.get("nm") # grab the value of nm from the POST
#            if answer == "chicken":
#                user = answer + '\n' ' Yeah Lets Eat'
#            else:
#                user = " I'm still Hungry Try Again"
#        else: # if a user sent a post without nm then assign value defaultuser
#            user = "I'm still Try Again"
#    # GET would likely come from a user interacting with a browser
#    elif request.method == "GET":
#        if request.args.get("nm"): # if nm was assigned as a parameter=value
#            user = request.args.get("nm") # pull nm from localhost:5060/login?nm=larry
#        else: # if nm was not passed...
#            user = "defaultuser" # ...then user is just defaultuser
#    return redirect(url_for("success", name = user)) # pass back to /success with val for name

@app.route("/")
def index():
    # how to have a Flask API return object as JSON
    return jsonify(jsondata)

if __name__ == "__main__":
   app.run(host="0.0.0.0", port=2224) # runs the application
