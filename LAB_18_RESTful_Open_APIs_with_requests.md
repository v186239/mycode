RESTful Open APIs with requests
Lab Objective
The objective of this lab is to learn to work with the requests library. The request library is a abstracted way to work with HTTP / HTTPS messaging, that many prefer over the native python urllib.request library.

This library is a 3rd party library, so we'll need to use the pip module (a Python tool for installing code from pypi.org) to install it.

Using this library means that we now have several ways to query an API (that is, provided you've used urllib.request previously). So, which one should you use? The method described in this lab is the "newest cool" and is quite a bit easier than the older method using the urllib.request library. However, as a rule of thumb: if your code works in Python 3, and it does not throw a deprecation warnings, then use it!

Read about requests here:
https://requests.readthedocs.io/en/master/

In this lab, we'll use the same target as we did in a previous lab, http://api.open-notify.org/astros.json

Lab Procedure
A web service has an address (url) just like a web page does. Instead of returning HTML for a web page it returns data. Open http://api.open-notify.org/astros.json

Take a moment to study our list of JSON-ized space heroes on the International Space Station. Way to go humanity!

You'll find JSON uses some new naming, but you'll recognize the structure. It's dictionaries, key:value pairs, lists, strings, and integers. If you've been paying attention in Python class, JSON should be very clear. What is a bit tricky is that JSON looks identical to Pythonic data structures, but it isn't. It's JSON. So, we'll need to convert it.

Open a new command window.

Let's stay in the habit of organizing our work. For now, make /home/student/mycode/iss/ a directory.

student@bchd:~$ mkdir ~/mycode/iss/

Move to the /home/student/mycode/iss directory.

student@bchd:~$ cd ~/mycode/iss/

To begin, you'll need to install the requests library.

student@bchd:~/mycode/iss$ python3 -m pip install requests

Create a new script:

student@bchd:~/mycode/iss$ vim requests-ride_iss.py

Write the following script:


#!/usr/bin/python3
"""tracking the iss using
   api.open-notify.org/astros.json | Alta3 Research"""

# notice we no longer need to import urllib.request or json
import requests

## Define URL
MAJORTOM = 'http://api.open-notify.org/astros.json'

def main():
    """runtime code"""

    ## Call the webservice
    groundctrl = requests.get(MAJORTOM)
    # send a post with requests.post()
    # send a put with requests.put()
    # send a delete with requests.delete()
    # send a head with requests.head()


    ## strip the json off the 200 that was returned by our API
    ## translate the json into python lists and dictionaries
    helmetson = groundctrl.json()


    ## display our Pythonic data
    print("\n\nConverted Python data")
    print(helmetson)

    print('\n\nPeople in Space: ', helmetson['number'])
    people = helmetson['people']
    print(people)

if __name__ == "__main__":
    main()
Save and exit with :wq

Run your script.

student@bchd:~$ python3 ~/mycode/iss/requests-ride_iss.py

You should get the same output as if you used the urllib.request library, only this one took a lot fewer imports, and some less complicated lines of code!

If you're tracking your code in GitHub, issue the following commands:

cd ~/mycode
git add *
git commit -m "Learning to track ISS with requests library"
git push origin main

