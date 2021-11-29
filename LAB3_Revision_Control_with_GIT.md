# Revision Control with Git and GitHub
In this lab, we're going to explore SCM, or Software Control Management platforms. Git is the de-facto tool for tracking and version controlling your work. Git is a tool that we run on our local machine. GitHub is an HTTPS browser-friendly platform that syncs with git, and makes your code available to the world. This is a good thing.

In this lab, you'll make a GitHub account. This is free and will allow you to save the code you develop this week.

Procedure - GitHub Account
In your local browser, open a new tab to https://github.com

Click on Sign-up on the landing page.

Enter the following information.

Username - This handle will be shared with career professionals.
Email Address - Use an email address you check often.
Password - Always make passwords unique and ultimately change them often.
Now click on the Create account button at the bottom of the screen.

At the bottom of the screen, click the green Continue button.

Answer the questions as best you can to help the GitHub metrics, and then click Submit at the bottom of the screen.

You'll need to verify your email address. Check the email address you used to sign up, and click on the link or button they sent to you.

Now that we have a verified GitHub account, let's try tracking some work. In the upper right hand corner, click on your profile icon, then on Your Profile. This is where you can choose to create a bio and a profile. This account is public and the world will look at your code, so be professional.

In the center of the screen, click on the word Repositories, which is followed by a 0.

Click on the green New button, with the little book icon on it. This creates a repository. Repositories track work.

Set the Repository name as mycode.

Set the Description as something like, Tracking my code

The repository should be set to Public.

The README option is always best practice, so check the box. The objective is to describe what your repo contains.

Change Add a license: None to GNU General Public License v3.0. Here's the TLDR, "We're comfortable with the world borrowing our code, provided they give us credit, should it get used."

Now click the green Create repository button at the bottom of the screen.

Your new repo will appear. Click on the file, README.md.

You'll find a small pencil on the right side of the screen. Click on this.

Enter the following template into your README.md and then customize it. The goal is to advertise to the world the purpose of your repository. Don't hold back. If you're a 1st time student interested in Microservices and/or Python, let the GitHub community know! FYI, files on GitHub are written in markdown which is a web-friendly way to format text. Read about it here: https://guides.github.com/features/mastering-markdown/


# mycode (Project Title)

One Paragraph of your project description goes here. Describe what you're trying to do.
What is the purpose of putting up this repo?

## Getting Started

These instructions will get you a copy of the project up and running on your local machine
for development and testing purposes. See deployment for notes on how to deploy the project
on a live system.

### Prerequisites

What things are needed to install the software and how to install them. For now, maybe copy in
"how to install python and python3 using apt."

## Built With

* [Python](https://www.python.org/) - The coding language used

## Authors

* **Your Name** - *Initial work* - [YourWebsite](https://example.com/)
When you finish, click the green Commit changes button at the bottom of the screen.

Generally, we don't want to use GitHub as a development tool. Just for viewing. But to get our README.md started, this is fine. From now on, we'll only add to our repo from the command line.

At the top of the screen, click on your username to return to your homepage.

You should see your repository mycode.

GitHub lets you have friends just like other social media platforms. Checkout all of the Alta3 Python Instructors:

Zach
Sam
Chad
While you are there, click follow, to follow all of your Alta3 Python Instructors.

You might try asking some fellow students for their usernames and repeating the above steps.

RETURN TO YOUR ALTA3 TMUX ENVIRONMENT NOW

Now we want to sync our command line (where we run git) with GitHub. The goal is to get our code into the mycode repo we created. Move to the ~/.ssh home directory.

student@bchd:~$ cd /home/student/.ssh

Now we will generate a new RSA keypair. We will use this to communicate securely with GitHub because as of August 2021, GitHub will no longer accept passwords from us. This will generate two files, the private key (id_rsa_github) and the public key (id_rsa_github.pub).

student@bchd:~/.ssh$ ssh-keygen -f id_rsa_github


Generating public/private rsa key pair.
Enter passphrase (empty for no passphrase):
When you see this, you will need to hit enter twice


Enter same passphrase again:
Your identification has been saved in id_rsa_github.
Your public key has been saved in id_rsa_github.pub.
The key fingerprint is:
SHA256:DFjw7WCP+u2luMtPATqKHGBi/+XNUzlRYfqIYz8S2/Q student@bchd
The key's randomart image is:
+---[RSA 2048]----+
|    ...      +.  |
|     + .    +    |
|oo  . * .  o     |
|= .  o O  . =    |
| . .o ..S= * .   |
|.....oo +.O o    |
|... .. ..*.+ E   |
|     o + oo .    |
|      *==        |
+----[SHA256]-----+
Next we need to copy the text from inside of the id_rsa_github.pub public key into our clipboard. We will need to paste this into GitHub soon.

student@bchd:~/.ssh$ cat id_rsa_github.pub


ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCvTemj7NIlxXEu97VyN4wcmob+F0wQ0nPinZSdUvlWSGAx790EmfXmckZ01/aFDOKIA4OZWYtW95DaGqQ+Tja3QUYlAdTdIlp4TTgH3ZE+KdaLc16rN9FzHv8hwdLFx8CugNw/u/sDbYjEM1qlazB5fbAf0LZ+mN5iCDn6IaYbPZ0wQdF9s4RI/z5wS5wE/J++KV/xJA0f2ICZwaKj4Kq/fron2KoYRkCYcma0oHYvVSnnuxCVGbOJdhWK1LiJRPweNUajp0OItECJxgCR1gB/DVEWnBmknOcPnY6q3QeaUrm28nPSAjGTkfFSHDbOJptaqKaSkRhwNsuOGiw6KQ1R student@bchd
Select all of the output and copy it. NOTE: Yours will be different than the one listed above!

RETURN TO GITHUB NOW

At the top of the screen, click on your username to return to your homepage.

You should see your repository mycode. Click into it.

Near the top right of the screen, there is a little gear icon that says Settings. Click on that.

On the left of the screen, click on Deploy Keys. Deploy keys are essentially a token that we set up that allow somebody to read from, and optionally write to, our repository, even if it is private. They just need to have the private key set up on their system as a means of authenticating with the public key stored on github.

Your screen should look like the following. Click on the button that says Add deploy key.

deploy key

Give your key a name. alta3 environment would work. Then paste your key (from id_rsa_github.pub) into the large text box. And also click on the checkbox that says Allow write access. Then, click Add key.

deploy key pt 2

RETURN TO YOUR ALTA3 TMUX ENVIRONMENT NOW

Fantastic. Let's set up git for first-time use. First of all, let's move back to our home directory.

student@bchd:~/.ssh$ cd ~

Replace the name Mona Lisa with your own! When you perform a git commit, this is the name that will be applied to the commit (the save).

student@bchd:~$ git config --global user.name "Mona Lisa"

Replace the username portion (only) of the email address monalisa@users.noreply.github.com with your github username. When you perform a git commit, this is the email that will be applied to the commit (the save). The domain users.noreply.github.com with cause emails sent to you to end up in your GitHub account (not your SMTP inbox).

student@bchd:~$ git config --global user.email "monalisa@users.noreply.github.com"

Customize the command below so that the entire <github-username> is replaced with only your GitHub username. The angle brackets are not allowed.

student@bchd:~$ git clone git@github.com:<github-username>/mycode.git

If you run into an error with this step, read the instructions once more and try it again!

You should now have a new folder (mycode) in your home directory. Move into it.

student@bchd:~$ cd /home/student/mycode/

Let's edit README.md

student@bchd:~/mycode$ vim /home/student/mycode/README.md

At the top of your README.md file, within your project description, add a sentence about wanting to learn how to version control projects with git. (Press the i key to enter insert mode).

Exit insert mode with ESC.

Save (write) and exit with :wq and then ENTER

The following steps are ones you should memorize. You'll be issuing these commands all the time. First issue git status, which will reveal if you added something and forgot about it.

student@bchd:~/mycode$ git status

Next we'll describe what we want to add to our repo. We'll wildcard this, so everything in the ~/mycode/ directory is added.

student@bchd:~/mycode$ git add *

Time to perform a commit. This makes a new version.

student@bchd:~/mycode$ git commit -m "First commit to learn about version controlling"

Now push your new version to GitHub for tracking. By default, the keyword origin points to the repo you cloned the repo from. Enter the following followed by your username and password.

student@bchd:~/mycode$ git push origin

Go up to GitHub, and see if your README.md file has changed. Remember, we don't want to edit any files in GitHub anymore. Just validate that GitHub has the new data.

You should get in the habit of issuing the following commands each time you have a success, or end for the day:

git status
git add /home/student/mycode/*
git commit -m "reason for commit"
git push origin
Great! Move back to your home directory.

student@bchd:~/mycode$ cd /home/student/

Troubleshooting
The following items resolve most student issues with connecting to GitHub.

"origin" is defined incorrectly
The variable origin needs to be set to use SSH protocol, not HTTP. You can check how it is set by issuing, cat ~/mycode/.git/config.

If you see mention of url = https://github.com/..., you need to redefine origin by issuing the following command from inside the directory ~/mycode/


`git remote set-url origin git@github.com:YourGitHubUsername/mycode`
You'll need to replace, YourGitHubUsername with your actual GitHub account name.

The public key you generated is misnamed
The key-pair you generated should be named, id_rsa_github and id_rsa_github.pub. If they are named something else, regenerate them with the correct name, and place the new public key on GitHub.

Alternatively, you can update the entry in the file ~/.ssh/config. There is an entry for github.com that indicates the name of the private key to use (private keys do not have .pub extension). Change the entry the config file to reflect the name of the keypair that you created. Save and quit, then try to push to GitHub again.

Histories cannot be merged
If you are seeing this error, the safest and easiest solution is to delete the repository on GitHub.com (but not locally). Create a new mycode repo on GitHub without a README.md (or any other file). This is called a "bare" repository. Try pushing your code to this new repo.

Nothing to push
You need a commit to push to GitHub.com. Get a list of all the commits in your local repository with git log. If you don't see anything recent, you might need to perform the git add / git commit commands before you can get a commit to push to GitHub.

Other Useful Resources
If you ever run into a problem using git / GitHub, let the instructor know. It is critical to start learning to version control code. You might want to spend some time clicking around on the following guides. They're quite short, and although you might not understand what they're talking about, they'll begin exposing you to the way we 'speak' when using git & version controlling software. Some getting started guides relating to GitHub can be found here: https://guides.github.com/

Windows and Mac users might also check out the local client GitHub Desktop, available at https://desktop.github.com/ This client makes it easy to work through git via a local GUI on your Windows or Mac desktop environment.


