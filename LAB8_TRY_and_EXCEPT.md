# Try and Except
Lab Objective
The objective of this lab is to introduce the try and except block. Given a try block, you will always have (at least) a single except block. Other possibilities include multiple except statements, else, and/or finally.

The try statement works in the following way. First, the try block will attempted to be executed. If no exception occurs, the except clause is skipped and execution of the try statement is finished.

If an exception occurs during execution of the try clause, the rest of the clause is skipped. Then if its type matches the exception named after the except keyword, the except clause is executed, and then execution continues after the try statement.

If an exception occurs which does not match the exception named in the except clause, it is passed on to outer try statements; if no handler is found, it is an unhandled exception and execution stops with a standard error message.

Errors may be general, or specific. A list of possible errors is as follows, or checked out at the following website https://docs.python.org/3/library/exceptions.html:

Exception - Cause of Error
AssertionError - Raised when assert statement fails.
AttributeError - Raised when attribute assignment or reference fails.
EOFError - Raised when the input() functions hits end-of-file condition.
FloatingPointError - Raised when a floating point operation fails.
GeneratorExit - Raise when a generator's close() method is called.
ImportError - Raised when the imported module is not found.
IndexError - Raised when index of a sequence is out of range.
KeyError - Raised when a key is not found in a dictionary.
KeyboardInterrupt - Raised when the user hits interrupt key (Ctrl+c or delete).
MemoryError - Raised when an operation runs out of memory.
NameError - Raised when a variable is not found in local or global scope.
NotImplementedError - Raised by abstract methods.
OSError - Raised when system operation causes system related error.
OverflowError - Raised when result of an arithmetic operation is too large to be represented.
ReferenceError - Raised when a weak reference proxy is used to access a garbage collected referent.
RuntimeError - Raised when an error does not fall under any other category.
StopIteration - Raised by next() function to indicate that there is no further item to be returned by iterator.
SyntaxError - Raised by parser when syntax error is encountered.
IndentationError - Raised when there is incorrect indentation.
TabError - Raised when indentation consists of inconsistent tabs and spaces.
SystemError - Raised when interpreter detects internal error.
SystemExit - Raised by sys.exit() function.
TypeError - Raised when a function or operation is applied to an object of incorrect type.
UnboundLocalError - Raised when a reference is made to a local variable in a function or method, but no value has been bound to that variable.
UnicodeError - Raised when a Unicode-related encoding or decoding error occurs.
UnicodeEncodeError - Raised when a Unicode-related error occurs during encoding.
UnicodeDecodeError - Raised when a Unicode-related error occurs during decoding.
UnicodeTranslateError - Raised when a Unicode-related error occurs during translating.
ValueError - Raised when a function gets argument of correct type but improper value.
ZeroDivisionError - Raised when second operand of division or modulo operation is zero.
Procedure
Make a new directory to work in:

student@bchd:~$ mkdir -p ~/mycode/err/

Move into our work directory.

student@bchd:~$ cd ~/mycode/err/

Edit a new script in our development directory.

student@bchd:~/mycode/err$ vim ~/mycode/err/try01.py

Our first script will catch all possible exceptions. Copy the following code block:


#!/usr/bin/python3
"""Review of try and except logic | Alta3 Research"""

# Start with an infinite loop
while True:
    try:
        print("Enter a file name: ")
        name = input()
        with open(name, "w") as myfile:
            myfile.write("No problems with that file name.")
        break
    except:
        print("Error with that file name! Try again...")
Save and exit with :wq

Run your script.

student@bchd:~/mycode/err$ python3 ~/mycode/err/try01.py

Enter test01.txt. It should end as normal. When the script ends, use ls to confirm it was made.

Run your script again. Just press Enter and it should say "Error with that file name! Try again...". Finally enter a unique file name.

Create a new script:

student@bchd:~/mycode/err$ vim ~/mycode/err/try02.py

We can also handle specific errors, such as a ZeroDivisionError. Error handling is a kind of FIFO operation, so if the error is not a ZeroDivisionError, our general error handling, except Exception as err will called.


#!/usr/bin/python3
"""Catching specific errors | Alta3 Research"""

# Start with an infinite loop
while True:
    try:
        print("Let's divide x by y!")
        x = int(input("What is the integer value of x? "))
        y = int(input("What is the integer value of y? "))
        print("The value of x/y: ", x/y)
    except ZeroDivisionError as zerr:
        print("Handling run-time error:", zerr)
    # general error handling
    # a practical use might be exceptions we haven't designed solution for yet
    except Exception as err:
        # sys.exc_info returns a 3 tuple with into about the exception handled
        print("We did not anticipate that:", err)
Save your script as /home/student/mycode/err/try02.py

Run your script.

student@bchd:~/mycode/err$ python3 ~/mycode/err/try02.py

On the first run, trigger a ZeroDivisionError by entering 5, followed by 0. This illegal condition triggers the exception we have already defined.

On the second run, enter homer as a value for x or y. The program will error. First it will display, "We did not anticipate that", followed by the class of error produced. Next, the raise condition will replay the error. We should build a solution to this "ValueError".

Create a new script.

student@bchd:~/mycode/err$ vim ~/mycode/err/try03.py

Edit your script so it looks like the following.


#!/usr/bin/python3
"""try except and else | Alta3 Research"""

# Start with an infinite loop
while True:
    try:
        print("\nLet's divide x by y!")
        x = int(input("What is the integer value of x? "))
        y = int(input("What is the integer value of y? "))
        print("The value of x/y: ", x/y)
    except ZeroDivisionError as err:
        print("Handling run-time error:", err)
    except ValueError as err:
        print("That was not a legal value for division:", err)
    # general error handling
    # a practical use might be exceptions we haven't designed solution for yet
    except Exception as err:
        # sys.exc_info returns a 3 tuple with into about the exception handled
        print("We did not anticipate that:", err)
        # raise by itself simply calls the previous exception that was thrown
        raise
    # else ONLY runs if there wasn't any errors
    else:
        print("\nThanks for learning to handle errors!")
        break
Save your script as /home/student/mycode/err/try03.py

Run your script.

student@bchd:~/mycode/err$ python3 ~/mycode/err/try03.py

This time try entering wool. A Value Error is still created, but the program does not end.

Enter 7 for x and 7 for y. The program should complete and finish, as the else logic is evaluated. In this example, we understand the else block to imply 'this code only runs if there were no exceptions'.

Now that we are starting to handle errors, lets try writing our error to a log. Create a new file:

student@bchd:~/mycode/err$ vim ~/mycode/err/try04.py

Copy the following into your new script. In this example, imagine we're trying to write a piece of a program that looks for a configuration file we need to load into a network switch or router. To simulate a ticket order, we'll generate a UUID using import uuid. A handy part of the Python Standard Library: https://docs.python.org/3/library/uuid.html


#!/usr/bin/python3
"""try except else and finally | Alta3 Research"""

# python standard library
import uuid

# generate a UUID based on the host id, sequence number, and current time
# simulating a ticketed job number
ticket = uuid.uuid1()

try: # try to do this
    print('Type the name of the configuration file to load.')
    configfile = input('Filename: ')
    with open(configfile, 'r') as configfileobj:
        switchconfig = configfileobj.read()
except: # if any errors occurred
    x = 'General error with obtaining configuration file!'
else: # if there were no errors
    x = 'Switch config file found.'
finally: # in all cases, write out what happened to a log file
    with open("try04.log", "a") as zlog:
        print('\n\nWriting results of routine to log file')
        print(ticket, " - ", x, file=zlog)
Save your script as /home/student/mycode/err/try04.py

Run the above script.

student@bchd:~/mycode/err$ python3 ~/mycode/err/try04.py

Enter the value switch.conf, this file is not on our local system, so it will cause an error, which will get written into try04.log

Display the value of ~/mycode/err/try04.log

student@bchd:~/mycode/err$ cat ~/mycode/err/try04.log

Run the script a few more times to ensure the log file is continually collecting errors.

The way to read your code is as follows: "Try this code. On an exception do these things; else if there are no exceptions, do these things- finally, do this stuff as you exit through the giftshop!"

If you're tracking your code in GitHub, issue the following commands:

cd ~/mycode/
git add *
git commit -m "A bit on error handling"
git push origin main
Type in your username and password
