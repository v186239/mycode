etcd and RESTful Client-side Design
Lab Objective
Our objective is to explore RESTful API interfaces with Python. REST stands for Representational State Transfer (it is sometimes spelled "REST", or "RESTful"). It relies on a stateless, client-server, cacheable communications protocol -- and in virtually all cases, the HTTP protocol is used (although this is not a requirement). REST is an architecture style for designing networked applications.

In computer programming, an application programming interface (API) is a set of subroutine definitions, protocols, and tools for building application software. A good API makes it easier to develop a computer program by providing all the building blocks, which are then put together by the programmer.

In this lab we'll use etcd. The tool etcd is remarkable in that it works as a keystore that can be serviced with HTTP requests. It can be run in HA mode, and used to store critical information in an easy-to-access manner.

Procedure
Create a directory to work in.

student@bchd:~$ mkdir -p ~/mycode/etcdstore/

Let's first install etcd on the machine

student@bchd:~$ sudo apt install etcd -y

Ensure that etcd is running on the machine.

student@bchd:~$ sudo service etcd status

press q to quit

Now let's test the etcd api with the curl command. First we'll try getting the etcd version. The -L flag means follow any redirection (3xx responses).

student@bchd:~$ curl -L http://127.0.0.1:2379/version


{"etcdserver":"3.2.17","etcdcluster":"3.2.0"}
Now let's place a key-value pair in etcd using curl and a PUT.

student@bchd:~$ curl http://127.0.0.1:2379/v2/keys/message -XPUT -d value="Hello world"


{"action":"set","node":{"key":"/message","value":"Hello world","modifiedIndex":4,"createdIndex":4}}
Try getting a key-value pair.

student@bchd:~$ curl http://127.0.0.1:2379/v2/keys/message


{"action":"get","node":{"key":"/message","value":"Hello world","modifiedIndex":4,"createdIndex":4}}
Now let's remove the key-value pair.

student@bchd:~$ curl http://127.0.0.1:2379/v2/keys/message -XDELETE


{"action":"delete","node":{"key":"/message","modifiedIndex":5,"createdIndex":4},"prevNode":{"key":"/message","value":"Hello world","modifiedIndex":4,"createdIndex":4}}
So we just deleted the key-value pair, and now we'll try to retrieve it. This should produce an error errorCode:100 message error expected.

student@bchd:~$ curl http://127.0.0.1:2379/v2/keys/message


{"errorCode":100,"message":"Key not found","cause":"/message","index":5}
Let's create a Python script that can interact with etcd.

student@bchd:~$ vim ~/mycode/etcdstore/etcd01.py

Create the following script:


#!/usr/bin/python3

import requests
import pprint

def main():

    # issue an HTTP PUT transaction to store our data within /keys/requests
    # in this case, PUT created a 'file' called '/requests', with a 'value' of 'http for humans'
    # r is the response code resulting from the PUT
    r = requests.put("http://127.0.0.1:2379/v2/keys/requests", data={'value': 'http for humans'})
    print(f"Status Code - {r.status_code}") # return the status code associated with object r
    # pretty print the json in the response
    pprint.pprint(r.json())

    print('******')

    # issue an HTTP PUT transaction to store our data within /keys/requests
    # in this case, PUT updated a 'file' called '/requests', with a 'value' of 'http for humans'
    # r is the response code resulting from the PUT
    r = requests.put("http://127.0.0.1:2379/v2/keys/requests", data={'value': 'http for humans, version 2'})
    print(f"Status Code - {r.status_code}") # return the status code associated with object r
    # pretty print the json in the response
    pprint.pprint(r.json())

    print('******')

    # issue an HTTP GET to our keys/requests
    r = requests.get("http://127.0.0.1:2379/v2/keys/requests")
    print(f"Status Code - {r.status_code}") # return the status code associated with object r
    # pretty print the json in the response
    pprint.pprint(r.json())

if __name__ == "__main__":
    main()
Save and exit with :wq

Run your script.

student@bchd:~$ python3 ~/mycode/etcdstore/etcd01.py

Cool! So the top two blocks placed a key in the etcd keystore, where the last one performed a GET on our key.

Try modifying what is PUT to the etcd keystore. There are other HTTP primitives to try out as well.

Now let's write a Python RESTful client to connect to etcd, which will mimic a ticketing system. If you'd like, you can try this script yourself before copying the solution. The objectives are to use HTTP to perform the following RESTful operations:

Objective 1 - A user can query for all tickets. GET /tickets/
Objective 2 - A user can retrieve a ticket (GET) GET /tickets/{ticketid}
Objective 3 - A user can create a ticket POST /tickets/ will generate a new /tickets/{ticketid}
Objective 4 - A user can update a ticket PUT /tickets/{ticketid}
Objective 5 - A user can delete a ticket DELETE /tickets/{ticketid}
Objective 6 - A user can exit the application.
Objective 7 - A user can delete the entire collection DELETE /tickets/?dir=true&recursive=true
Create a script for our ticketing application.

student@bchd:~$ vim ~/mycode/etcdstore/etcdTicketApp.py

Create the following application:


#!/usr/bin/python3
"""Russell Zachary Feeser Using etcd to design a RESTful ticket server"""

import requests

ETCD = "http://127.0.0.1:2379/v2/keys/tickets"

## read all available tickets
## use a GET on a directory to return all results
def gettickets():
    resp = requests.get(ETCD)
    resp = resp.json()
    # if the resp dict contains an errorCode
    if resp.get("errorCode"):
        return False
    # if no errorCode assume there are tickets in system
    else:
        ticketlist = []
        ## if someone manually deletes all entries from the directory /tickets/
        ## then it will still test true (no errorCode), but won't have entry for "nodes"
        if resp.get("node").get("nodes"):
        ## after studying resp dict, resp["node"]["nodes"] appears to be a list
        ## of ticket entries. We cycle through this
            for ticket in resp.get("node").get("nodes"):
                ## add a ticket number to ticketlist
                ticketlist.append(ticket.get("key").lstrip("/tickets/"))
            return ticketlist
        else:
            return False


## get a specific ticket
## pass in the ticket to GET
def getoneticket(ticketid):
    resp = requests.get(f"{ETCD}/{ticketid}")
    resp = resp.json()
    ## if a key called errorCode is returned in the JSON
    if resp.get("errorCode"):
        # return false
        return False
    else:
        # return the VALUE associated with they KEY called 'value'
        return resp.get("node").get("value")


## create a ticket
## use a POST to create a new resource
def createticket(descofissue):
   ## sending a POST to the base URL will create a new /tickets/{ID}
   resp = requests.post(ETCD, data={'value': descofissue })
   resp = resp.json()
   ## take resp["node"]["key"].lstrip("/tickets/") which is the ticketID
   resp = resp.get("node").get("key").lstrip("/tickets/")
   return resp

## update a ticket
## pass in the ticket to PUT
def updateticket(ticketid, descofissue):
    ## first test to see if that ticket exists
    ## invoke the function getoneticket(ticketid) to test
    ## this returns a FALSE if the ticket returns and error code
    if getoneticket(ticketid):
        ## assuming getoneticket returns a value that tests TRUE
        ## the code will not issue a PUT to alter /tickets/{ticketid}
        resp = requests.put(f"{ETCD}/{ticketid}", data={'value': descofissue })
        resp = resp.json()
    else:
        return False
    ## return a tuple of (new value, old value)
    return (resp.get("node").get("value"), resp.get("prevNode").get("value"))

## delete a ticket
## pass in the ticket to DELETE
def deleteticket(ticketid):
    requests.delete(f"{ETCD}/{ticketid}")
    return

## delete ALL tickets
## use the api parameter ?dir=true&recursive=true to remove a directory
def deletealltickets():
    requests.delete(f"{ETCD}?dir=true&recursive=true")
    return

def main():

    ## Enter a while true loop (run until a break condition)
    while True:

        ## pop up a menu
        print("""
        1) Read all available tickets
        2) Get ticket
        3) Create ticket
        4) Update ticket
        5) Delete ticket
        6) Exit
        99) DANGER! Delete all tickets
        """)

        ## collect input from user
        userinput = ""
        while userinput == "":
            userinput = input("> ")

        ## user wants ALL available tickets
        if userinput == "1":
            ## getickets() returns a list or FALSE
            ticketlist = gettickets()
            ## Test what was ticketlist?
            if ticketlist:
                print()
                for ticket in ticketlist:
                    print(f"Ticket ID - {ticket}")
            else:  ## if ticketlist() returned FALSE
                print("There are no tickets in the system")

        ## user wants info on a single ticket
        elif userinput == "2":
            ticketid = input("What is the ticket ID? ")
            oneticket = getoneticket(ticketid)
            # if oneticket returns a string or FALSE
            if oneticket:
                print(f"\nFor {ticketid}:")
                print(f"    Ticket Description - {oneticket}")
            ## handles condition where FALSE is returned
            else:
                print("That ticket does not exist within the system.")

        ## user wants to create a ticket
        elif userinput == "3":
            descofissue = input("Give a short 140 char description of the issue: ")
            createdticket = createticket(descofissue)
            print(f"\nTicket {createdticket} has been created.")

        ## user wants to update a ticket
        elif userinput == "4":
            ticketid = input("Update what ticket ID? ")
            descofissue = input("What is the updated 140 char description of the issue: ")
            ## updatedticket returns a two-tuple, or FALSE
            updatedticket = updateticket(ticketid, descofissue)
            if updatedticket:
                print(f"\nFor {ticketid}:")
                print(f"    Updated Ticket Description - {updatedticket[0]}")
                print(f"    Old Ticket Description - {updatedticket[1]}")
            else: ## if updatedticket() returned FALSE
                print("That ticket does not exist within the system.")

        ## user wants to delete a ticket
        elif userinput == "5":
            ticketid = input("What is the ticket ID? ")
            deleteticket(ticketid)
            print(f"\nTicket {ticketid} has been removed from the system")

        ## user wants to exit
        elif userinput == "6":
            ## end the while True loop
            break

        elif userinput == "99":
            deletealltickets()
            print("All tickets have been removed from the system")

        ## user inputs a non valid option
        else:
            print("That is not a valid option")

    print("Thanks for using the Alta3 RESTful ticketing service")

if __name__ == "__main__":
    main()
Save and exit with :wq

Execute your code.

student@bchd:~$ python3 ~/mycode/etcdstore/etcdTicketApp.py

Try playing with the application. Let the instructor know if you find any errors or have any issues understanding how it works.

Next, let's turn this into a real API.

student@bchd:~$ vim ~/mycode/etcdstore/etcd_api.py


from flask import Flask, request
import requests

app = Flask(__name__)

ETCD = "http://127.0.0.1:2379/v2/keys/tickets"


# READ (return all of the tickets)
@app.route("/tickets", methods=["GET"])
def get_tickets():
    resp = requests.get(ETCD)
    resp = resp.json()
    # if the resp dict contains an errorCode
    if resp.get("errorCode"):
        return {"msg": f"Error Code: {resp['errorCode']}"}
    # if no errorCode assume there are tickets in system
    else:
        all_tickets = []
        # If someone manually deletes all entries from the directory /tickets/
        # then it will still test true (no errorCode), but won't have entry for "nodes"
        if resp.get("node").get("nodes"):
            # after studying resp dict, resp["node"]["nodes"] appears to be a list
            # of ticket entries. We cycle through this
            for ticket in resp.get("node").get("nodes"):
                # add a ticket number to all_tickets
                all_tickets.append(ticket.get("key").lstrip("/tickets/"))
            return {"tickets": all_tickets}
        else:
            return {"msg": "No Tickets Found! Good Work!"}


# READ (return a specified ticket)
@app.route("/tickets/<ticket_id>")
def get_one_ticket(ticket_id):
    resp = requests.get(f"{ETCD}/{ticket_id}")
    resp = resp.json()
    # if a key called errorCode is returned in the JSON
    if resp.get("errorCode"):
        # return false
        return {"msg": "Ticket Not Found"}
    else:
        # return the VALUE associated with they KEY called 'value'
        print(resp)
        return resp.get("node").get("value")


# CREATE (use POST to create a new ticket resource)
@app.route("/tickets", methods=["POST"])
def create_ticket():
    data = request.json
    print(data)
    value = data["value"]
    # sending a POST to the base URL will create a new /tickets/{ID}
    resp = requests.post(ETCD, data={"value": value})
    resp = resp.json()
    resp = resp.get("node").get("key").lstrip("/tickets/")
    return resp


# UPDATE (PUT the ticket's new info in place)
@app.route("/tickets", methods=["PUT"])
def update_ticket():
    # first test to see if that ticket exists
    data = request.json
    ticket_id = data["ticket_id"]
    msg = data["msg"]
    print(data)
    print(ticket_id)
    print(msg)
    if get_one_ticket(ticket_id):
        # assuming get_one_ticket returns a value that tests TRUE
        # the code will now issue a PUT to alter /tickets/{ticket_id}
        resp = requests.put(f"{ETCD}/{ticket_id}", data={'value': msg})
        resp = resp.json()
    else:
        return {"msg": f"Unable to update ticket # {ticket_id}"}
    # return a tuple of (new value, old value)
    return resp.get("node").get("value"), resp.get("prevNode").get("value")


# DELETE (remove a specified ticket resource)
@app.route("/tickets", methods=["DELETE"])
def delete_ticket():
    ticket_id = request.args.get("ticket_id")
    if ticket_id:
        requests.delete(f"{ETCD}/{ticket_id}")
        return f"The following ticket was deleted: {ticket_id}"
    else:
        return f"Unable to delete the ticket"


# DELETE (remove ALL ticket resources)
@app.route("/remove_all_tickets", methods=["DELETE"])
def delete_all_tickets():
    requests.delete(f"{ETCD}?dir=true&recursive=true")
    return {"msg": "You just removed everything. I hope you are happy now"}


if __name__ == "__main__":
    app.run(debug=True, port=2224, host="0.0.0.0")
Start up your etcd ticket API now!

student@bchd:~$ python3 ~/mycode/etcdstore/etcd_api.py

Open (or switch to) another TMUX pane.

Ctrl b "

Now let's try some curl commands against our API. First, a GET.

student@bchd:~$ curl localhost:2224/tickets


{
  "msg": "Error Code: 100"
}
Notice that we got an error code? That is because we don't have any tickets in there right now!

Let's add a ticket in. NOTE: Your ticket numbers may be different than the resultes posted.

student@bchd:~$ curl localhost:2224/tickets -X POST -H "Content-Type: application/json" -d '{"value": "Learning to add tickets"}'


00000000000000000010
Let's verify that it was added in.

student@bchd:~$ curl localhost:2224/tickets


{
  "tickets": [
    "00000000000000000010"
  ]
}
How about we add in a few more for fun?

student@bchd:~$ curl localhost:2224/tickets -X POST -H "Content-Type: application/json" -d '{"value": "Added my second ticket"}'


00000000000000000011
student@bchd:~$ curl localhost:2224/tickets -X POST -H "Content-Type: application/json" -d '{"value": "This is my third ticket"}'


00000000000000000012
GET all of your tickets again.

student@bchd:~$ curl localhost:2224/tickets


{
  "tickets": [
    "00000000000000000010",
    "00000000000000000011",
    "00000000000000000012"
  ]
}
Next let's update the value of the last ticket we created. For this, you will need your most recent ticket_id (This may be different than the command shown), as well as a new message to send in.

student@bchd:~$ curl localhost:2224/tickets -X PUT -H "Content-Type: application/json" -d '{"msg": "PUT it there!", "ticket_id": "00000000000000000012"}'


PUT it there!
Make sure that the ticket has been updated appropriately. (The ticket_id may be different than the command shown)

student@bchd:~$ curl localhost:2224/tickets/00000000000000000012


PUT it there!
Excellent! Now, we just have to try using the DELETE method. (The ticket_id may be different than the command shown)

student@bchd:~$ curl localhost:2224/tickets?ticket_id=00000000000000000012 -X DELETE


The following ticket was deleted: 00000000000000000012
GET all of your tickets again to make sure the last one was deleted.

student@bchd:~$ curl localhost:2224/tickets


{
  "tickets": [
    "00000000000000000010",
    "00000000000000000011"
  ]
}
Finally, remove ALL of the tickets.

student@bchd:~$ curl localhost:2224/remove_all_tickets -X DELETE


{
    "msg": "You just removed everything. I hope you are happy now"
}
And verify that they all are gone.

student@bchd:~$ curl localhost:2224/tickets


{
  "msg": "Error Code: 100"
}
Challenge! Use SwaggerHub to create an OpenAPI specification describing the API that we just built. Make sure to include all of the paths and methods we specified, as well as the examples we just ran through. This is an all too common occurence, where code gets built before it gets planned out thoroughly, so this is a very realistic task.

If you're tracking your code in GitHub, issue the following commands:

cd ~/mycode
git add *
git commit -m "etcd and RESTful APIs"
git push origin main

