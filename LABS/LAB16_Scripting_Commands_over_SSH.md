# Scripting Commands over SSH
Lab Objective
The objective of this lab is to learn a way to setup a target VM or container with a particular set of Python dependencies we pull in with the pip utility. This certainly not the only way. It could also easily be altered to pull code from a GitHub repo (or bitbucket), or any other source for that matter. This lab uses RSA keypairs to connect. However, Paramiko can also work with passwording.

This lab was written in response to a student's request for a 'pure Python solution'. And as always, 'MISSION ACCEPTED'

However, for the record, the way Alta3 would do this is to write an Ansible playbook. It could be accomplished in ten or so lines of code and be completely intelligible to everyone within your organization upon first examination. Ansible is a free programming language that is actually 'just' abstracted Python code (Python made easier). It just so happens Alta3 Research teaches a class on that too: https://alta3.com/courses/ansible

Procedure
Open a terminal and create a directory to work in.

student@bchd:~$ mkdir /home/student/mycode/paramikopip/

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

student@bchd:~$ python3 -m pip install paramiko

Move into your new directory

student@bchd:~$ cd /home/student/mycode/paramikopip/

For this script, you'll need a requirements file. A requirements file is a list of all of the current dependencies on the current system. If you are using Python 2.7, then you would just run python -m pip freeze

student@bchd:~/mycode/paramikopip$ python3 -m pip freeze

We can make our own requirements file. It's just a list of what we want to install with pip:

student@bchd:~/mycode/paramikopip$ vim requirements.txt

Let's have pip install Ansible, Scrapy, and Requests. All of these can be found out on pypi as they are very popular projects. Copy and paste the following into your new file:


 ansible
 scrapy
 requests
Create a new script.

student@bchd:~/mycode/paramikopip$ vim deploypipsetup.py

Copy and paste the following into your script:


#!/usr/bin/env python3

## import Paramiko for SSH, import OS for operating system
import paramiko, os

## shortcut issuing commands to remote
def commandissue(command_to_issue):
    ssh_stdin, ssh_stdout, ssh_stderr = sshsession.exec_command(command_to_issue)
    return ssh_stdout.read()

## list of targets
def gettargets():
    targetlist = []
    targetip = input("What IP address do you want to connect to? ")
    targetlist.append(targetip)
    targetuser = input("What UN would you like to use? ")
    targetlist.append(targetuser)
    return targetlist

## Begin collecting information to connect.
connectionlist = []
while(True):
    connectionlist.append(gettargets()) ## creds to connect
    zvarquit = input("Do you want to continue? (y/N): ")
    if (zvarquit.lower() == 'n') or (zvarquit == ""):
        break
    
## prepare requirements file
# reqlocation = input("Please provide the path to the requirements file to deploy: ")
reqfile = input("what is the name of the requirements file? Press ENTER for default (requirements.txt): ")
if reqfile == "":
    reqfile = "requirements.txt"

## define SSH session
sshsession = paramiko.SSHClient()

############# IF YOU WANT TO CONNECT USING UN / PW #############
#sshsession.connect(server, username=username, password=password)
############## IF USING KEYS #################

## mykey is our private key
mykey = paramiko.RSAKey.from_private_key_file("/home/student/.ssh/id_rsa")

## if we never went to this SSH host, add the fingerprint to the known host file
sshsession.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        
## begin connection
for x in range(len(connectionlist)):
    sshsession.connect(hostname=connectionlist[x][0], username=connectionlist[x][1], pkey=mykey)
    ftp_client=sshsession.open_sftp()
    ftp_client.put(reqfile,reqfile)
    ftp_client.close()
    commandissue("sudo apt install python3-pip -y") # ensure pip is installed
    commandissue("python3 -m pip install -r " + reqfile)
Save and exit with :wq then run your script.

student@bchd:~/mycode/paramikosshrsa$ python3 deploypipsetup.py

Add a line of code so that the sshsession object is closed when the for loop ends (we don't want open SSH sessions).

CUSTOMIZATION REQUEST 01 - Alter the code so it asks the user where the requirements.txt file is located and then sets the path to that location.

CUSTOMIZATION REQUEST 02 - Develop the location and name of the requirements file into a function.

If you're tracking your code in GitHub, issue the following commands:

cd ~/mycode
git add *
git commit -m "your commit message"
git push origin main

