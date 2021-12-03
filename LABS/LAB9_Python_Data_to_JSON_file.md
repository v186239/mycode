# Python Data to JSON file
Lab Objective
The objective of this lab is to use Python to create a file on the local system as well as start learning about JSON. Not so surprisingly, JavaScript Object Notation was inspired by a subset of the JavaScript programming language. JSON has long since become language agnostic and exists as its own standard by the IETF in RFC 8259 (https://tools.ietf.org/html/rfc8259)

People chiefly liked JSON because it was REALLY easy for machines to create and parse, it had minimal size requirements as compared to XML, and was pretty okay for humans to create and parse. JSON's inability to be REALLY easy for humans is what led to the creation of YAML, but we can focus on that later. For now, we'll write a script that leverages Python's native support for JSON via its standard library and push some data out to the screen.

Review the following Python to JSON term translation table. When we use Python to output our data to JSON these are the conversions that will take place.

Python	JSON
dict	object
list, tuple	array
str	string
int, long, float	number
True	true
False	false
None	null
Procedure
Let's stay in the habit of organizing our work. For now, make /home/student/mycode/ directory.

student@bchd:~$ mkdir ~/mycode/

Move into the new folder.

student@bchd:~$ cd ~/mycode/

Create a new script.

student@bchd:~/mycode$ vim ~/mycode/makejson01.py

Copy and paste the following into the script.


#!/usr/bin/python3
"""Reviewing how to parse json | Alta3 Research"""

# JSON is part of the Python Standard Library
import json

def main():
    """runtime code"""
    ## create a blob of data to work with
    hitchhikers = [{"name": "Zaphod Beeblebrox", "species": "Betelgeusian"},
      {"name": "Arthur Dent", "species": "Human"}]

    ## display our Python data (a list containing two dictionaries)
    print(hitchhikers)

    ## open a new file in write mode
    with open("galaxyguide.json", "w") as zfile:
        ## use the JSON library
        ## USAGE: json.dump(input data, file like object) ##
        json.dump(hitchhikers, zfile)

if __name__ == "__main__":
    main()
Save and exit with :wq

Run the script you just wrote.

student@bchd:~/mycode$ python3 ~/mycode/makejson01.py

Ensure your script produced a JSON file. It should be located in the file where we ran the script.

student@bchd:~/mycode$ cat ~/mycode/galaxyguide.json

Create a second new script.

student@bchd:~/mycode$ vim makejson02.py

In this script we explore json.dumps() which expects a single argument (a list or dictionary), performs the JSON transformation, and returns that as a JSON string. Copy and paste the following into the script.


#!/usr/bin/python3
"""The json.dumps() function creates a JSON string | Alta3 Research"""

# JSON is part of the Python Standard Library
import json

def main():
    """runtime code"""
    ## create a blob of data to work with
    hitchhikers = [{"name": "Zaphod Beeblebrox", "species": "Betelgeusian"},
      {"name": "Arthur Dent", "species": "Human"}]

    ## display our Python data (a list containing two dictionaries)
    print(hitchhikers)

    ## Create the JSON string
    jsonstring = json.dumps(hitchhikers)

    ## Display a single string of JSON
    print(jsonstring)

if __name__ == "__main__":
    main()
Save and exit with :wq

Run the script you just wrote. Python and JSON are very much alike, but take a moment to study some of the differences.

student@bchd:~/mycode$ python3 ~/mycode/makejson02.py

Cool! Let's create a block of JSON that represents a data center layout. Create a new script.

student@bchd:~/mycode$ vim ~/mycode/datacenter.json

Copy and paste the following into your script:


{
    "row1": ["svralpha", "svrbeta", "svrgamma", "svrdelta"],
    "row2": ["svr-avengers", "svr-justlge"],
    "row3": ["svr1", "svr2b", "svr3c", "svr4d"]
}
Save and exit with :wq

Create a new script that can parse out our new JSON file.

student@bchd:~/mycode$ vim ~/mycode/makejson03.py

Copy and paste the following into the new script.


#!/usr/bin/python3
"""opening a static file containing JSON data | Alta3 Research"""

# JSON is part of the Python Standard Library
import json

def main():
    """runtime code"""
    ## open the file
    with open("datacenter.json", "r") as datacenter:
        datacenterstring = datacenter.read()

    ## display our decoded string
    print(datacenterstring)
    print(type(datacenterstring))           
    print("\nThe code above is string data. Python cannot easily work with this data.")
    input("Press Enter to continue\n")            

    ## Create the JSON string
    datacenterdecoded = json.loads(datacenterstring)

    ## This is now a dictionary
    print(type(datacenterdecoded))

    ## display the servers in the datacenter
    print(datacenterdecoded)

    ## display the servers in row3
    print(datacenterdecoded["row3"])

    ## display the 2nd server in row2
    print(datacenterdecoded["row2"][1])

    ## write code to
    ## display the last server in row3

if __name__ == "__main__":
    main()
Save and exit with :wq

Run your script!

student@bchd:~/mycode/$ python3 ~/mycode/makejson03.py

The script should display your data. The dictionary allows us to shout out a name of a row within the datacenter and get back a list of servers as a list. Because lists have order we can determine which how the servers are arranged within a row. Try editing the code to return the last server in the 3rd row (this is svr4d).

If you're tracking your code in GitHub, issue the following commands:

cd ~/mycode/
git add *
git commit -m "reviewing how to manipulate JSON data with python"
git push origin main
Type in username & password
