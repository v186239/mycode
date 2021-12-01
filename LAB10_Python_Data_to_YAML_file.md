Python Data to YAML file
Lab Objective
The objective of this lab is to use Python to create a file on the local system as well as start learning about YAML. YAML (rhymes with “camel”) is a human-friendly cross language that is an official subset of JSON. This means we can easily translate between JSON and YAML. YAML's focus is human readability (at the cost of white spacing) whereas JSON is focused on machine-to-machine communications.

YAML's rise in popularity is partly due to the runaway success of the automation programming language Ansible. Ansible is abstracted Python programming and is structured around YAML.

Take a peek at the official YAML documentation page: https://yaml.org/spec/1.2/spec.html

Procedure
Let's stay in the habit of organizing our work. For now, make /home/student/mycode/ directory.

student@bchd:~$ mkdir ~/mycode/

Move to the /home/student/mycode/ directory.

student@bchd:~$ cd ~/mycode

Install pyyaml so we can import yaml.

student@bchd:~/mycode$ python3 -m pip install pyyaml

Create a new script.

student@bchd:~/mycode$ vim ~/mycode/makeyaml01.py

Copy and paste the following into the script. This script uses yaml.dump to create YAML strings and write them to a file.


#!/usr/bin/python3
"""Manipulate YAML | Alta3 Research"""

# YAML is NOT part of the standard library
# python3 -m pip install pyyaml
import yaml

def main():
    """runtime code"""
    ## create a blob of data to work with
    hitchhikers = [{"name": "Zaphod Beeblebrox", "species": "Betelgeusian"},
      {"name": "Arthur Dent", "species": "Human"}]

    ## display our Python data (a list containing two dictionaries)
    print(hitchhikers)

    ## open a new file in write mode
    with open("galaxyguide.yaml", "w") as zfile:

        ## use the YAML library
        ## USAGE: yaml.dump(input data, file like object)
        ## unlike JSON, the YAML lib uses .dump() to
        ## create YAML strings and write to files
        ## the JSON lib uses .dump() to create a string and .dumps() to write to files
        yaml.dump(hitchhikers, zfile)

if __name__ == "__main__":
    main()
Save and exit with :wq

Run the script you just wrote.

student@bchd:~/mycode$ python3 ~/mycode/makeyaml01.py

Ensure your script produced a YAML file. It should be located in the file where we ran the script.

student@bchd:~/mycode$ cat ~/mycode/galaxyguide.yaml

Create a second new script.

student@bchd:~/mycode$ vim ~/mycode/makeyaml02.py

In this script we explore yaml.dump() which expects a single argument, performs the YAML transformation, and returns that as a YAML string. Copy and paste the following into the script.


#!/usr/bin/python3
"""yaml.dump() expects a single argument
   performs the YAML transformation,
   and returns that as a YAML string | Alta3 Research"""

# YAML is NOT part of the standard library
# python3 -m pip install pyyaml
import yaml

def main():
    """runtime code"""
    ## create a blob of data to work with
    hitchhikers = [{"name": "Zaphod Beeblebrox", "species": "Betelgeusian"},
      {"name": "Arthur Dent", "species": "Human"}]

    ## display our Python data (a list containing two dictionaries)
    print(hitchhikers)

    ## Create the YAML string
    yamlstring = yaml.dump(hitchhikers)

    ## Display a single string of YAML
    print(yamlstring)

if __name__ == "__main__":
    main()
Save and exit with :wq

Run the script you just wrote. The Python data structures and YAML convey the same information, but are both very unique. Take a moment to study some of the differences.

student@bchd:~/mycode$ python3 ~/mycode/makeyaml02.py

In this next exercise let's try "reading-in" some YAML and converting it to Pythonic data structures. Create a new YAML document.

student@bchd:~/mycode$ vim ~/mycode/myYAML.yml

Copy and paste the following into your new YAML document.


---
- name: Alta3 Research
  hosts: all
  apps:
    - htop
    - sshd
    - iptables
...
Save and exit with :wq

Create a third script.

student@bchd:~/mycode$ vim ~/mycode/readyaml03.py

In this script we explore yaml.load() which expects a single file and converts the YAML to Pythonic data. This is going to be very useful as you try to read in and manipulate data from YAML documents. Copy and paste the following into the script.


#!/usr/bin/python3
"""yaml.load() expects a single file and
   converts the YAML to pythonic data | Alta3 Research"""

# YAML is NOT part of the standard library
# python3 -m pip install pyyaml
import yaml

def main():
    """runtime code"""
    ## Open a blob of YAML data
    with open("myYAML.yml", "r") as yf:
        ## convert YAML into Python data structures (lists and dictionaries)
        pyyammy = yaml.load(yf)
    # display our new Python data
    print(pyyammy)

if __name__ == "__main__":
    main()
Save and exit with :wq

Run the script you just wrote. The Python data structures and YAML convey the same information, but are both very unique. Take a moment to study some of the differences.

student@bchd:~/mycode$ python3 ~/mycode/readyaml03.py

Create a fourth script.

student@bchd:~/mycode$ vim ~/mycode/readyaml04.py

In this script, we will take our YAML data, translate to Python datastructures, alter it, then dump it back out as YAML.


#!/usr/bin/python3
"""Manipulating data pulled from YAML files | Alta3 Research"""

# YAML is NOT part of the standard library
# python3 -m pip install pyyaml
import yaml

def main():
    """runtime code"""
    ## Open a blob of YAML data
    with open("myYAML.yml", "r") as myf:
        ## pull in YAML as Python lists and dictionaries
        pyyammy = yaml.load(myf)
    ## how does our data currently look?
    print(pyyammy)
    ## add Minecraft to the list of apps
    pyyammy[0]['apps'].append('minecraft')
    ## Did the Python data change?
    print(pyyammy)
    ## open a file to dump out to
    with open("myYAML.yml.updated", "w") as myf:
    ## use the YAML library
    ## USAGE: yaml.dump(input data, file like object)
        yaml.dump(pyyammy, myf)

if __name__ == "__main__":
    main()
Save and exit with :wq

Run the script you just wrote. The Python data structures and YAML convey the same information but are both very unique. Take a moment to study some of the differences.

student@bchd:~/mycode$ python3 ~/mycode/readyaml04.py

Great job! That's it for this lab. If you're tracking your code in GitHub, issue the following commands:

cd ~/mycode/
git add *
git commit -m "learning about YAML"
git push origin main
Type in username & password
