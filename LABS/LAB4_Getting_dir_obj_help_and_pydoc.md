# Getting dir(obj) help() and pydoc
Lab Objective
The objective of this lab is to view the available built-in methods for you to use with the dir() function while in the Python shell. Methods can be described using the help() function. This is a useful way to learn about what is possible with Python.

Before starting this lab, it might help to review the following links:

https://docs.python.org/3/library/ - Python Standard Library

https://docs.python.org/3/library/functions.html - Python Standard Library Functions

Procedure
Determine what version of python is installed.

student@bchd:~$ python3 --version

Launch the python3 interpreter.

student@bchd:~$ python3

When you install Python, you are given access to the "standard library" which includes many functions. Functions are just references to code, so think of functions as, "call on us anytime you just want to repeat some code". If you haven't already, you can review the list of available Python functions here. Start by using the dir() function.

>>> dir(str)

What has been returned to us is all of the methods that can be used to alter string (str) objects. Let's create a string object.

>>> x = "EthGIG01"

Run dir() function on our string x, the same output should be returned that we saw previously.

>>> dir(x)

Let's pick one and learn about it, like lower(). Methods always trail the object using dot notation.

>>> x.lower()

Cool. Looks like it made every character lowercase. Sometimes methods have help pages. Try the following command to reveal the help page for lower().

>>> help(x.lower)

Press q to quit the help page. Then try another method. The upper() method will make all characters uppercase.

>>> x.upper()

We can also 'chain' together methods. When we do, they are processed from left to right. The method startswith() expects a string argument and returns a true or false value. The following line first converts the x string-object to lowercase then returns True because it 'startswith' eth.

>>> x.lower().startswith("eth")

Alta3's Office is in Hershey, PA where there's lots of dairy farms... which means lots of tractors. Think of a tractor as an object and its specialty attachment, the hay baler, as a method. After the hay baler's job is complete, it passes the hay bale off to the second specialty attachment, the trailer, which is like a second method. The analogy works in that these attachments can be mixed-and-matched (to a point).

Classic-Hershey-Pennsylvania-Tractor-Example

Everything in Python is an object. So, suppose we imagine a new Python object, like a boat. Boats don't have hay balers. That is to say, methods are uniquely associated with an object's type. To explore the concept further, let's create a file-object called x that has the attributes of myfile.txt, in write-mode (as in, we want to write text to it). We'll study input/output later, for now, we want to focus on getting to methods available to an object.

>>> x = open("myfile.txt", "w")

Now run dir() on our fileobject

>>> dir(x)

Wow. These are a lot different than the methods associated with string-object. Let's read the help() page on the read() method.

>>> help(x.read)

Press q to quit the help page. Did you notice some methods are surrounded by underscores? Those are built in methods, and in Python 3 they are no different than any other method (whereas in Python 2 they were kind of special...). Let's start to explore them as well. Start by making x an integer (int) object.

>>> x = 5

Run dir() on x

>>> dir(x)

Change the attribute of integer object x by using the __add__() function.

>>> x.__add__(6)

The result is 11... which is 5 + 6. In Python, the + sign has actually been mapped to use the __add__() method. The __le__() method is the > (less than) method. Try it out. The following expression is read, "Is x less-than 3?".

>>> x.__le__(3)

Hopefully methods are starting to make sense. To be clear, methods are different than functions. Functions are just repeating code blocks. Methods are repeating code blocks that are applied directly to an object, as in: object.method()

Exit the Python interpreter.

>>> exit()

You can check out the same documentation you saw with the help() from outside of a Python environment using pydoc. Let's use pydoc to read about the open function.

student@bchd:~$ python3 -m pydoc open

Press q to quit.

Let's use pydoc to read about the time module. You can use pydoc anytime you want to get more information about a Python module.

student@bchd:~$ python3 -m pydoc time

Press q to quit.

Answer the following questions:

Q: What are functions?
A: References to defined code. Functions allow designers to write less, and increase the manageability of code as your project grows in complexity.
Q: What is a class?
A: A class creates objects. They're a bit like object factories.
Q: What is a method?
A: Classes build objects. A method is just a function defined within a class. Therefore, when you create an object (like a string or list), they inherit the functions defined within their class.
Q: Do I have to understand classes, objects, and functions to be successful with Python?
A: Not at all. Understanding how objects are initialized, and then interact with functions and methods can help you make better sense of pip, import statements, dot notation, and writing more efficient code. However, you'll learn that stuff as you work with Python. Don't let it be a barrier to picking up Python to solve a problem.
Good job, that's it for this lab. Nothing to commit to GitHub this time.

Additional Resources
Python Standard Library - Python Standard Library

Python Standard Library Functions - Python Standard Library Functions

