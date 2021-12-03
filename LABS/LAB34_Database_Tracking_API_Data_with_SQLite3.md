# Tracking API Data with sqlite3
Lab Objective
The objective of this lab is to create a practical application that can harness data from an API and then save it within a SQL database for long term storage. This application is written to look up data from the Open Movies DataBase (OMDB) API, but could easily be modified to look up data from other API sources.

Procedure
In this lab, we'll use the Open Movie Data Base API to grab some metadata about movies to write into our local SQL database. Create a new directory to work in, ~/mycode/apisqlite/

student@bchd:~$ mkdir /home/student/mycode/apisqlite

Move into your new directory.

student@bchd:~$ cd /home/student/mycode/apisqlite

To have success with this lab, you'll need to go to https://www.omdbapi.com/apikey.aspx and sign up for an API key. Be sure to only sign up for a FREE account.

You'll need to confirm your API key via an email. Click the link at the bottom of the email to confirm your key.

Create a file to store your key in.

student@bchd:~/mycode/apisqlite$ vim ~/omdb.key

Copy your key out of your email, and paste it into this file. Your key is only 8 characters long, and should be at the top of the email itself. When you paste it into this file, be sure you didn't include any extra lines or whitespaces.

Save and exit with :wq

Create a new python script.

student@bchd:~/mycode/apisqlite$ vim apisqlite01.py

Copy and paste the following into your new script:


#!/usr/bin/env python3
""" Author: RZFeeser || Alta3 Research
Gather data returned by various APIs published on OMDB, and cache in a local SQLite DB
"""

import json
import sqlite3
import requests

# Define the base URL
OMDBURL = "http://www.omdbapi.com/?"

# search for all movies containing string
def movielookup(mykey, searchstring):
    """Interactions with OMDB API
       mykey = omdb api key
       searchstring = string to search for"""
    try:
        # begin constructing API
        api = f"{OMDBURL}apikey={mykey}&s={searchstring}"

        ## open URL to return 200 response
        resp = requests.get(api)
        ## read the file-like object decode JSON to Python data structure
        return resp.json()
    except:
        return False

def trackmeplease(datatotrack):
    conn = sqlite3.connect('mymovie.db')
    try:
        conn.execute('''CREATE TABLE IF NOT EXISTS MOVIES (TITLE TEXT PRIMARY KEY NOT NULL, YEAR INT  NOT NULL);''')

        # loop through the list of movies that was passed in
        for data in datatotrack:
            # in the line below, the ? are examples of "bind vars"
            # this is best practice, and prevents sql injection attacks
            # never ever use f-strings or concatenate (+) to build your executions
            conn.execute("INSERT INTO MOVIES (TITLE,YEAR) VALUES (?,?)",(data.get("Title"), data.get("Year")))
            conn.commit()

        print("Database operation done")
        conn.close()
        return True
    except:
        return False

# Read in API key for OMDB
def harvestkey():
    with open("/home/student/omdb.key") as apikeyfile:
        return apikeyfile.read().rstrip("\n") # grab the api key out of omdb.key

def printlocaldb():
    pass
    #cursor = conn.execute("SELECT * from MOVIES")
    #for row in cursor:
    #    print("MOVIE = ", row[0])
    #    print("YEAR = ", row[1])


def main():

    # read the API key out of a file in the home directory
    mykey = harvestkey()

    # enter a loop condition with menu prompting
    while True:
        # initialize answer
        answer = ""
        while answer == "":
            print("""\n**** Welcome to the OMDB Movie Client and DB ****
            ** Returned data will be written into the local database **
            1) Search for All Movies Containing String
            2) Search for Movies Containing String, and by Type
            99) Exit""")

            answer = input("> ") # collect an answer for testing

        # testing the answer
        if answer in ["1", "2"]:
            # All searches require a string to include in the search
            searchstring = input("Search all movies in the OMDB. Enter search string: ")

            if answer == "1":
                resp = movielookup(mykey, searchstring)
            elif answer == "2":
                print("\nSearch by type coming soon!\n") # maybe you can write this code!
                continue                                 # restart the while loop
            if resp:
                # display the results
                resp = resp.get("Search")
                print(resp)
                # write the results into the database
                trackmeplease(resp)
            else:
                print("That search did not return any results.")

        # user wants to exit
        elif answer == "99":
            print("See you next time!")
            break

if __name__ == "__main__":
    main()
Save and exit with :wq

Run your code.

student@bchd:~/mycode/apisqlite$ python3 apisqlite01.py

Try running the script a few times. Search for a few different movies.

Ensure the sqlite3 client is installed with apt

student@bchd:~/mycode/apisqlite$ sudo apt install sqlite3

Connect to the SQL database client. Information on the client can be found here: https://sqlite.org/cli.html Note: If you get stuck in this client, press CTRL + D

student@bchd:~/mycode/apisqlite$ sqlite3

Open your database file, mymovie.db

sqlite> .open mymovie.db

Get the tables within mymovie.db

sqlite> .tables

Select all of the data in the table, and display it on the screen.

sqlite> .dump

Exit the SQL database client.

sqlite> .quit

CUSTOMIZATION 01 - After reviewing the API usage on https://www.omdbapi.com/. Add an "option 2" that allows the user to limit their search by "type".

CUSTOMIZATION 02 - After reviewing the API usage on https://www.omdbapi.com/. Add an "option 3" that allows the user to limit their search by "year of release".

CUSTOMIZATION 03 - After reviewing the API usage on https://www.omdbapi.com/. Add an "option 4" that allows the user to limit their search by "type" and "year of release".

*CUSTOMIZATION SOLUTION 01 to 03 available @ https://static.alta3.com/courses/pyapi/apisqlite02.py

CODE CUSTOMIZATION 04 - Add an "option 5" that displays the contents of the LOCAL database.

CODE CUSTOMIZATION 05 - Replace the CLI User Interface with a User Interface provided by Flask. All of the same "options" should be available via HTTP GET's to your local Flask server.

If you're tracking your code in GitHub, issue the following commands:

cd ~/mycode
git add *
git commit -m "Learning to cache data locally pulled from APIs"
git push origin main

