Lab Objective
The objective of this lab is to review lists, list methods, and built in functions. Lists are ways to organize data (items) within Python. An item may be just about any object you'd like (string, integer, float, other lists, dictionaries, and so on). Lists are ordered, which means if we place an item at index (position) '7' in the list, it should remain at index (position) '7'. Lists are also mutable, which means they can be altered (re-ordered, remove items, add items, etc.)

Strengthening our skills with Python lists will help us understand and work with JSON (and YAML).

Procedure
Let's stay in the habit of organizing our work. For now, make ~/mycode/ directory.

student@bchd:~$ mkdir ~/mycode/

Create a new script.

student@bchd:~$ vim ~/mycode/listrev01.py

Copy and paste the following into the script.


#!/usr/bin/python3
"""Learning or Reviewing about Lists | by Alta3 Research"""

def main():
    ## create an empty list
    myemptylist = []

    ## add to our list with a list method
    ## The extend method will add every item to the list
    myemptylist.extend('192.168.102.55')

    ## display our list
    print(myemptylist)

if __name__ == "__main__":
    main()
Save and exit with :wq

Run the script you just wrote.

student@bchd:~$ python3 ~/mycode/listrev01.py

Create a second new script.

student@bchd:~$ vim ~/mycode/listrev02.py

Copy and paste the following into the script.


#!/usr/bin/python3
"""Learning or Reviewing about Lists | by Alta3 Research"""

def main():
    anotheremptylist = []

    ## This will throw an ERROR
    ## the extend method expects exactly one argument
    anotheremptylist.extend('10.0.0.1', 'retro_game_server')

    print(anotheremptylist)

if __name__ == "__main__":
    main()
Save and exit with :wq

Run the script you just wrote to see this script ERROR OUT.

student@bchd:~$ python3 ~/mycode/listrev02.py

Create a third script.

student@bchd:~$ vim ~/mycode/listrev03.py

Copy and paste the following into the script.


#!/usr/bin/python3
"""Learning or Reviewing about Lists | by Alta3 Research"""

def main():
    ## create a list already containing IP addresses (strings)
    iplist = ['10.0.0.1', '10.0.1.1', '10.3.2.1']

    ## create a list of ports (strings)
    iplist2 = ['5060', '80', '22']

    ## display list
    print(iplist)

    ## Use the extend method on iplist, our list object
    ## Extend iterates over each 'thing' it is passed, and adds them to a list object
    iplist.extend(iplist2)

    ## show how iplist has changed
    print(iplist)

if __name__ == "__main__":
    main()
Save and exit with :wq

Run the script you just wrote.

student@bchd:~$ python3 ~/mycode/listrev03.py

Create a fourth script.

student@bchd:~$ vim ~/mycode/listrev04.py

Copy and paste the following into the script.


#!/usr/bin/python3
"""Learning or Reviewing about Lists | by Alta3 Research"""

def main():
    ## create a list already containing IP addresses (strings)
    iplist = ['10.0.0.1', '10.0.1.1', '10.3.2.1']

    ## create a list of ports (strings)
    iplist2 = ['5060', '80', '22']

    ## display list
    print(iplist)

    ## Use the append method on iplist, our list object
    ## append takes whatever it is passed and adds it to the list object (iplist)
    ## this will create a list within a list
    iplist.append(iplist2)

    ## show how iplist has changed
    print(iplist)

    ## just like extend, append expects exactly one item to be passed.
    ## If you'd like, uncomment the code below and see the error caused
    # iplist.append('aa:bb:cc:dd:ee:ff', '00:11:22:33:44:55')

if __name__ == "__main__":
    main()
Save and exit with :wq

Run the script you just wrote.

student@bchd:~$ python3 ~/mycode/listrev04.py

Review the script listrev04.py. If you'd like, uncomment the line at the end of the script with the remark that it will make the script fail, then run the script again. This fails because, just like list.extend(), it expects a single argument. list.append() also expects a single argument.

Create a fifth script.

student@bchd:~$ vim ~/mycode/listrev05.py

Copy and paste the following into the script.


#!/usr/bin/python3
"""Learning or Reviewing about Lists | by Alta3 Research"""

def main():
    ## a list of Alta3 classes
    alta3classes = ['python_basics', 'python_api_design', 'python_for_networking', 'kubernetes', \
      'sip', 'ims', '5g', '4g', 'avaya', 'ansible', 'python_and_ansible_for_network_automation']

    ## display the list
    print(alta3classes)

    ## how long is the list? use the built in len function
    ## THEN print (display) the results
    print(len(alta3classes))

    # display python_basics
    print(alta3classes[0])

    # display SIP
    print(alta3classes[4])

    # display Ansible
    print(alta3classes[9])

    ##Uncomment to see a list index out of range error
    #print(alta3classes[99])

    print(alta3classes[0:3])

    print(alta3classes[2:5])

    print(alta3classes[-1])

if __name__ == "__main__":
    main()
Save and exit with :wq

Run the script you just wrote.

student@bchd:~$ python3 ~/mycode/listrev05.py

Review the following rules about list slicing.

Basics of list slicing (this works for strings too). Pretend a is a list or string.


  a[start:end] # items start through end-1
  a[start:]    # items start through the rest of the array
  a[:end]      # items from the beginning through end-1
  a[:]         # a copy of the whole array
There is also the step value, which can be used with any of the above:


  a[start:end:step] # start through not past end, by step
The key point to remember is that the :end value represents the first value that is not in the selected slice. So, the difference between end and start is the number of elements selected (if step is 1, the default).

The other feature is that start or end may be a negative number, which means it counts from the end of the array instead of the beginning. So:


  a[-1]    # last item in the array
  a[-2:]   # last two items in the array
  a[:-2]   # everything except the last two items
Similarly, step may be a negative number:


  a[::-1]    # all items in the array, reversed
  a[1::-1]   # the first two items, reversed
  a[:-3:-1]  # the last two items, reversed
  a[-3::-1]  # everything except the last two items, reversed
After reviewing the rules, feel free to edit ~/mycode/listrev05.py and play around with these rules regarding slicing.

Answer the following questions:

Q: What are lists?
A: Lists offer users ways to create ordered data sets within Python.
Q: Do lists exist outside of Python?
A: Yes! In JSON and other programming languages they're called 'arrays'.
Great job! That's it for this lab. If you're tracking your code in GitHub, issue the following commands:

cd ~/mycode/
git add *
git commit -m "learning about lists"
git push origin main
Type in username & password
