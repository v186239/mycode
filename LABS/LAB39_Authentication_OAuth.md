OAuth
Lab Objective
The objective of this lab is to design an API that is able to request and use an OAuth token as its auth method for performing specific actions. OAuth is an Authorization Framework version 2.0 (current). It enables third-party applications to obtain limited access to an HTTP service, such as a website. This is most typically done via an End User approving an interaction between the HTTP service and the third-party application.

You will achieve this by generating an OAuth token token on GitHub and used it to authenticate using our own 3rd Party Service (python script) with our Resource Server (GitHub) and perform the actions of listing and creating repositories.

Photo Printing Example - OAuth Application
Let's imagine that an End User has recently taken a trip to Wakanda, and they stored all of their wonderful pictures of their journey on an online photo storage and sharing service, more aptly known as a Resource Server. In order to access this service, the End User must authenticate using a username and password, like so:
OAuth Password Authentication

Once this user has authenticated with their Resource Server, they will be able to perform ALL of the actions available to their specific user. In this case, let's imagine that they are able to upload, download, and delete pictures from this Photo Sharing Service. OAuth User Permissions

However, they have a problem. In order to afford the trip to Wakanda, they had to sell their own personal printer, and all of it's ink. They cannot print their awesome pictures at home, and now must have some other service print these photos, referred to as a Client, or a 3rd Party Service. But they don't want to go through the hassle of downloading these super-hi-resolution photos, and then uploading them to the printing service. They want the internet to take care of this hassle. So they now face this conundrum:

OAuth Why?

Option 1 is to simply give this 3rd Party Service their login information to the Photo Sharing Service. This would let the 3rd Party Service access the photos as requested. However, this also will grant them ALL OF THE PERMISSIONS THE END USER HAS. This is not a good plan.

OAuth do not do Option 2 is a much better option, known as OAuth. This process is not simple to set up on the backend, but makes the authorization flow for users incredibly simple, and it will allow for the 3rd Party Service to have a limited scope of actions to take in your Resource Server. You may have even already used OAuth without knowing it.

From the user's point of view, the flow in the diagram below would be: 0. Sign in to the 3rd Party Printing Service.

Ask the 3rd Party Printing Service to connect to your Photo Sharing Service.
Get Prompted with a "Sign in" page for your Photo Sharing Service.
Sign in to the Photo Sharing Service and click the button that says "Allow 3rd Party Printing Service to access your Photos."
Use your 3rd Party Printing Service to select photos and order them to be printed
OAuth Explained

Now that the first interaction has between your 3rd Party Printing Service and the Photo Sharing Service has been authorized by you, there is no further need for the user to authenticate the 3rd Party Printing Service. It is the responsibility of the 3rd Party Printing Service to retain and periodically update the token that it must use to authenticate to the Photo Sharing Service.

Additionally, the Photo Sharing Service has the responsibility to assure that the token that does get generated offers only limited actions to the service using it. In this case, there is no reason why a printing service would ever need to add or delete pictures from your account, so the only permission that should be granted to it would be to browse and download these images.

OAuth Used

Procedure
Using your local browser, log in to https://github.com.

Click on your profile picture in the top right corner, then select Settings (near the bottom of the dropdown).

On the left hand navigation bar, near the bottom, click on Developer Settings.

Dev settings

Next, select Personal access tokens.

Personal access token 1

Then Generate new token.

Personal access token 2

Now we need to give our personal access token a name, as well as one or more scopes. The name is up to you, or feel free to use the example given of ouath_example_1. Then, select the radio (checkmark) button to the left of the bold word repo inside of the Select scopes section of this page. This grants ANYBODY WITH THIS TOKEN complete access to your repos. All of them.

For your token --- "Keep it secret. Keep it safe" - J. R. R. Tolkien

Generate New token

Scroll down to the bottom of the page and select the green Generate Token button.

You now should be back at your main Personal access tokens page, and see that there is a new token there for you. Make sure that you copy this token right now, and put it somewhere safe. As soon as you move off of this page, you lose the ability to view it any more. We will need this token for the rest of the lab.

Copy new token

BACK IN YOUR TERMINAL ENVIRONMENT you will soon be creating a new python script file for generating requests using your token. But first we will need to save this token in a safe location. Create the following file, and paste your token in there.

student@bchd:~$ vim ~/token


fea2009de2a192kdk9k10a3k39as605d
Save and Quit

Now we will make a new oauth directory and move into there.

student@bchd:~$ mkdir -p ~/mycode/oauth

Move into ~/mycode/oauth

student@bchd:~$ cd ~/mycode/oauth

Before we get too far ahead of ourselves, let's take a look at what we can do with our token manually. The primary purpose that we tasked our token with doing is allowing us to connect to our private repos. But it also is a viable way to let us authenticate with GitHub's API for other use cases too. So before reaching into the realm of repos, let's try to do something simple like grab an SSH public key from some user's GitHub account. But even before this, perform the following command:

student@bchd:~/mycode/oauth$ curl https://api.github.com/rate_limit


{
  "resources": {
    "core": {
      "limit": 60,
      "remaining": 60,
      "reset": 1615234282,
      "used": 0
    },
    "graphql": {
      "limit": 0,
      "remaining": 0,
      "reset": 1615237644,
      "used": 0
    },
    "integration_manifest": {
      "limit": 5000,
      "remaining": 5000,
      "reset": 1615237644,
      "used": 0
    },
    "search": {
      "limit": 10,
      "remaining": 10,
      "reset": 1615234104,
      "used": 0
    }
  },
  "rate": {
    "limit": 60,
    "remaining": 60,
    "reset": 1615234282,
    "used": 0
  }
}
This command shows us the number of requests that we have remaining for our IP address. There is a chance that you actually are out of any remaining due to others in this same IP address using them all up. That is okay, because this is currently being done without any authentication.

Next, we can use our token as an authentication method for GitHub's API. This will allow us to authenticate via our specific user, not just from a specific IP address (that you share with all of your classmates). Paste your personal token in where it says <token>. And notice how you have gone from a rate of 60 requests to 5000.

student@bchd:~/mycode/oauth$ curl -H "Authorization: token <token>" https://api.github.com/rate_limit


{
  "resources": {
    "core": {
      "limit": 5000,
      "used": 0,
      "remaining": 5000,
      "reset": 1615235630
    },
    "search": {
      "limit": 30,
      "used": 0,
      "remaining": 30,
      "reset": 1615234829
    },
    "graphql": {
      "limit": 5000,
      "used": 0,
      "remaining": 5000,
      "reset": 1615238369
    },
    "integration_manifest": {
      "limit": 5000,
      "used": 0,
      "remaining": 5000,
      "reset": 1615238369
    },
    "source_import": {
      "limit": 100,
      "used": 0,
      "remaining": 100,
      "reset": 1615234829
    },
    "code_scanning_upload": {
      "limit": 500,
      "used": 0,
      "remaining": 500,
      "reset": 1615238369
    }
  },
  "rate": {
    "limit": 5000,
    "used": 0,
    "remaining": 5000,
    "reset": 1615235630
  }
}
Let's try to use up some of those limits and see how they respond! To start with, we will do the next command four times unauthenticated, then check on the rate remaining. Feel free to put your own username in place of sgriffith3, that is just this lab author's GitHub username.

student@bchd:~/mycode/oauth$ curl https://api.github.com/users/sgriffith3/keys

Run this command four times.

Now, let's check to see how many requests you have remaining.

student@bchd:~/mycode/oauth$ curl https://api.github.com/rate_limit


...
  "rate": {
    "limit": 60,
    "remaining": 56,
    "reset": 1615234282,
    "used": 4
  }
}
Next, let's try to run the exact same curl command, except this time we will pass the Header for Authorization to the request, using our token. This time run this command seven times. Remember to paste your personal token in where it says <token>, and feel free to use your own username.

student@bchd:~/mycode/oauth$ curl -H "Authorization: token <token>" https://api.github.com/users/sgriffith3/keys

Run this command seven times.

Now we can see how many Authenticated requests we have left. Paste your personal token in where it says <token>.

student@bchd:~/mycode/oauth$ curl -H "Authorization: token <token>" https://api.github.com/rate_limit


...
  "rate": {
    "limit": 5000,
    "used": 7,
    "remaining": 4993,
    "reset": 1615235630
  }
}
Now that we have seen how to use cURL to authenticate with GitHub, let's attempt to do that with Python. The goal of these next several steps is to create a Python script that will let us list existing and create new repos on GitHub. Create the following file:

student@bchd:~/mycode/oauth$ vim repo_manager.py

Create the following script:


#!/usr/bin/env python3
"""GitHub Client - OAUth and API study | Alta3 Research"""

import json
import requests

MY_USERNAME = ""  # Make sure you put your own username in here!

def create_repo(repo_name: str, token: str) -> str:
    """
    This will create a repo for your GitHub account.
    """
    repo_data = {"name": repo_name}
    json_data = json.dumps(repo_data)
    headers = {"Authorization": f"token {token}"}
    r = requests.post(f"https://api.github.com/user/repos", data=json_data, headers=headers)
    response_code = r.status_code
    response = r.text
    print(response_code, response)
    return response

def show_repos(username: str, token: str) -> list:
    """
    This will list out all of the repos associated with your GitHub account.
    """
    url = f"https://api.github.com/users/{username}/repos"
    headers = {"Authorization": f"token {token}"}
    r = requests.get(url, headers=headers)
    resp_headers = r.headers
    print(f"""Rate - \n            Limit: {resp_headers['X-RateLimit-Limit']}
            Used: {resp_headers['X-RateLimit-Used']}
            Remaining: {resp_headers['X-RateLimit-Remaining']}""")
    repos = list(r.json())
    for repo in repos:
        print(repo['name'])
    return repos

def get_token() -> str:
    # Read token in from file
    with open("/home/student/token") as f:
        token = f.read().rstrip("\n")
        return token

if __name__ == "__main__":
    tkn = get_token()
    show_repos(MY_USERNAME, tkn)
    create_repo("learning_oauth", tkn)

Make sure that you edit line 6 to include YOUR GITHUB USERNAME!! Also, if you do not have the requests package installed, install it now python3 -m pip install requests.

Now we can run our repo_manager.py script. This will list all of our GitHub repos, then will create a new GitHub repo named learning_oauth for us.

student@bchd:~/mycode/oauth$ python3 repo_manager.py


Rate -
        Limit: 5000
        Used: 1
        Remaining: 4999
mycode-dev
Hooray! We just used our OAuth token to authenticate using our own 3rd Party Service (python script) with our Resource Server (GitHub) and perform the actions of listing and creating repositories!

If you're tracking your code in GitHub, issue the following commands:

cd ~/mycode
git add *
git commit -m "Exploring how to work with large data sets"
git push origin main
Type your username and password
Additional Reading
RFC 6749

The OAuth2.0 Authorization Framework

