Python to Cisco NX-OS
Lab Objective
The objective of this lab is to demonstrate Python connectivity to a Cisco NX-OS platform, specifically one running the Cisco Nexus 9k software (switch). This lab is comprised of two main components; the first is exposing the API on the device, the second is writing Python code to interact with the Cisco API itself.
Cisco makes writing code for their devices easy via their NX-API sandbox. This is available for users by navigating to management IP of the NX-OS platform after enabling the NX-API via ssh. THIS LAB REQUIRES INSTALLING CISCO VPN CLIENT. This lab is READ-ONLY if you do not have sufficient privileges to install software.

Procedure
Make a Cisco DevNet account by accessing https://developer.cisco.com/site/nx-os/

At the bottom of the screen click the 1 Node Reservable button.

If you don't have a DevNet account this begins the signup process. Complete this process before continuing.

Once you have an account, you will reach the "blueprint" page. Press the reserve button in the upper right corner. This will take 10 minutes to launch.

You'll receive multiple emails. The important one will be received after the 10 minutes are finished.

Inside the final email is a link that says "Download the Cisco AnyConnect VPN Client Software." Click this link to download a zip file. Unzip the file.

The VPN client to install is named "anyconnect-win-4.9.04043-core-vpn-predeploy-k9.msi" (the version may have increased since publication)

After installing the software, launch Cisco AnyConnect Secure Mobility Client (this can be found in the Windows Start menu)

When the Cisco AnyConnect software begins, you'll need to copy the lab network address from the final e-mail you received. Paste this into the Cisco AnyConnect software prompt.

Next you'll be prompted for your username and password (all of which is in your "Your Cisco DevNet Sandbox Lab is Ready" email)

To connect to the NX-OS toolserver (which is really just a Linux server), open putty on your personal machine.

Begin an ssh putty session to the IP address of the model NX-OS toolserver. This IP address is available on the blueprint screen along with the username and password. At the time of this writing, the toolserver credentials are root and cisco123

From your Linux server we now need to ssh into the switch to activate the API. This IP address is available on the blueprint screen along with the username and password. At the time of this writing, the switch credentials are admin and Cisco123

[root@localhost ~]# ssh admin@xx.xx.xx.xx

Put the switch into configuration mode.

switch-n9kv# conf t

The prompt will change. The command below will expose the API.

switch-n9kv(config)# feature nxapi

By default the API uses HTTPS protocol (port 443). For simplicity, we will enable HTTP (port 80). In production it is not advisable to ever run in HTTP mode.

switch-n9kv(config)# nxapi http port 80

Check your work. You should see the API is exposed on port 443 and port 80.

switch-n9kv(config)# show nxapi

Exit configuration mode but do not exit the switch.

switch-n9kv(config)# exit

In your local browser, open a tab to https://xx.xx.xx.xx (use the IP address of your switch) and enter your login info (admin and password Cisco123 were the username/password at publication)

In the top window type a Cisco CLI command. Something simple like show ver is fine.

Take some time to examine what's being presented to you. An HTTP POST was created on your behalf. You are being presented with JSON attached to the post (form data) as well as the JSON response that came back on a 200.

Over in the switch CLI, issue the same command, show ver

switch-n9kv# show ver

Compare the CLI response to the response presented to you on the NX-API sandbox page. The content should be the same, however the JSON is far easier to parse and useful for automation purposes.

Cycle through the tabs available to you (Request, Python, Python3, Java, JavaScript, Go-Lang) where you are provided with the code needed to send a HTTP POST.

On the Linux server provided, we only have Python and not Python3. Therefore copy the code from the Python tab.

Back in your putty terminal, exit the switch.

switch-n9kv# exit

Vim is not installed, so use vi to create your Python script. Use shift insert to paste.

[root@localhost ~]# vi showver01.py

Once you've pasted in the code, you'll need to edit the value of switchuser and switchpassword (admin and Cisco123).

You will also have to add one line to the bottom of your code.


print(response)
Save and exit with :wq

Run your script.

[root@localhost ~]# python showver01.py

You should get the same response that was provided to you in the NX-API sandbox.

OPTIONAL CHALLENGE 01- You're welcome to explore other commands, as the NX-API supports "show" commands and "configuration" commands. If you don't know Cisco commands well, try something simple such as show switchname

That's it for this lab! Cisco appears to let you spin up these environments whenever you need them. Cisco has other devices available as well, DevNet resources are worth bookmarking and exploring!


