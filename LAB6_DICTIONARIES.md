# Dictionaries
Lab Objective
The objective of this lab is to play around with dictionaries, dictionary methods, and built in functions. Dictionaries are created with key:value pair relationships. Keys always recall values, but values will not recall keys. Dictionaries are unordered, which means if we place a key:value pair at index (position) '7' in the dictionary there is no guarantee it will remain at index (position) '7'. Dictionaries are also mutable, which means they can be altered (re-ordered, remove key:value pairs, add key:value pairs, etc.)

Strengthening our skills with Python dictionaries will help us understand and work with JSON (and YAML).

Procedure
Let's stay in the habit of organizing our work. For now, make /home/student/mycode/ directory.

student@bchd:~$ mkdir ~/mycode/

Move to the /home/student/mycode/ directory.

student@bchd:~$ cd ~/mycode/

Create a new script named dictrev01.py.

student@bchd:~$ vim ~/mycode/dictrev01.py

Copy and paste the following into the script.


#!/usr/bin/python3
"""Learning about Dictionaries | Alta3 Research"""

def main():
    """runtime code"""
    hostipdict = {'host01':'10.0.2.3', 'host02':'192.168.3.3', 'host03':'72.4.23.22'}

    ## Display the current state of our dictionary
    print(hostipdict)

    ## add another entry to the dict
    hostipdict['host04'] = '10.23.43.224'

    ## display the dict with the new entry for host4
    print(hostipdict)

    ## rewrite the value for host02
    hostipdict['host02'] = '192.168.70.55'

    ## display the dict with the new entry applied
    print(hostipdict)

    ## recall from the dict
    ## 'host02' should now point to '192.168.70.55'
    print(hostipdict['host02'])

    ## This will cause a key error
    ## toast01 is not a key
    ##print(hostipdict['toast01'])

if __name__ == "__main__":
    main()
Save and exit with :wq

Run the script you just wrote.

student@bchd:~$ python3 ~/mycode/dictrev01.py

Edit ~/mycode/dictrev01.py and uncomment the last line of code. Run the script again and the script should fail with a key error. That is because the key toast01 does not exist.

Create a second new script. In this one we'll try using a dictionary method called .get() to recall our data. This method expects to be given the key you are looking for. If it does not exist, it will not error out.

student@bchd:~$ vim ~/mycode/dictrev02.py

Copy and paste the following into the script.


#!/usr/bin/python3
"""Reviewing how to work with dictionaries | Alta3 Research"""

def main():
    firewalldict = {'sip':'5060', 'ssh':'22', 'http':'80'}

    ## display the current state of our dictionary
    print(firewalldict)

    ## add another entry to the dict
    ## notice that https maps to an INT, not a STRING
    firewalldict['https'] = 443

    ## display the dict with the new entry for host4
    print(firewalldict)

    ## display some dictionary data
    print('The print statement can be passed multiple items, provided they are separated by commas')
    print("The port in use for HTTP Secure is:", firewalldict['https'])

    ## this SHOULD fail but it will not because we are using the .get method
    print("A safer way to recall that data is to use the .get method:", \
      firewalldict.get('razzledazzlerootbeer'))

    ## use the .keys method to return a list of keys
    print(firewalldict.keys())

    ## use the .values method to return a list of values
    print(firewalldict.values())

    ## remove a single key from the dict
    del firewalldict["sip"]
    print(firewalldict)

if __name__ == "__main__":
    main()
Read through the comments, then save and exit.

Run the script you just wrote. It should work.

student@bchd:~$ python3 ~/mycode/dictrev02.py

Create a third script. In this script, we'll start to focus on methods a bit more.

student@bchd:~$ vim ~/mycode/dictrev03.py

To understand what a method is, you have to understand just a bit about classes and objects. Classes create objects. We won't get into creating classes here, but think of class like factory that can create objects. For example, there is a dict class that creates objects we call dictionaries. Functions can be defined inside of a class, which allows objects instantiated from that class to inherit those functions. We call these inherited functions, 'methods'.

Copy and paste the following into the script.


#!/usr/bin/python3
"""exploring dictionary methods | Alta3 Research"""

def main():
    """run time code"""
    vendordict = {'cisco': True, 'juniper': False, 'arista': True, 'netgear': True}
    custlist = ['acme', 'globex corporation', 'soylent green', 'initech', 'umbrella corporation']

    ## Display the current state of our dictionary
    print(vendordict)

    ## display all of the dictionary methods
    ## focus on the ones without underscores
    ## dict is a special word that Python treats as a dictionary
    ## FYI -- dict would be a terrible variable name
    print(dir(dict))
    # ['clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', \
    # 'update', 'values']

    ## use a few dictionary methods
    print(vendordict.keys())
    print(vendordict.values())
    print(vendordict.get('juniper'))
    ## remove the key:value pair for netgear
    vendordict.pop('netgear')
    ## notice that 'netgear' no longer returns a value (the key:value pair is gone)
    print(vendordict.get('netgear'))

    ## display all of the list methods-- focus on the ones without underscores
    ## list is a special word that Python treats as a list
    ## FYI -- list would be a terrible variable name
    print(dir(list))
    # ['append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', \
    # 'reverse', 'sort']
    custlist.append('cyberdyne')

    ## cyberdyne should now be part of the list
    print(custlist)

if __name__ == "__main__":
    main()
Read over the comments in the code, then save and exit with :wq

Run the script you just wrote. Compare the output to the code and figure out what each of the displayed lines represent.

student@bchd:~$ python3 ~/mycode/dictrev03.py

Great job! That's it for this lab. If you're tracking your code in GitHub, issue the following commands:

cd ~/mycode/
git add *
git commit -m "learning about dictionaries"
git push origin main
Type in username & password
