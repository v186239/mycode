requests library - Open APIs
Lab Objective
The objective of this lab is to work with API Data. Oftentimes APIs will return APIs that may need explored. We also may need to limit the amount of data returned by learning to work with API parameters.

A rich open set of data is tracked by the Game Of Thrones can be found here:
https://www.anapioficeandfire.com/api

To probe the dataset, we will use the requests library. If you haven't read about it yet, read about requests here:
https://requests.readthedocs.io/en/master/

Procedure
To start, review the documentation on the APIs https://anapioficeandfire.com/Documentation

Create a directory to work in:

student@bchd:~$ mkdir ~/mycode/

Move to the /home/student/mycode/ directory.

student@bchd:~$ cd ~/mycode/

Install the requests library. It is possible this package is already installed on your system, as it is a popular one.

student@bchd:~/mycode$ python3 -m pip install requests

Create a new script we can use to display the data returned by the root API.

student@bchd:~/mycode$ vim ~/mycode/iceAndFire01.py

Create the following script:


#!/usr/bin/python3
"""Alta3 Research - Exploring OpenAPIs with requests"""
# documentation for this API is at
# https://anapioficeandfire.com/Documentation

import requests

AOIF = "https://www.anapioficeandfire.com/api"

def main():
    ## Send HTTPS GET to the API of ICE and Fire
    gotresp = requests.get(AOIF)

    ## Decode the response
    got_dj = gotresp.json()

    ## print the response
    print(got_dj)

if __name__ == "__main__":
    main()
Save and exit with :wq

Execute your script.

student@bchd:~/mycode$ python3 ~/mycode/iceAndFire01.py

Create a new script that we can use to explore the API relating to books.

student@bchd:~/mycode$ vim ~/mycode/iceAndFire02.py

Create the following script:


#!/usr/bin/python3
"""Alta3 Research - Exploring OpenAPIs with requests"""
# documentation for this API is at
# https://anapioficeandfire.com/Documentation

import pprint
import requests

AOIF_BOOKS = "https://www.anapioficeandfire.com/api/books"

def main():
    ## Send HTTPS GET to the API of ICE and Fire books resource
    gotresp = requests.get(AOIF_BOOKS)

    ## Decode the response
    got_dj = gotresp.json()

    ## print the response
    ## using pretty print so we can read it
    pprint.pprint(got_dj)

if __name__ == "__main__":
    main()
Save and exit with :wq

Execute your script.

student@bchd:~/mycode$ python3 ~/mycode/iceAndFire02.py

Create a new script that we can use to further explore the API relating to books. In this next script, we'll display the name, pages, ISBN, publisher, and number of characters found within the book.

student@bchd:~/mycode$ vim ~/mycode/iceAndFire03.py

Create the following script:


#!/usr/bin/python3
"""Alta3 Research - Exploring OpenAPIs with requests"""
# documentation for this API is at
# https://anapioficeandfire.com/Documentation

import requests

AOIF_BOOKS = "https://www.anapioficeandfire.com/api/books"

def main():
    ## Send HTTPS GET to the API of ICE and Fire books resource
    gotresp = requests.get(AOIF_BOOKS)

    ## Decode the response
    got_dj = gotresp.json()

    ## loop across response
    for singlebook in got_dj:
        ## display the names of each book
        ## all of the below statements do the same thing
        #print(singlebook["name"] + ",", "pages -", singlebook["numberOfPages"])
        #print("{}, pages - {}".format(singlebook["name"], singlebook["numberOfPages"]))
        print(f"{singlebook['name']}, pages - {singlebook['numberOfPages']}")
        print(f"\tAPI URL -> {singlebook['url']}\n")
        # print ISBN
        print(f"\tISBN -> {singlebook['isbn']}\n")
        print(f"\tPUBLISHER -> {singlebook['publisher']}\n")
        print(f"\tNo. of CHARACTERS -> {len(singlebook['characters'])}\n")

if __name__ == "__main__":
    main()
Save and exit with :wq

Execute your script.

student@bchd:~/mycode$ python3 ~/mycode/iceAndFire03.py

Now let's create a script that accepts input from the user and searches for a particular character. The API notes that we can send a parameter for each character's numeric entry.

student@bchd:~/mycode$ vim ~/mycode/iceAndFire04.py

Create the following script.


#!/usr/bin/python3
"""Alta3 Research - Exploring OpenAPIs with requests"""
# documentation for this API is at
# https://anapioficeandfire.com/Documentation

import requests
import pprint

AOIF_CHAR = "https://www.anapioficeandfire.com/api/characters/"

def main():
        ## Ask user for input
        got_charToLookup = input("Pick a number between 1 and 1000 to return info on a GoT character! " )

        ## Send HTTPS GET to the API of ICE and Fire character resource
        gotresp = requests.get(AOIF_CHAR + got_charToLookup)

        ## Decode the response
        got_dj = gotresp.json()
        pprint.pprint(got_dj)

if __name__ == "__main__":
        main()
Save and exit with :wq

Run your script.

student@bchd:~/mycode$ python3 ~/mycode/iceAndFire04.py

CODE CUSTOMIZATION 01 - Return the house(s) affiliated with the character looked up, along with a list of books they appear in.

If you're tracking your code in GitHub, issue the following commands:

cd ~/mycode
git add *
git commit -m "Exploring how to work with large data sets"
git push origin main
Type your username and password

