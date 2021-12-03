# Paramiko SFTP with UN and PW
Lab Objective
The objective of these next two labs is to learn to push files across an SFTP connection using Paramiko. These labs use variations of a password/username combination as well as an RSA keypair.

For SFTP connections we can run Paramiko in two ways. The first is to create a general transport object and then invoke the SFTP protocol (FTP/SSH). Alternatively, we can create an SSH object and then invoke SFTP. Both methods are demonstrated within this lab.

Procedure
Create a directory to work in.

student@bchd:~$ mkdir -p ~/mycode/paramikosftp/

Move into the home directory.

student@bchd:~$ cd

Great. Now let's download a script that will build 4 separate SSH targets for us.

student@bchd:~$ wget https://static.alta3.com/projects/ansible/deploy/pexpress-setup.sh

Now download the script that will remove any of the virtual environments when we're done. This clean up script is called, max_teardown.sh

student@bchd:~$ wget https://static.alta3.com/projects/ansible/deploy/max-teardown.sh

Run the script to remove any old virtual environments from previous labs. Always run this script before you run the 'build' script.

student@bchd:~$ bash max-teardown.sh

Run the build script we downloaded to deploy our containers. ONLY IF this is the first time running the script will it take about four or five minutes. It will look like it is stuck, but it is not. Environments are being created! Go get a cup of coffee or something.

student@bchd:~$ bash pexpress-setup.sh

Once your environments are built, try pinging them. First bender.

student@bchd:~$ ping -c 1 10.10.2.3

Now try to ping fry.

student@bchd:~$ ping -c 1 10.10.2.4

Now try to ping zoidberg.

student@bchd:~$ ping -c 1 10.10.2.5

Paramiko allows python to work across SSH tunnels, we'll want to make sure that it is installed. This is supported by Python 2.7+ and 3.x releases, so everyone should feel at home using it. Read the documentation page here: http://www.paramiko.org/installing.html

student@bchd:~$ python3 -m pip install --upgrade pip

student@bchd:~$ python3 -m pip install paramiko

Create a new script.

Make a directory we can copy from:

student@bchd:~$ mkdir /home/student/filestocopy/

Make a empty file for us to copy:

student@bchd:~$ touch /home/student/filestocopy/myfile.txt

Make another empty file for us to copy:

student@bchd:~$ touch /home/student/filestocopy/myfile02.txt

Make a third empty file for us to copy:

student@bchd:~$ touch /home/student/filestocopy/myfile03.txt

Move into the directory where we will write our code.

student@bchd:~$ cd ~/mycode/paramikosftp/

Create a new script.

student@bchd:~/mycode/paramikosftp$ vim sftpmover.py

Copy and paste the following into your script:


#!/usr/bin/env python3
## Moving files with SFTP
# import from standard library
import os

# imports from pip
import paramiko

def main():
    
    ## where to connect to
    t = paramiko.Transport("10.10.2.3", 22) ## IP and port
    
    ## how to connect (see other labs on using id_rsa private / public keypairs)
    t.connect(username="bender", password="alta3")
    
    ## Make an SFTP connection object
    sftp = paramiko.SFTPClient.from_transport(t)
    
    ## iterate across the files within directory
    for x in os.listdir("/home/student/filestocopy/"): # iterate on directory contents
        if not os.path.isdir("/home/student/filestocopy/"+x): # filter everything
                                                              # that is NOT a directory
            sftp.put("/home/student/filestocopy/"+x, "/tmp/"+x) # move file to target location

    ## close the connection
    sftp.close() # close the connection

## call the main function
main()
Save and close, then run the script.

student@bchd:~/mycode/paramikosftp$ python3 sftpmover.py

SSH to the bender container.

student@bchd:~/mycode/paramikosftp$ ssh bender@10.10.2.3

List the contents of /tmp/

bender@bender:~$ ls /tmp/

Remove the files you just moved.

bender@bender:~$ rm /tmp/myfile*

Exit the bender machine.

bender@bender:~$ exit

So our code works, but let's rewrite that code to adhere to some best practice standards. Create a new script.

student@bchd:~/mycode/paramikosftp$ vim sftpmover-updated.py

Copy and paste the code below into your new script. It has been upgraded to accept the directory files to move as an argument from the command line.


#!/usr/bin/env python3
## Moving files with SFTP

## import standard library imports
import os
## import Paramiko so we can talk SSH
import paramiko
## allow user to pass input at prompt
import argparse

def sftpmover(dir2move, sftpsessionobj):
  ## iterate across the files within directory
  for x in os.listdir(dir2move): # iterate on directory contents
    if not os.path.isdir(dir2move+x): # filter everything
                                      # that is NOT a directory
      sftpsessionobj.put(dir2move+x, "/tmp/"+x) # move file to target location

def main():
  ## where to connect to
  t = paramiko.Transport("10.10.2.3", 22) ## IP and port

  ## how to connect (see other labs on using id_rsa private / public keypairs)
  t.connect(username="bender", password="alta3")

  ## Make an SFTP connection object
  sftp = paramiko.SFTPClient.from_transport(t)

  sftpmover(args.moveme, sftp)

  ## close the connection
  sftp.close() # close the SFTP connection
  
  t.close() # close SSH connection

if __name__ == "__main__":
  parser = argparse.ArgumentParser()
  parser.add_argument("moveme", help="Directory containing files you wish to move.", type=str)
  args = parser.parse_args()
  main()
Save and exit with :wq

Run your new script. You'll need to include the directory of files you wish to move (an argument). This argument is mapped to the value moveme within our script.

student@bchd:~/mycode/paramikosftp$ python3 sftpmover-updated.py "/home/student/filestocopy/"

SSH to the bender container, where the files should have returned.

student@bchd:~/mycode/paramikosftp$ ssh bender@10.10.2.3

List the contents of /tmp/

bender@bender:~$ ls /tmp/

Remove the files you just moved (yes, we're going to make another change to our script).

bender@bender:~$ rm /tmp/myfile*

Exit the bender machine.

bender@bender:~$ exit

So our code works but let's rewrite that code to take the IP address and usernames from a flat text file. Create our login file.

student@bchd:~/mycode/paramikosftp$ vim connections.dat

Copy and paste the following into connections.dat


10.10.2.3 bender
10.10.2.4 fry
10.10.2.5 zoidberg
Save and exit with :wq

Now we need to create a new script that accepts connections.dat as an argument and then parses out the data.

student@bchd:~/mycode/paramikosftp$ vim sftpmover-updated02.py

Copy and paste the code below into your new script.


#!/usr/bin/env python3
## Moving files with SFTP

## import standard library imports
import os
## import Paramiko so we can talk SSH
import paramiko
## allow user to pass input at prompt
import argparse

def sftpmover(dir2move, sftpsessionobj):
  ## iterate across the files within directory
  for x in os.listdir(dir2move): # iterate on directory contents
    if not os.path.isdir(dir2move+x): # filter everything
                                      # that is NOT a directory
      sftpsessionobj.put(dir2move+x, "/tmp/"+x) # move file to target location

def main():
  
  with open(args.connectfile, "r") as f:
    for line in f:
      ## where to connect to
      t = paramiko.Transport(line.split(" ")[0], 22) ## IP and port
      ## how to connect (see other labs on using id_rsa private / public keypairs)
      t.connect(username=line.split(" ")[1].rstrip("\n"), password="alta3")
      
      ## Make an SFTP connection object
      sftp = paramiko.SFTPClient.from_transport(t)
      
      sftpmover(args.moveme, sftp)
      
      ## close the connection
      sftp.close() # close the SFTP connection
      
      t.close() # close SSH connection

if __name__ == "__main__":
  parser = argparse.ArgumentParser()
  parser.add_argument("moveme", help="Directory containing files you wish to move.", type=str)
  parser.add_argument("connectfile", help="File containing IPs to connect to.", type=str)
  args = parser.parse_args()
  main()
Save and exit with :wq

Run the help flag against your script to understand what is required to make our script work.

student@bchd:~/mycode/paramikosftp$ python3 sftpmover-updated02.py -h

Run your script.

student@bchd:~/mycode/paramikosftp$ python3 sftpmover-updated02.py "/home/student/filestocopy/" "connections.dat"

SSH to the various boxes to ensure the script worked.

student@bchd:~/mycode/paramikosftp$ ssh zoidberg@10.10.2.5

List the contents of /tmp/ on zoidberg. Our files should be there.

zoidberg@zoidberg:~$ ls /tmp/

Exit zoidberg.

zoidberg@zoidberg:~$ exit

Each example within this script created an object using the transport class. Let's throw together a quick script that copies a file, slurm.cola, to our target hosts and changes the name to slurm.kola. Let's also have it then display the contents of each directory on the remote systems so we can be sure our script worked. Begin by creating an file called slurm.cola.

student@bchd:~/mycode/paramikosftp$ touch slurm.cola

This next connection will use SSH keys instead of passwords! You'll need to copy your id_rsa.pub key into these machines with the following commands:

student@bchd:~$ ssh-copy-id -i ~/.ssh/id_rsa.pub bender@10.10.2.3

student@bchd:~$ ssh-copy-id -i ~/.ssh/id_rsa.pub fry@10.10.2.4

student@bchd:~$ ssh-copy-id -i ~/.ssh/id_rsa.pub zoidberg@10.10.2.5

Create a new script.

student@bchd:~/mycode/paramikosftp$ vim sftpmoveer-dirscrape.py

Copy and paste the following into your script. The script below also uses a keypair to access the remote systems, rather than a username and password combination.


#!/usr/bin/python3
"""Learning about Python SSH | rzfeeser@alta3.com"""

## suppress warnings generated by Paramiko
## at time of writing, paramiko is generating deprecation warnings
import warnings

## python3 -m pip install paramiko
import paramiko

## describe the types of warnings to ignore
warnings.filterwarnings(action="ignore", module=".*paramiko.*")

def main():
    """Our runtime code that calls other functions"""
    # describe the connection data
    credz = [{"un": "bender", "ip": "10.10.2.3"}, {"un": "zoidberg", "ip": "10.10.2.5"},\
            {"un": "fry", "ip": "10.10.2.4"}]

    # harvest private key for all three servers
    mykey = paramiko.RSAKey.from_private_key_file("/home/student/.ssh/id_rsa")
    
    ## loop across credz
    for cred in credz:
        ## create a session object with SSHClient
        sshsession = paramiko.SSHClient()

        ## add host key policy
        sshsession.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        # display our connections
        print("Connecting to... " + cred.get("un") + "@" + cred.get("ip"))
        # make a connection
        sshsession.connect(hostname=cred.get("ip"), username=cred.get("un"), pkey=mykey)

        sftpsession = sshsession.open_sftp()

        # move file, and also rename extension to kola
        sftpsession.put("slurm.cola", "/home/" + cred.get("un") + "/slurm.kola")
        
        # display the current working directory of remote system
        working_dir = sftpsession.listdir()

        print("Files in the remote home directory:")
        for onefile in working_dir:
            # check the FIRST character of the string
            # filter out IF it begins with a "."
            if "." not in onefile[0]:
                print(onefile)
                            
        ## close SFTP and SSH connection
        sftpsession.close()
        sshsession.close()

    print("\nLooping with Python and Paramiko!")
    
main()
Save and exit with :wq

Run your script. It should display the contents of our remote user's home directory. You should see the file slurm.kola was moved to all the home directories of our users.

student@bchd:~/mycode/paramikosftp$ python3 sftpmoveer-dirscrape.py

CUSTOMIZATION REQUEST 01 - Looking to further your understanding? Add general exception handling to one of the scripts. On an error, always attempt to close the connection and print out an message indicating some kind of connection error occurred. Error handling is controlled with try and except statements in Python. If you have never studied this, you may need to do some Google research or ask the instructor for some help.

When you finish, be sure to run the max-teardown.sh script, to clean up your virtual environments.

student@bchd:~$ bash ~/max-teardown.sh

If you're tracking your code in GitHub, issue the following commands:

cd ~/mycode
git add *
git commit -m "Paramiko and SFTP"
git push origin main
Type your username and password

