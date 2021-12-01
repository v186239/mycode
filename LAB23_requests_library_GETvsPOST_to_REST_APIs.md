requests library - GET vs POST to REST APIs
Lab Objective
The objective of this lab is to learn to learn the difference between a GET and POST request, and how they might be expected to interact different with APIs. The default HTTP behavior of browsers (and most HTTP applications) is to send a GET. GETs require any information being 'passed' to the API to be done so within the URL. This is done via key=value pairs found after a ? and delimited by & for example:
www.example.com/search?subject=apis&date=recent

This lab depends on the open APIs found at https://jsontest.com The site makes several APIs available, all of which return JSON. One API will be of particular interest to us, https://validate.jsontest.com which allows for the validation of JSON via a GET or POST. For now, just read over the documentation.

Procedure
Create a directory to work in.

student@bchd:~$ mkdir ~/mycode/jsontest/

Move to the /home/student/mycode/ directory.

student@bchd:~$ cd ~/mycode/

Install the requests library. It is possible this package is already installed on your system, as it is a popular one.

student@bchd:~/mycode$ python3 -m pip install requests

Create a new script we can use to play around with the IP API found at https://ip.jsontest.com This API returns JSON attached to an HTTP 200 response code revealing the sender's IP address.

student@bchd:~/mycode$ vim jsontest/jsontestIP.py

Create the following script:


#!/usr/bin/python3

import requests

# define the URL we want to use
IPURL = "http://ip.jsontest.com/"

def main():
    # use requests library to send an HTTP GET
    resp = requests.get(IPURL)

    # strip off JSON response
    # and convert to PYTHONIC LIST / DICT
    respjson = resp.json()

    # display our PYTHONIC data (LIST / DICT)
    print(respjson)

    # JUST display the value of "ip"
    print(f"The current WAN IP is --> {respjson['ip']}")

if __name__ == "__main__":
    main()
Save and exit with :wq

Execute your script.

student@bchd:~/mycode$ python3 jsontest/jsontestIP.py

The IP address should be displayed. Cool! Let's now try to validate some JSON.

student@bchd:~/mycode$ vim jsontest/jsontestValidateGET.py

This API works one of two ways. The first (which we'll explore now) is with a GET. This is not recommended, as you must pass all of your JSON in via a URL! This could be very big, very fast. However, it does work. So, write the following script.


#!/usr/bin/python3

import requests
import json

# define the URL we want to use
GETURL = "http://validate.jsontest.com/"

def main():
    # test data to validate as legal json
    mydata = {"fruit": ["apple", "pear"], "vegetable": ["carrot"]}

    ## the next two lines do the same thing
    ## we take python, convert to a string, then strip out whitespace
    #jsonToValidate = "json=" + str(mydata).replace(" ", "")
    #jsonToValidate = f"json={ str(mydata).replace(' ', '') }"
    ## slightly different thinking
    ## user json library to convert to legal json, then strip out whitespace
    jsonToValidate = f"json={ json.dumps(mydata).replace(' ', '') }"

    # use requests library to send an HTTP GET
    resp = requests.get(f"{GETURL}?{jsonToValidate}")

    # strip off JSON response
    # and convert to PYTHONIC LIST / DICT
    respjson = resp.json()

    # display our PYTHONIC data (LIST / DICT)
    print(respjson)

    # JUST display the value of "validate"
    print(f"Is your JSON valid? {respjson['validate']}")

if __name__ == "__main__":
    main()
Save and exit with :wq

Run your code.

student@bchd:~/mycode$ python3 jsontest/jsontestValidateGET.py

This should produce valid JSON. Which is cool, but let's try that with a POST. Unlike a GET, a POST allows for the attachment of a 'form', which can contain key=value pairs. The attachment can be of nearly any size, which makes it a bit more desirable than a GET. Additionally, we do not have white space concerns as we did when we jammed our JSON into a URL.

student@bchd:~/mycode$ vim jsontest/jsontestValidatePOST.py

Create the following script to validate with a POST. The trickiest thing about this exercise is that the documentation does a poor job explaining that the proper formatting for your form data is {"json" : "the json to validate"}.


#!/usr/bin/python3

import requests

# define the URL we want to use
POSTURL = "http://validate.jsontest.com/"

def main():
    # test data to validate as legal json
    # when a POST json= is replaced by the KEY "json"
    # the key "json" is mapped to a VALUE of the json to test
    # because the test item is a string, we can include whitespaces
    mydata = {"json": "{'fruit': ['apple', 'pear'], 'vegetable': ['carrot']}" }

    # use requests library to send an HTTP POST
    resp = requests.post(POSTURL, data=mydata)

    # strip off JSON response
    # and convert to PYTHONIC LIST / DICT
    respjson = resp.json()

    # display our PYTHONIC data (LIST / DICT)
    print(respjson)

    # JUST display the value of "validate"
    print(f"Is your JSON valid? {respjson['validate']}")

if __name__ == "__main__":
    main()
Save and exit with :wq

Run you code.

student@bchd:~/mycode$ python3 jsontest/jsontestValidatePOST.py

Okay. Now a bit of a challenge. Write a single script that utilizes the APIs on https://jsontest.com to perform the following:

PART A Pull timestamp of now (format is up to you)
PART B Pull the IP address of your current system
PART C Read in a list of servers from a file called, myservers.txt (you'll need to make this)
PART D format the data in the following manner: {"json": "time: <<PART A>>, ip: <<PARTB>>, mysvrs: [ <<PARTC>> ]"}
PART E Validate your JSON with a POST
The solution to the challenge above is below.

Create your hosts file, myservers.txt

student@bchd:~/mycode$ vim jsontest/myservers.txt

Enter the following into the file


 host1
 host2
 host3
Save and exit with :wq

Create the solution script.

student@bchd:~/mycode$ vim jsontest/jsontestValidatePOST02.py

The following is one possible solution.


#!/usr/bin/python3

import requests

# define the URL we want to use
TIMEURL = "http://date.jsontest.com"
IPURL = "http://ip.jsontest.com"
VALIDURL = "http://validate.jsontest.com/"

def main():
    ## PART A
    ## pull a time object from date.jsontest.com
    # make the request
    resp = requests.get(TIMEURL)
    # pull json off 200 response
    # and change to PYTHONIC data
    mytime = resp.json()
    # pull out the value associated with the KEY "time"
    # then strip out all whitespaces
    # replace colons with hyphens
    mytime = mytime["time"].replace(" ", "").replace(":", "-")

    ## PART B
    ## make the request
    resp = requests.get(IPURL)
    myip = resp.json()
    print(myip)
    ## grab the value associated with the KEY "ip"
    myip = myip["ip"]

    ## PART C
    ## read a list of hosts out of a flat file
    with open("/home/student/mycode/jsontest/myservers.txt") as myfile:
        mysvrs = myfile.readlines()

    ## PART D
    # test data to validate as legal json
    # when a POST json= is replaced by the KEY "json"
    # the key "json" is mapped to a VALUE of the json to test
    # because the test item is a string, we can include whitespaces
    # format for requests to validate.testjson.com is...
    # data={"json": "json you want to validate as str"}
    jsonToTest = {}
    jsonToTest["time"] = mytime
    jsonToTest["ip"] = myip
    jsonToTest["mysvrs"] = mysvrs

    mydata = {}
    mydata["json"] = str(jsonToTest)

    ## PART E
    # use requests library to send an HTTP POST
    resp = requests.post(VALIDURL, data=mydata)

    # strip off JSON response
    # and convert to PYTHONIC LIST / DICT
    respjson = resp.json()

    # display our PYTHONIC data (LIST / DICT)
    print(respjson)

    # JUST display the value of "validate"
    print(f"Is your JSON valid? {respjson['validate']}")

if __name__ == "__main__":
    main()
Save and exit with :wq

Run your solution.

student@bchd:~/mycode$ python3 jsontest/jsontestValidatePOST02.py

If you're tracking your code in GitHub, issue the following commands:

cd ~/mycode
git add *
git commit -m "GET vs POST"
git push origin main
Type your username and password
