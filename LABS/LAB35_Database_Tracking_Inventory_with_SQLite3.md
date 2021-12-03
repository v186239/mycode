# Tracking Inventory with sqlite
Lab Objective
We're going to create two applications: a flask API that manipulates a SQL database, as well as a client to speak to our API. Our application is going to track a collection of student information, but could easily be manipulated to track any type of collection.

Be sure to check up on Python sqlite3 module's official documentation: https://docs.python.org/3/library/sqlite3.html

Procedure
Create a new directory to work in and a place to stash templates: ~/mycode/myapp/templates/

student@bchd:~$ mkdir -p /home/student/mycode/myapp/templates/

Move into your new directory.

student@bchd:~$ cd /home/student/mycode/myapp

Create a new script, server01.py. This script will handle our server-side logic: hosting the Flask API, interacting with and connecting to the sqlite database.

student@bchd:~/mycode/myapp$ vim server01.py

Copy and paste the following into your script.


#!/usr/bin/python3
"""RZFeeser || Alta3 Research
Tracking student inventory within a sqliteDB accessed
via Flask APIs"""

# standard library
import sqlite3 as sql

# python3 -m pip install flask
from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)

# return home.html (landing page)
@app.route('/')
def home():
    return render_template('home.html')

# return student.html (a way to add a student to our sqliteDB)
@app.route('/enternew')
def new_student():
    return render_template('student.html')

# if someone uses student.html it will generate a POST
# this post will be sent to /addrec
# where the information will be added to the sqliteDB
@app.route('/addrec',methods = ['POST'])
def addrec():
    try:
        nm = request.form['nm']         # student name
        addr = request.form['addr']     # student street address
        city = request.form['city']     # student city
        pin = request.form['pin']       # "pin" assigned to student
                                        # ("pin" is just an example of meta data we want to track)

        # connect to sqliteDB
        with sql.connect("database.db") as con:
            cur = con.cursor()

            # place the info from our form into the sqliteDB
            cur.execute("INSERT INTO students (name,addr,city,pin) VALUES (?,?,?,?)",(nm,addr,city,pin) )
            # commit the transaction to our sqliteDB
            con.commit()
        # if we have made it this far, the record was successfully added to the DB
        msg = "Record successfully added"
        
    except:
        con.rollback()  # this is the opposite of a commit()
        msg = "error in insert operation"    # we were NOT successful

    finally:
        con.close()     # successful or not, close the connection to sqliteDB
        return render_template("result.html",msg = msg)    #

# return all entries from our sqliteDB as HTML
@app.route('/list')
def list_students():
    con = sql.connect("database.db")
    con.row_factory = sql.Row
    
    cur = con.cursor()
    cur.execute("SELECT * from students")           # pull all information from the table "students"
    
    rows = cur.fetchall()
    return render_template("list.html",rows = rows) # return all of the sqliteDB info as HTML

if __name__ == '__main__':
    try:
        # ensure the sqliteDB is created
        con = sql.connect('database.db')
        print("Opened database successfully")
        # ensure that the table students is ready to be written to
        con.execute('CREATE TABLE IF NOT EXISTS students (name TEXT, addr TEXT, city TEXT, pin TEXT)')
        print("Table created successfully")
        con.close()
        # begin Flask Application 
        app.run(host="0.0.0.0", port=2224, debug = True)
    except:
        print("App failed on boot")
Save and exit with :wq

Create an HTML script for student.html

student@bchd:~/mycode/myapp$ vim templates/student.html

Copy and paste the following into your new script. As it can be seen, form data is posted to the /addrec URL which binds the addrec() function.


<html>
   <body>
      <form action = "{{ url_for('addrec') }}" method = "POST">
         <h3>Student Information</h3>
         Name:<br>
         <input type = "text" name = "nm" /><br>
         
         Address:<br>
         <textarea name = "addr" ></textarea><br>
         
         City:<br>
         <input type = "text" name = "city" /><br>
         
         PINCODE<br>
         <input type = "text" name = "pin" /><br>
         <input type = "submit" value = "submit" /><br>
      </form>
   </body>
</html>
Save and exit with :wq

In our script, notice that the addrec() function retrieves the form’s data via a POST method and inserts in the table. A message corresponding to a success or error is rendered to result.html. We should create the script result.html now.

student@bchd:~/mycode/myapp$ vim templates/result.html

Copy and paste the following into the new script. The escaping statement (msg) should display the result of the insert operation.


<!doctype html>
<html>
   <body>
      result of addition : {{ msg }}
      <h2><a href = "\">go back to home page</a></h2>
   </body>
</html>
Save and exit with :wq

We'll need list.html, another template, which iterates over the row set and renders the data in an HTML table.

student@bchd:~/mycode/myapp$ vim templates/list.html


<!doctype html>
<html>
   <body>
      <table border = 1>
         <thead>
            <td>Name</td>
            <td>Address</td>
            <td>City</td>
            <td>Pincode</td>
         </thead>
         
         {% for row in rows %}
            <tr>
               <td>{{ row["name"] }}</td>
               <td>{{ row["addr"] }}</td>
               <td>{{ row["city"] }}</td>
               <td>{{ row["pin"] }}</td>	
            </tr>
         {% endfor %}
      </table>
      
      <a href = "/">Go back to home page</a>
   </body>
</html>
Save and exit with :wq

At one point we need to render a home.html which acts as the entry point of the application.

student@bchd:~/mycode/myapp$ vim templates/home.html

Copy and paste the following into your new script.


<!doctype html>
<html>
   <body>
      <h2>Welcome to my Flask & database app</h2>
      <a href = "/">Home Page (you are here)</a>
      <a href = "/enternew">Make a New Database Entry</a>
      <a href = "/list">View Records in the Database</a>
   </body>
</html>
Try running your script!

student@bchd:~/mycode/myapp$ python3 server01.py

Create a new record or two. Fill the appropriate form fields and submit it. The underlying function inserts the record in the students table. Click ‘Show List’ link to see the current data within the sqlite database.

Back in your SECOND TMUX PANE, cURL the root of your API.

student@bchd:~$ curl http://127.0.0.1:2224/

We can make an addition by sending a POST to /addrec. Let's try that now.

student@bchd:~$ curl http://127.0.0.1:2224/addrec -d "nm=David" -d "addr=Texas" -d "city=Dallas" -d "pin=1"

Great! Looks like a user was successfully added! Let's now add a second one.

student@bchd:~$ curl http://127.0.0.1:2224/addrec -d "nm=Tailor" -d "addr=FL" -d "city=Orlando" -d "pin=2"

Try getting everything out of the students table within the database. The result of this cURL command will be a an HTML page dynamically populated students from the sqlite database.

student@bchd:~$ curl http://127.0.0.1:2224/list

CHALLENGE 01: Try to make an entry and commit it to the database. Then pull your results.

CHALLENGE 02 - Add functionality to the script, so that a student may be REMOVED from the database.

CHALLENGE 03 - Rewrite this script to do track data you might be interested in. This could be prices of things on the internet, an inventory of some collection, teams, resources, staff, or anything else you dream up. To be successful your script doesn't need to be as complex as the script we wrote in this lab.

If you're tracking your code in GitHub, issue the following commands:

cd ~/mycode
git add *
git commit -m "Learning about APIs and DBs"
git push origin main

