# APIs and Dev Keys
Lab Objective
The objective of this lab is to create a Python client that can query APIs across a WAN. As a Python programmer, you'll be expected to work with APIs, which means understanding protocols like HTTP(S) and data structures like JSON. It doesn't matter if you're on the server or network side of automation, APIs are everywhere.

In addition to giving us things like Velcro and camera phones, NASA also will give us a massive amount of amazing data via RESTful APIs. In this lab and others we'll use NASA's free data to improve our skills writing Python programs and starting to make API calls across networks.

This lab is broken into two parts:

PART I - RESTful API calls to the NASAs Picture of the Day(APOD) API.

PART II - RESTful API calls to the Near Earth Object Web Service API.

Procedure
PART I: RESTful API Request to the NASA APOD

Open a new browser tab and visit NASA's Open API Data Set https://api.nasa.gov/

Apply for a API developer's key on NASA's website. It's free, and will entitle you to 1000 API requests per hour. The site to apply for a dev key is here: https://api.nasa.gov/

You'll need to supply your name and email address. Your dev key and account information will be emailed to you but you should record the key now. You'll need it when you make request to various NASA APIs. If you're a bit lost, see the screenshot below. You should be seeing something like it by the time you're at this step.

NASA API developer key

Now that you're armed with a NASA dev key, let's check out one of their most popular projects, NASA's Picture of the Day (APOD).

To explore this API. Let's start in the terminal. Type python3

student@bchd:~$ python3

First import the standard library for working with HTTP.

>>> import urllib.request

Define the NASA url.

>>> nasaurl = "https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY"

Now make a request using the NASA provided DEMO_KEY. We don't want to over use this option, and the number of requests per day is highly limited. But it should work for now.

>>> apodurlobj = urllib.request.urlopen(nasaurl)

Discover the names in the response object. Ignore anything with double-underscores around it. The other names are attributes or methods.

>>> dir(apodurlobj)

Show the response code attribute that is contained within our object.

>>> apodurlobj.code

Show the response HTTP message attribute that is contained within our object.

>>> apodurlobj.msg

Show the length (octets) contained within the response HTTP message.

>>> apodurlobj.length

Try displaying the attached json().

>>> apod = apodurlobj.read().decode("utf-8")

Some people use pretty print to make json more readable. Try that out. First import pprint

>>> import pprint

Try to pretty print the data structure.

>>> pprint.pprint(apod)

Okay, enough exploration. Try exiting.

>>> exit()

In a terminal, put your NASA API key in a location that will not get committed to GitHub. Your home directory is a good spot.

student@bchd:~$ vim ~/nasa.creds

Put your API key in this file. Don't put an 'extra' line feed.

Save and exit with :wq

Make a directory to work in.

student@bchd:~$ mkdir -p ~/mycode/nasa/

Move into the new directory.

student@bchd:~$ cd ~/mycode/nasa/

Use vim to write a script:

student@bchd:~/mycode/nasa$ vim apod.py

Create the following script. We can improve the design of this script later. First, let's just get something that works. The solution below uses the urllib.request and json libraries from the Python standard library.


#!/usr/bin/python3
import urllib.request
import json

## uncomment this import if you run in a GUI
## and want to open the URL in a browser
## import webbrowser

NASAAPI = "https://api.nasa.gov/planetary/apod?"

def main():
    ## Define creds
    with open("/home/student/nasa.creds") as mycreds:
        nasacreds = mycreds.read()

    ## remove any "extra" new line feeds on our key
    nasacreds = "api_key=" + nasacreds.strip("\n")

    ## Call the webservice with our key
    apodurlobj = urllib.request.urlopen(NASAAPI + nasacreds)

    ## read the file-like object
    apodread = apodurlobj.read()

    ## decode JSON to Python data structure
    apod = json.loads(apodread.decode("utf-8"))

    ## display our Pythonic data
    print("\n\nConverted Python data")
    print(apod)

    print()

    print(apod["title"] + "\n")

    print(apod["date"] + "\n")

    print(apod["explanation"] + "\n")

    print(apod["url"])

    ## Uncomment the code below if running in a GUI
    ## and you want to open the URL in a browser
    ## use Firefox to open the HTTPS URL
    ## input("\nPress Enter to open NASA Picture of the Day in Firefox")
    ## webbrowser.open(decodeapod["url"])
if __name__ == "__main__":
    main()
Save and exit with :wq

student@bchd:~/mycode/nasa$ python3 apod.py

Run your code. It should work, but we can do better by using the requests library.

student@bchd:~/mycode/nasa$ python3 -m pip install requests

Create a new script, apod02.py

student@bchd:~/mycode/nasa$ vim apod02.py

Create the following. In addition to the requests library, we'll also break our code to include an additional function, returncreds(). The function opens our nasa.creds file. One benefit of isolating code within functions, is that is more easily identifiable, reused, and debugged.


#!/usr/bin/python3

import requests

NASAAPI = "https://api.nasa.gov/planetary/apod?"

# this function grabs our credentials
def returncreds():
    ## first I want to grab my credentials
    with open("/home/student/nasa.creds", "r") as mycreds:
        nasacreds = mycreds.read()
    ## remove any newline characters from the api_key
    nasacreds = "api_key=" + nasacreds.strip("\n")
    return nasacreds

# this is our main function
def main():
    ## first grab credentials
    nasacreds = returncreds()

    ## make a call to NASAAPI with our key
    apodresp = requests.get(NASAAPI + nasacreds)

    ## strip off json
    apod = apodresp.json()

    print(apod)

    print()

    print(apod["title"] + "\n")

    print(apod["date"] + "\n")

    print(apod["explanation"])

    print(apod["url"])

if __name__ == "__main__":
    main()
Save and exit with :wq

student@bchd:~/mycode/nasa$ python3 apod02.py

PART II: RESTful API Request to the NASA NEOWS

In the second part of this lab, the data set we'll work is the Near Earth Object Web Service. With NeoWs a user can search for Asteroids based on their closest approach date to Earth, look up a specific asteroid with its NASA JPL small body id, and browse the overall data-set.

EXAMPLE: Retrieve a list of Asteroids based on their closest approach date to Earth.

GET https://api.nasa.gov/neo/rest/v1/feed?start_date=START_DATE&end_date=END_DATE&api_key=API_KEY

Open a new browser tab. You don't need to do this step within the remote desktop. If you haven't already, check out NASA's second most popular project, NASA Near Earth Object Web Service: https://api.nasa.gov/api.html#NeoWS

This part of the lab will also require your NASA developer key.

Open a new script with vim (keep working in the same directory as PART I).

student@bchd:~/mycode/nasa$ vim neows.py

Copy the following codeblock into your new script:


#!/usr/bin/python3
import requests

## Define NEOW URL
NEOURL = "https://api.nasa.gov/neo/rest/v1/feed?"

# this function grabs our credentials
# it is easily recycled from our previous script
def returncreds():
    ## first I want to grab my credentials
    with open("/home/student/nasa.creds", "r") as mycreds:
        nasacreds = mycreds.read()
    ## remove any newline characters from the api_key
    nasacreds = "api_key=" + nasacreds.strip("\n")
    return nasacreds

# this is our main function
def main():
    ## first grab credentials
    nasacreds = returncreds()

    ## update the date below, if you like
    startdate = "start_date=2019-11-11"

    ## the value below is not being used in this
    ## version of the script
    # enddate = "end_date=END_DATE"

    # make a request with the request library
    neowrequest = requests.get(NEOURL + startdate + "&" + nasacreds)

    # strip off json attachment from our response
    neodata = neowrequest.json()

    ## display NASAs NEOW data
    print(neodata)

if __name__ == "__main__":
    main()
Save and exit with :wq

Change your permission.

student@bchd:~/mycode/nasa$ chmod u+x neows.py

Run your code (the method below depends on having a shebang set as the first line of your code).

student@bchd:~/mycode/nasa$ ./neows.py

CODE CUSTOMIZATION 01 - Looking for a bit of a challenge? Make the program accept a start date from a user, and an (optional) end parameter.

CODE CUSTOMIZATION 02 - Try reading your API key in with the https://pypi.org/project/python-dotenv/ project. This makes it easy to interact with environmental variables from your local shell.

CODE CUSTOMIZATION 03 - Find an additional NASA API listed on https://api.nasa.gov/ and write Python code to interact with it.

If you followed the labs, your NASA API key should NOT be anywhere in your current code. Remember, we saved it in a file ~/nasa.creds, which is not being tracked by git. If the API key was coded into your solution, you should remove it before performing the following git operations.

If you're tracking your code in GitHub, issue the following commands:

cd ~/mycode/
git add *
git commit -m "Working with NASA APIs"
git push origin main
Type your username and password

