# requests library - RESTful GET and JSON parsing
Lab Objective
The objective of this lab is to learn to learn to parse JSON responses. This is a critical skill that some students need additional help with. To that end, we'll use a highly available, ever-evolving, set of data from none other than the creators of Pok?mon. No need to admit if you grew up watching the show, collecting cards, or playing the video games! Also, no need to know anything about Pok?mon to appreciate this lab. At the end of the day, it is all about parsing JSON responses. It just so happens, https://pokeapi.co/ makes a very large open data-set available to us!

Procedure
Create a directory to work in.

student@bchd:~$ mkdir ~/mycode/pokemon/

Move to the /home/student/mycode/ directory.

student@bchd:~$ cd ~/mycode/

Install the requests library. It is possible this package is already installed on your system, as it is a popular one.

student@bchd:~/mycode$ python3 -m pip install requests

Create a new script we can use to play around with the API found at https://pokeapi.co/ Check it out in a bowser before creating our script.

student@bchd:~/mycode$ vim pokemon/pikachu01.py

In this first script, we'll attempt to get all the names of the Pokemon available in the index. To do this, we'll augment the API with a ?limit=1000 parameter. We knew we could do this because we read the documentation. Create the following script:


#!/usr/bin/python3

import requests

# define base URL
POKEURL = "http://pokeapi.co/api/v2/pokemon/"

def main():

    # Make HTTP GET request using requests, and decode
    # JSON attachment as pythonic data structure
    # Augment the base URL with a limit parameter to 1000 results
    pokemon = requests.get(f"{POKEURL}?limit=1000")
    pokemon = pokemon.json()

    # Loop through data, and print pokemon names
    for poke in pokemon["results"]:
        # Display the value associated with 'name'
        #print(poke["name"])
        print(poke.get("name"))

    print(f"Total number of Pokemon returned: {len(pokemon['results'])}")

if __name__ == "__main__":
    main()
Save and exit with :wq

Execute your script.

student@bchd:~/mycode$ python3 pokemon/pikachu01.py

Great! Now let's try to work with the http://pokeapi.co/api/v2/items/ api. Create the following script. Let's write one that searches for the word 'heal' within the available items, and returns all words containing that word.

student@bchd:~/mycode$ vim pokemon/pikachu02.py

Create the following script.


#!/usr/bin/python3

import requests

ITEMURL = "http://pokeapi.co/api/v2/item/"

def main():

    # Make HTTP GET request using requests
    # and decode JSON attachment as pythonic data structure
    # Also, append the URL ITEMURL with a parameter to return 1000
    # items in one response
    items = requests.get(f"{ITEMURL}?limit=1000")
    items = items.json()

    # create a list to store items with the word "heal"
    healwords = []

    # Loop through data, and print pokemon names
    # item.get("results") will return the list
    # mapped to the key "results"
    for item in items.get("results"):
        # check to see if the current item's VALUE mapped to item["name"]
        # contains the word heal
        if 'heal' in item.get("name"):
            # if TRUE, add that item to the end of list healwords
            healwords.append(item.get("name"))

    ## list all
    print(f"There are {len(healwords)} words that contain the word 'heal' in the Pokemon Item API!")
    print("List of Pokemon items containing heal: ")
    print(healwords)

if __name__ == "__main__":
    main()
Save and exit with :wq

Execute your code.

student@bchd:~/mycode$ python3 pokemon/pikachu02.py

Let's make one last upgrade to our script. This time let's write a script that allows a user to pass in a word to search on, we count the number of times that word appears, print the total word list out to the screen, and then finally export everything to MS Excel XLSX format. To do this, we'll need to use pandas. Pandas also relies on openpyxl to export to XLSX format. Let's install both now.

student@bchd:~/mycode$ python3 -m pip install pandas openpyxl

Create a new script.

student@bchd:~/mycode$ vim pokemon/pikachu03.py

Write the following:


#!/usr/bin/python3

## for accepting arguments from the cmd line
import argparse

## for making HTTP requests
## python3 -m pip install requests
import requests

## for working with data in lots of formats
## python3 -m pip install pandas
import pandas

ITEMURL = "http://pokeapi.co/api/v2/item/"

def main():

    # Make HTTP GET request using requests
    # and decode JSON attachment as pythonic data structure
    # Also, append the URL ITEMURL with a parameter to return 1000
    # items in one response
    items = requests.get(f"{ITEMURL}?limit=1000")
    items = items.json()

    # create a list to store items with the word searched on
    matchedwords = []

    # Loop through data, and print pokemon names
    # item.get("results") will return the list
    # mapped to the key "results"
    for item in items.get("results"):
        # check to see if the current item's VALUE mapped to item["name"]
        # contains the search word
        if args.searchword in item.get("name"):
            # if TRUE, add that item to the end of list matchedwords
            matchedwords.append(item.get("name"))

    finishedlist = matchedwords.copy()
    ## map our matchedword list to a dict with a title
    matchedwords = {}
    matchedwords["matched"] = finishedlist

    ## list all words containing matched word
    print(f"There are {len(finishedlist)} words that contain the word '{args.searchword}' in the Pokemon Item API!")
    print(f"List of Pokemon items containing '{args.searchword}': ")
    print(matchedwords)

    ## export to excel with pandas
    # make a dataframe from our data
    itemsdf = pandas.DataFrame(matchedwords)
    # export to MS Excel XLSX format
    # run the following to export to XLSX
    # python -m pip install openpyxl
    # index=False prevents the index from our dataframe from
    # being written into the data
    itemsdf.to_excel("pokemonitems.xlsx", index=False)

    print("Gotta catch 'em all!")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Pass in a word to search\
    the Pokemon item API")
    parser.add_argument('searchword', metavar='SEARCHW',\
    type=str, default='ball', help="Pass in any word. Default is 'ball'")
    args = parser.parse_args()
    main()
Save and exit with :wq

Execute your code. Be sure to pass a search word at the command line! Search on the word 'heal', it should return 7 matching objects.

student@bchd:~/mycode$ python3 pokemon/pikachu03.py heal

Awesome! Way to go. Try it again with 'ball', it should return 33 matching objects.

student@bchd:~/mycode$ python3 pokemon/pikachu03.py ball

CODE CUSTOMIZATION 01 - Use the PokeAPI to export a list of all Pokemon as plaintext, JSON, and Excel formats. Hint: Explore the Pandas library for help on exporting datasets!

If you're tracking your code in GitHub, issue the following commands:

cd ~/mycode
git add *
git commit -m "learning to parse JSON responses within HTTP requests"
git push origin main
Type your username and password

