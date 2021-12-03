# Introducing Paramiko
Lab Objective
The objective of this lab is to introduce the Paramiko, as well as the getpass standard library.

Paramiko is a 3rd party library for simplifying the process of SSHing to remote targets. The libarary also allows for the establishment of FTP sessions over SSH (SFTP).

The getpass.getpass() prompts the user for a password without echoing (as with input()). Using getpass provides a secure way to handle the password prompts where programs interact with the users via the terminal.

Documentation on the Paramiko libarary can be found here:
http://www.paramiko.org/

Documentation on the getpass standard library can be found here:
https://docs.python.org/latest/library/getpass.html

Procedure
Create a directory to work in.

student@bchd:~$ mkdir -p ~/mycode/passwd/

Move into your new directory:

student@bchd:~$ cd ~/mycode/passwd/

Create a new script.

student@bchd:~/mycode/passwd$ vim firstpasswd.py

Copy and paste the following into your script:


#!/usr/bin/python3
# A simple Python program to demonstrate  getpass.getpass() to read password 
import getpass 

def main():
    p = getpass.getpass() 
    print("Password entered:", p)
    
if __name__ == "__main__":
    main()
Run this very basic script, and make sure that it works. Try entering alta3 as your password.

student@bchd:~/mycode/passwd$ python3 firstpasswd.py

Move down to your home directory.

student@bchd:~/mycode/passwd$ cd

Great. Now let's download a script that will build 4 separate SSH targets for us.

student@bchd:~$ wget https://static.alta3.com/projects/ansible/deploy/pexpress-setup.sh

Now download the script that will remove any of the virtual environments when we're done. This clean up script is called, max_teardown.sh

student@bchd:~$ wget https://static.alta3.com/projects/ansible/deploy/max-teardown.sh

Run the script to remove any old virtual environments from previous labs. Always run this script before you run the 'build' script.

student@bchd:~$ bash max-teardown.sh

Run the build script we downloaded to deploy our containers. ONLY IF this is the first time running the script will it take about four or five minutes. It will look like it is stuck, but it is not. Environments are being created! Go get a cup of coffee or something.

student@bchd:~$ bash pexpress-setup.sh

Great. Now try to SSH to each.

student@bchd:~$ ssh bender@10.10.2.3

If prompted, type 'yes' to accept the key, then exit.

bender@bender:~$ exit

Now, fry.

student@bchd:~$ ssh fry@10.10.2.4

If prompted, type 'yes' to accept the key, then exit.

fry@fry:~$ exit

Finally, zoidberg.

student@bchd:~$ ssh zoidberg@10.10.2.5

If prompted, type 'yes' to accept the key, then exit.

zoidberg@zoidberg:~$ exit

Paramiko works across SSH tunnels. So we'll want to make sure that is installed. This is supported by Python 2.7+ and 3.x releases, so everyone should feel at home using it. Read the documentation page here: http://www.paramiko.org/installing.html

student@bchd:~$ python3 -m pip install paramiko

Move back to your ~/mycode/passwd directory and create a new script.

student@bchd:~/mycode/passwd$ cd ~/mycode/passwd && vim secondpasswd.py

Copy and paste the following into your script:


#!/usr/bin/python3
## Try a real world test with getpass

## import Paramiko so we can talk SSH
import paramiko # allows Python to ssh
import os # low level operating system commands
import getpass # we need this to accept passwords


def main():
    ## where to connect to
    t = paramiko.Transport("10.10.2.3", 22) ## IP and port of bender
    
    ## how to connect (see other labs on using id_rsa private / public keypairs)
    t.connect(username="bender", password=getpass.getpass()) # notice the password references getpass
    
    ## Make an SFTP connection object
    sftp = paramiko.SFTPClient.from_transport(t)
    
    ## copy our firstpasswd.py script to bender
    sftp.put("firstpasswd.py", "firstpasswd.py") # move file to target location home directory
    
    ## close the connection
    sftp.close() # close the connection
if __name__ == "__main__":
    main()
Save and close, then run the script (see the next step, you'll need to enter the password alta3).

student@bchd:~/mycode/passwd$ python3 secondpasswd.py

Enter the password: alta3

SSH to bender and confirm that your script firstpasswd.py was moved.

student@bchd:~/mycode/passwd$ ssh bender@10.10.2.3

SSH to bender and confirm that your script firstpasswd.py was moved.

bender@bender:~$ ls

Exit bender.

bender@bender:~$ exit

When you finish, be sure to run the max-teardown.sh script, to clean up your virtual environments.

student@bchd:~$ bash ~/max-teardown.sh

If you're tracking your code in GitHub, issue the following commands:

cd ~/mycode
git add *
git commit -m "your commit message"
git push origin main
Type username and password
