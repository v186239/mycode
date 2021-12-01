Logging API Behavior
Lab Objective
The objective of this lab is to learn to explore JSON responses from APIs, as well as create scripts that log their behavior. For this lab, use the following resource:

https://www.anapioficeandfire.com/api

Documentation for the API can be found here:

https://anapioficeandfire.com/Documentation

In this lab, you'll also employ the logging library from the standard library. The library runs deep, so if you have never used it, it is highly recommended that you check out the basic tutorial on the documentation page:

https://docs.python.org/3/howto/logging.html#logging-basic-tutorial

Procedure
Create a directory to work in.

student@bchd:~$ mkdir -p mycode/logging/

Move into the new directory.

student@bchd:~$ cd mycode/logging/

Create a new script icefire.py

student@bchd:~/mycode/logging$ vim icefire.py

Copy and paste the following into your script:


#!/usr/bin/python3
"""RZFeeser | Alta3 Research
Exploring logging options within python"""

# standard library imports
import logging
import argparse
import pprint

# python3 -m pip install requests
import requests

BOOK = "https://www.anapioficeandfire.com/api/books"

def main():

    # if you use logging, always describe your logging.basicConfig @ the start
    # default logging level is 'warning', which would skip less severe warnings
    logging.basicConfig(filename='icefire.log', format='%(levelname)s:%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p', level=logging.INFO)
    
    try:
        # this write
        # INFO: 12/12/2019 11:55:02 AM Program started
        logging.info('Scripting started')
    
        # make a call to the API
        icefire = requests.get(BOOK + "/" + args.bookno)
       
        # force a ZeroDivisionError
        # 10 / 0

        # pretty print the json response
        pprint.pprint(icefire.json())
        
        # write response code to log
        logging.info("API Response Code - " + str(icefire))
        
    # if a program errors, write that error to a log file
    except Exception as err:
        logging.critical(err)
                        
    finally:
        # INFO: 12/12/2019 11:55:02 AM Program ended
        logging.info("Program ended")
        
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--bookno', help='Enter the book number (integer) to look up.')
    args = parser.parse_args()
    main()
Save and exit with :wq

Try running the script. It requires a parameter, so if we run it now. it will cause an error.

student@bchd:~/mycode/logging$ python3 icefire.py

Huh. No error? That's because we trapped it in the log. icefire.log. Try taking a look at it.

student@bchd:~/mycode/logging$ cat icefire.log

Try a few successful runs.

student@bchd:~/mycode/logging$ python3 icefire.py --bookno 2

Another one.

student@bchd:~/mycode/logging$ python3 icefire.py --bookno 1

Great, examine the log again. This time you should see a bunch of successful 200 response codes.

student@bchd:~/mycode/logging$ cat icefire.log

If you'd like to see the log get a bit more interesting, change the line # 10 / 0 to 10 / 0 within your script. Then give it another run and check out the log.

That's it for this lab. If you're looking for more. The Python tutorial has an advanced section.

git add *
git commit -m "Ice and Fire API with logging"
git push origin main
Provide your username & password for https://github.com

