RESTful APIs and Dev Keys
Lab Objective
The objective of this lab is to explore a vast data set as provided by the Marvel API. Marvel requires a developer's account to access their data but creating an account only requires a valid email address.

This lab suggests one of many applications that is possible given the 70 years of Marvel history. After building the Python application described in this lab you're welcome to be creative and build your own application using the Marvel API.

Remember, all API keys are a source of great power. If exchanged over HTTPS, you can be fairly certain that your credentials are not being exposed. If exchanged over HTTP, then you better be certain no sensitive data is being transmitted. In this lab, we'll learn how to hide our data in a secure fashion.

Just remember what Gandalf said to... Spiderman concerning API keys- ‘Keep it secret, and keep it safe!'

Before you get started, read about what you're getting into: https://developer.marvel.com/

Procedure
Clean up your desktop screen.

Make your Marvel dev account. Head on over to https://developer.marvel.com/

Click your way through the creation process.

Enter your birthday CLICK
Enter your personal info (probably uncheck 'I want Marvel fan mail') CLICK
Scroll to the bottom and check "Agree" CLICK
To enable your API keys you receive, click the link in the confirmation email you receive. OPEN EMAIL -> CLICK
You get both a public and private key. Copy these both to a safe location. All calls to the Marvel Comics API must pass your public key via an apikey parameter. Please keep your private key private! Do not store your private key in publicly available code or repositories that are accessible to the public. Do not accidentally leave it at the bar.

The TLDR on this is as follows: server-side applications must pass two parameters in addition to the apikey parameter:

ts - a timestamp (or other long string which can change on a request-by-request basis)
hash - a md5 digest of the ts parameter, your private key and your public key (e.g. md5(ts+privateKey+publicKey)
For example, a user with a public key of "1234" and a private key of "abcd" could construct a valid call as follows: http://gateway.marvel.com/v1/public/comics?ts=1&apikey=1234&hash=ffd275c5130566a2916217b101f26150

The hash value is the md5 digest of 1abcd1234
The value ts is unique each time, which means we'll need to calculate a unique hash each time. We don't want to risk saving our private API key to the cloud but we do need it available to our script. Let's place it in a file in our home directory (which is encrypted).

student@bchd:~$ vim marvel.priv

Copy and paste your private key from the Marvel website into this file.

Save and exit with :wq

Let's just put our public key in a file located in the home folder as well. That way if someone else wants to use our code they don't need to edit the code, just substitute in their own keyfiles.

student@bchd:~$ vim marvel.pub

Copy and paste your public key from the Marvel website into this file.

Save and exit with :wq

Create a directory to work in.

student@bchd:~$ mkdir mycode/xmen

Move into the new directory:

student@bchd:~$ cd mycode/xmen/

Ensure you have the requests library installed. This is a third party library and is a replacement for urllib.request.

student@bchd:~/mycode/xmen$ python3 -m pip install requests

It seems bad practice as well as insecure and inflexible to hard code where our private API key is stored on our system, so let's pass this as an argument. We can do this with argparse. The argparse library has been available in the standard library since Python 3.2 and replaces sys as a more comprehensive way to collect command line arguments. Maybe one day the requests library will become part of the standard library as well.

Create a new script.

student@bchd:~/mycode/xmen$ vim marvel_api_01.py

Copy and paste the following into your script.


#!/usr/bin/env python3
"""Marvel Python Client
RZFeeser@alta3.com | Alta3 Research"""

# standard library imports
import argparse   # pull in arguments from CLI
import time       # create time stamps (for our RAND)
import hashlib    # create our md5 hash to pass to dev.marvel.com
from pprint import pprint # we only want pprint() from the package pprint

# 3rd party imports
import requests   # python3 -m pip install requests

## Define the API here
API = 'http://gateway.marvel.com/v1/public/characters'

## Calculate a hash to pass through to our MARVEL API call
## Marvel API wants md5 calc md5(ts+privateKey+publicKey)
def hashbuilder(rand, privkey, pubkey):
    return hashlib.md5((f"{rand}{privkey}{pubkey}").encode('utf-8')).hexdigest()  # create an MD5 hash of our identifers

## Perform a call to MARVEL Character API
## http://gateway.marvel.com/v1/public/characters
## ?name=Spider-Man&ts=1&apikey=1234&hash=ffd275c5130566a2916217b101f26150
def marvelcharcall(rand, keyhash, pubkey, lookmeup):
    r = requests.get(f"{API}?name={lookmeup}&ts={rand}&apikey={pubkey}&hash={keyhash}")  # send an HTTP GET to this location

    # the marvel APIs are "flakey" at best, so check for a 200 response
    if r.status_code != 200:
        response = None     #
    else:
        response = r.json()

    # return the HTTP response with the JSON removed
    return response


def main():

    ## harvest private key
    with open(args.dev) as pkey:
        privkey = pkey.read().rstrip('\n')

    ## harvest public key
    with open(args.pub) as pkey:
        pubkey = pkey.read().rstrip('\n')

    ## create an integer from a float timestamp (for our RAND)
    rand = str(time.time()).rstrip('.')

    ## build hash with hashbuilder(timestamp, privatekey, publickey)
    keyhash = hashbuilder(rand, privkey, pubkey)

    ## call the API with marvelcharcall(timestamp, hash, publickey, character)
    result = marvelcharcall(rand, keyhash, pubkey, "Wolverine")  # search for Wolverine

    ## display results
    pprint(result)

## Define arguments to collect
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    # This allows us to pass in public and private keys
    parser.add_argument('--dev', help='Provide the /path/to/file.priv containing Marvel private developer key')
    parser.add_argument('--pub', help='Provide the /path/to/file.pub containing Marvel public developer key')

    args = parser.parse_args()
    main()
Save and exit with :wq

Run your script.

student@bchd:~/mycode/xmen$ python3 marvel_api_01.py --dev /home/student/marvel.priv --pub /home/student/marvel.pub

You should get results about the character Wolverine (Logan). Our function call to marvelcharcall is hard-coded to look up this character.

Let's write a new script that allows us to look up any character we wish.

student@bchd:~/mycode/xmen$ vim marvel_api_02.py

Copy and paste the following into your script:


#!/usr/bin/env python3
"""Marvel Python Client
RZFeeser@alta3.com | Alta3 Research"""

# standard library imports
import argparse   # pull in arguments from CLI
import time       # create time stamps (for our RAND)
import hashlib    # create our md5 hash to pass to dev.marvel.com
from pprint import pprint # we only want pprint() from the package pprint

# 3rd party imports
import requests   # python3 -m pip install requests

## Define the API here
API = 'http://gateway.marvel.com/v1/public/characters'

## Calculate a hash to pass through to our MARVEL API call
## Marvel API wants md5 calc md5(ts+privateKey+publicKey)
def hashbuilder(rand, privkey, pubkey):
    return hashlib.md5((f"{rand}{privkey}{pubkey}").encode('utf-8')).hexdigest()  # create an MD5 hash of our identifers

## Perform a call to MARVEL Character API
## http://gateway.marvel.com/v1/public/characters
## ?name=Spider-Man&ts=1&apikey=1234&hash=ffd275c5130566a2916217b101f26150
def marvelcharcall(rand, keyhash, pubkey, lookmeup):
    r = requests.get(f"{API}?name={lookmeup}&ts={rand}&apikey={pubkey}&hash={keyhash}")  # send an HTTP GET to this location

    # the marvel APIs are "flakey" at best, so check for a 200 response
    if r.status_code != 200:
        response = None     #
    else:
        response = r.json()

    # return the HTTP response with the JSON removed
    return response


def main():

    ## harvest private key
    with open(args.dev) as pkey:
        privkey = pkey.read().rstrip('\n')

    ## harvest public key
    with open(args.pub) as pkey:
        pubkey = pkey.read().rstrip('\n')

    ## create an integer from a float timestamp (for our RAND)
    rand = str(time.time()).rstrip('.')

    ## build hash with hashbuilder(timestamp, privatekey, publickey)
    keyhash = hashbuilder(rand, privkey, pubkey)

    ## call the API with marvelcharcall(timestamp, hash, publickey, character)
    result = marvelcharcall(rand, keyhash, pubkey, args.hero)

    ## display results
    pprint(result)

## Define arguments to collect
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    # This allows us to pass in public and private keys
    parser.add_argument('--dev', help='Provide the /path/to/file.priv containing Marvel private developer key')
    parser.add_argument('--pub', help='Provide the /path/to/file.pub containing Marvel public developer key')

    ## This allows us to pass the lookup character
    parser.add_argument('--hero', help='Character to search for within the Marvel universe')
    args = parser.parse_args()
    main()
Save and exit with :wq

Run your script.

student@bchd:~/mycode/xmen$ python3 marvel_api_02.py --dev /home/student/marvel.priv --pub /home/student/marvel.pub --hero Spider-Man

Try issuing a few more calls. Each time, change the hero you search for. If you're not a Marvel fan, try out --hero Iceman, --hero Venom, or --hero Archangel. Also try out some false tests, --hero Bicycle-Repairman and --hero Kalegirl should fail.

Use your own mechanism to make the response more readable. This will likely mean limiting the amount of data that is actually displayed to the user (this is common practice).

CODE CUSTOMIZATION 01 - Use the Marvel Developer's page to research additional parameters that might be defined along with your API lookup to the Marvel character database.

CODE CUSTOMIZATION 02 - Create a mechanism to dig deeper into the returned data. If links are available, give the user options to automatically open them within the browser.

Great job! That's it for this lab. If you make something worth sharing, be sure to let the instructor know.

If you're tracking in GitHub, and you'd like to backup your code, run the following commands:

cd ~/mycode
git add *
git commit -m "All about Xaviers School for Gifted Youngsters"
git push origin main

