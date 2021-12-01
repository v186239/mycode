RESTful Open APIs
Lab Objective
The objective of this lab is to access various RESTful APIs with Python. To start, you might be wondering, "What is a RESTful API?"

The term was first, and is still best, defined within a doctorate dissertation. If you like reading, you can read that dissertation here:

https://roy.gbiv.com/pubs/dissertation/rest_arch_style.htm

An application programming interface, or API, is a general term that simply means a mechanism by which to configure an application or system. Whereas, REST, implies a particular architecture, the more notable design notes being; a client-server relationship, one-in one-out messaging, no assumptions the server will cache responses, and the possibility of a layered system (proxies). However, there is never a mention of HTTP or HTTPs as being the protocol to use when designing RESTful APIs. HTTP and HTTPs just happen to be extraordinarily popular protocols, which make them great choices for designing highly available RESTful APIs.

We'll start to explore all of these concepts by tracking those braving the cold dark of space with an open API web service. The HTTP responses from the API contain JSON that reveals those people currently aboard the International Space Station (ISS). The data returned in this lab is very much accurate, and in real-time, from NASA data sets.

Procedure
A web service has an address (url) just like a web page does. Instead of returning HTML for a web page it returns data. Open (http://api.open-notify.org/astros.json) in a web browser.

Take a moment to study our list of JSON-ized space heroes on the International Space Station. Way to go humanity!

You'll find JSON uses some new naming but you'll recognize the structure. It's dictionaries, key:value pairs, lists, strings, and integers. If you've been paying attention in Python class, JSON should be very clear. What is a bit tricky is that JSON LOOKS identical to Pythonic data structures, but it isn't. It's JSON. So, we'll need to convert it.

Let's stay in the habit of organizing our work. For now, make /home/student/mycode/ directory.

student@bchd:~$ mkdir ~/mycode/

Move into the new directory.

student@bchd:~$ cd ~/mycode/

Open vim.

student@bchd:~/mycode$ vim ~/mycode/ride_iss.py

Cut and paste the following code into your script:


#!/usr/bin/python3
"""Alta3 Research - astros on ISS"""

import urllib.request
import json

MAJORTOM = "http://api.open-notify.org/astros.json"

def main():
    """reading json from api"""
    # call the api
    groundctrl = urllib.request.urlopen(MAJORTOM)

    # strip off the attachment (JSON) and read it
    # the problem here, is that it will read out as a string
    helmet = groundctrl.read()

    # show that at this point, our data is str
    # we want to convert this to list / dict
    print(helmet)

    helmetson = json.loads(helmet.decode("utf-8"))

    # this should say bytes
    print(type(helmet))

    # this should say dict
    print(type(helmetson))

    print(helmetson["number"])

    # this returns a LIST of the people on this ISS
    print(helmetson["people"])

    # list the FIRST astro in the list
    print(helmetson["people"][0])

    # list the SECOND astro in the list
    print(helmetson["people"][1])

    # list the LAST astro in the list
    print(helmetson["people"][-1])

    # display every item in a list
    for astro in helmetson["people"]:
        # display what astro is
        print(astro)

    # display every item in a list
    for astro in helmetson["people"]:
        # display ONLY the name value associated with astro
        print(astro["name"])

if __name__ == "__main__":
    main()
Save and exit with :wq

Run your script.

student@bchd:~/mycode$ python3 ~/mycode/ride_iss.py

CHALLENGE 01 - Tweak your script, and see if you can make it print out data in the following fashion.


People in space: 4
Eddie Kopra on the ISS
James Peake on the ISS
Yuri Kopra on the ISS
Buzz Aldrin on the ISS
Hint: Be sure to use the key 'name' and key 'craft' when you print() the above data.

SOLUTION 01 - There's a lot of solutions, one is as follows:


#!/usr/bin/python3
"""Alta3 Research - tracking ISS updated output"""

import urllib.request
import json

MAJORTOM = "http://api.open-notify.org/astros.json"

def main():
    """reading json from api"""
    # call the api
    groundctrl = urllib.request.urlopen(MAJORTOM)

    # strip off the attachment (JSON) and read it
    # the problem here, is that it will read out as a string
    helmet = groundctrl.read()

    helmetson = json.loads(helmet.decode("utf-8"))

    # display people in space
    print("People in space: " + str(helmetson["number"]))

    # display every item in a list
    for astro in helmetson["people"]:
        # display ONLY the name value associated with astro
        print(astro["name"] + " on the " + astro["craft"])

if __name__ == "__main__":
    main()
If you're tracking your code in GitHub, issue the following commands:

cd ~/mycode/
git add *
git commit -m "Pulling in data from API with python standard library"
git push origin main
Type in username & password

