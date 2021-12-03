# API Design Best Practice
Most modern APIs are designed to use HTTP as the protocol, so it is worth going over the most common HTTP methods that we can use.

CRUD	Method	Description
Create	POST	Create new resources
Read	GET	Retrieve a representation of a resource
Update	PUT	Update existing resources
Delete	DELETE	Delete existing resources
Developers like to use these HTTP Methods as verbs which make things happen on the resource paths. So best practice for designing a URL is to have it include nouns, such as /pets or /users. Then a developer can effectively say GET /users/<username> or DELETE /users/<username>. This allows the developer to use the HTTP Method as the directive on a specific resource and be very clear in what they are trying to do.

Another important aspect of a well designed API is to always have examples. That way a developer can very quickly understand what an appropriate HTTP request should look like, and also what the expected response would be.

Goals
Use SwaggerHub to design our API
Create an API that allows us to Create, Read, Update, and Delete items from a restaurant menu
Show how to use the aiohttp framework
Show how to make database calls using aiosqlite
Procedure
In your browser, navigate to https://swagger.io/. Then click on the top right where it says "Log In". This will give you the option to Log in with GitHub, SSO, or SwaggerHub sign-in. We suggest you use your GitHub login.

swagger_sign_in

Next you should be greeted by a page like this:

swagger_hub

Click on the CREATE API button. You will then see a screen like this:

swagger_create_api

Keep all of the settings as seen here, and give it your own name. Then click on the CREATE API button.

After a few seconds, you should see a new page pop up. The center will have an area to edit the swagger.yaml file which has the design of the API laid out for you. Let's remove all of the YAML text.

DELETE THE YAML CONTENTS

Now we will add in our data. First, add in some meta information about this API. PLEASE MAKE SURE YOU UPDATE YOUR email FIELD.


openapi: 3.0.0
servers:
  # Added by API Auto Mocking Plugin
  - description: SwaggerHub API Auto Mocking
    url: https://virtserver.swaggerhub.com/sgriffith3/student-flask-api/1.0.0
info:
  description: This is a menu microservice API
  version: "1.0.0"
  title: Menu Microservice API
  contact:
    # Put your email here!
    email: <me@email.com>
  license:
    name: Apache 2.0
    url: 'http://www.apache.org/licenses/LICENSE-2.0.html'
tags:
  - name: developers
    description: Operations available to regular developers
Just after that, let's add a POST method to our API. This acts as our Create portion of our CRUD operations.


paths:
  # curl -x POST myserver.com/menu ...
  /menu:  
    post:
      tags:
        - developers
      summary: adds an inventory item
      operationId: addInventory
      description: Adds an item to the system
      responses:
        '201':
          description: item created
        '400':
          description: 'invalid input, object invalid'
        '404':
          description: page not found
        '409':
          description: an existing item already exists
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/MenuItem'
        description: Inventory item to add
      ```



After this, add in the GET method for the /menu path. This acts as the Read portion of our CRUD operations.


    # perform a GET request
    get:
      # any special tags we may want to group methods together
      tags:
        - developers
      summary: searches menu
      operationId: get_menu
      description: |
        By passing in the appropriate options, you can search for
        available menu items in the system
      # options that must/may be included in the query string
      parameters:
        - in: query
          name: searchString
          description: pass an optional search string for looking up inventory
          required: false
          schema:
            type: string
      responses:
        # available HTTP responses
        '200':  # 200 == OK
          description: search results matching criteria
          # what the body of the response will look like
          content:
            # specifies the format will be JSON
            application/json:
              schema:
                type: array
                # structure of the data being returned
                items:
                  $ref: '#/components/schemas/MenuItem'
        '400':  # 400 == Bad Request
          description: bad input parameter
Next we will need to allow our users a way to Update the existing resources. So let's add in a PUT method.


    put:
      tags:
      - developers
      summary: updates a menu item
      operationId: updateMenu
      responses:
        '200':
          description: item updated
        '400':
          description: invalid object
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/MenuItem'
        description: Menu item to update
And finally, we should give our users a way to remove entries from the menu, so we will add in a DELETE method.


    delete:
      tags:
      - developers
      summary: removes a menu item
      operationId: delete_item
      responses:
        '200':
          description: item deleted
        '400':
          description: invalid object
      parameters:
        - in: query
          name: item
          description: pass a string of the item to be deleted
          required: true
          schema:
            type: string   
          example: ?item=Kung%20Pao%20Beef
And finally, we will need to create a definition of our MenuItem schema that we have used already in our put and post methods.


components:
  schemas:
    MenuItem:
      type: object
      required:
        - item
        - description
        - price
      properties:
        item:
          type: string
          example: Kung Pao Chicken
        description:
          type: string
          example: Yummy chicken ready to karate kick your tongue
        price:
          type: number
          example: 12.99
Create the directory called menu_api.

student@bchd:~$ cd /home/student/mycode && mkdir -p menu_api

Download the following bash script to help you install python3.8:

student@bchd:~/mycode$ wget https://static.alta3.com/courses/microservices/py38.sh && bash py38.sh

Next, let's create a requirements.txt file for our python scripts.

student@bchd:~/mycode$ vim menu_api/requirements.txt


aiohttp
aiosqlite
Now let's make sure that all of our required third party packages get installed.

student@bchd:~/mycode$ python3.8 -m pip install -r menu_api/requirements.txt

First, let's create an admin task as a one-off process. This script will allow us to create the initial database and table called menu. Check out the 12 Factor App to learn about microservice application best practices.

student@bchd:~/mycode$ vim menu_api/db_create.py


import aiosqlite
import asyncio
import os

DB_FILE = os.getenv("DB_FILE", "menu.db")

async def create_menu() -> bool:
    """
    This will create the menu table in the DB_FILE
    """
    async with aiosqlite.connect(DB_FILE) as db:
        sql = "CREATE TABLE IF NOT EXISTS MENU (item CHAR(50), description CHAR(250), price REAL);"
        await db.execute(sql)
    return True


if __name__ == "__main__":
    asyncio.run(create_menu())
Let's create the database now by running our script.

student@bchd:~/mycode$ python3.8 menu_api/db_create.py

Now we will need to create our python code to serve actually host our API that will interact with the database.

student@bchd:~/mycode$ vim menu_api/menu.py


import json
import os

from aiohttp import web
import aiosqlite

HOST = os.getenv("MENU_HOST", "0.0.0.0")
PORT = os.getenv("MENU_PORT", 2227)
DB_FILE = os.getenv("DB_FILE", "menu.db")


def routes(app: web.Application) -> None:
    """
    These are the paths that may be appended to the URL.
    Each one has a Request type
    (get == GET, post == POST, put == PUT, delete == DELETE)
    and a different function is called for each type of request
    """

    app.add_routes(
        [
            web.get("/", menu),
            web.get("/menu", menu),
            web.put("/menu", update_menu),
            web.post("/menu", add_item),
            web.delete("/menu", delete_item)
        ]
    )


async def read_menu(search_item=None):
    """Read all of the information from the menu table of the database and return it as an iterable"""
    async with aiosqlite.connect(DB_FILE) as db:
        if search_item:
            sql = f"SELECT * FROM menu where item like '{search_item}'"
        else:
            sql = f"SELECT * FROM menu"
        data = await db.execute(sql)
        return await data.fetchall()


async def menu(request) -> json:
    """
    This will select everything from the menu table in the DB_FILE and return a JSON based web response
    """
    print(request)
    search = request.query.get('item')
    print(search)
    data = await read_menu(search)
    foods = []
    for food in data:
        foods.append({"item": food[0], "description": food[1], "price": food[2]})
    return web.json_response(foods)

async def add_item(request: web.Request) -> web.Response:
    print(request)
    post = await request.json()
    print(post)
    item = post['item']
    desc = post['description']
    price = post['price']
    sql = f"INSERT INTO MENU (item, description, price) VALUES ('{item}', '{desc}', {price});"
    async with aiosqlite.connect(DB_FILE) as db:
        await db.execute(sql)
        await db.commit()
        return web.Response(body="Successfully Updated the Database")


async def update_menu(request: web.Request) -> web.Response:
    print(request)
    put = await request.json()
    print(put)
    item = put['item']
    desc = put['description']
    price = put['price']
    data = await read_menu()
    sql = ""
    for row in data:
        print(row)
        if item == row[0]:
            # If this item already exists, update the description and price
            sql = f"UPDATE MENU SET description = '{desc}', price = {price} where item like '{item}';"
        elif desc == row[1]:
            # If the description matches exactly, update the item name and the price
            sql = f"UPDATE MENU SET item = '{item}', price = {price} where description like '{desc}';"
        else:
            # If the item and desc do not exist, this is a new item to be added to the database
            sql = f"INSERT INTO MENU (item, description, price) VALUES ('{item}', '{desc}', {price});"
    if sql != "":
        async with aiosqlite.connect(DB_FILE) as db:
            await db.execute(sql)
            await db.commit()
            return web.Response(body="Successfully Updated the Database")

async def delete_item(request: web.Request) -> web.Response:
    """
    This function will read the 'item' query string and attempt to
    DELETE the value from the database
    """
    item = request.query.get('item')
    print(f"Trying to delete {item}")
    sql = f"DELETE FROM MENU WHERE item = '{item}'"
    async with aiosqlite.connect(DB_FILE) as db:
        await db.execute(sql)
        await db.commit()
        return web.Response(body=f"Successfully Deleted {item} from the database")


def main():
    """
    This is the main process for the aiohttp server.

    This works by instantiating the app as a web.Application(),
    then applying the setup function we built in our routes
    function to add routes to our app, then by starting the async
    event loop with web.run_app().
    """

    print("This aiohttp web server is starting up!")
    app = web.Application()
    routes(app)
    web.run_app(app, host=HOST, port=PORT)


if __name__ == "__main__":
    main()

Now it is time to run the web application.

student@bchd:~/mycode$ python3.8 menu_api/menu.py

Open (or switch to) another TMUX pane

Ctrl b %

Perform a GET request against our API.

student@bchd:~/mycode$ curl localhost:2227/menu

This should currently be a blank list as a response. We have not added anything into our menu yet.

Let's add in some data to our menu using curl now. Note that the flag -X allows us to select which HTTP Method we wish to use (POST in this case), and the flag -d allows us to pass data in.

student@bchd:~/mycode$ curl -X POST -d '{"item": "Kung Pao Shrimp", "description": "Tasty shrimp ready to kick", "price": 9.88}' localhost:2227/menu


Successfully Updated the Database
And we should verify that our shrimp was in fact added in.

student@bchd:~/mycode$ curl localhost:2227/menu


[{"item": "Kung Pao Shrimp", "description": "Tasty shrimp ready to kick", "price": 9.88}]
Excellent! Let's add some chicken to our menu too!

student@bchd:~/mycode$ curl -X POST -d '{"item": "Teriyaki Chicken", "description": "Best chicken ever!", "price": 11.99}' localhost:2227/menu


Successfully Updated the Database
And we should also verify that our chicken and shrimp are both in the menu database now.

student@bchd:~/mycode$ curl localhost:2227/menu


[{"item": "Kung Pao Shrimp", "description": "Tasty shrimp ready to kick", "price": 9.88}, {"item": "Teriyaki Chicken", "description": "Best chicken ever!", "price": 11.99}]
Let's pretend we are now having a sale. The chicken price has been discounted to $10.01 for national palindrome day. We want to update the price without changing anything else about the item, so we can use a PUT Request.

student@bchd:~/mycode$ curl -X PUT -d '{"item": "Teriyaki Chicken", "description": "Best chicken ever!", "price": 10.01}' localhost:2227/menu


Successfully Updated the Database
Verify that the chicken price has been updated now.

student@bchd:~/mycode$ curl localhost:2227/menu


[{"item": "Kung Pao Shrimp", "description": "Tasty shrimp ready to kick", "price": 9.88}, {"item": "Teriyaki Chicken", "description": "Best chicken ever!", "price": 10.01}]
Next let's pretend that our restaurant has been badly hurt by a national shrimp shortage, and we can no longer sell our Kung Pao Shrimp. We need to remove it (DELETE) from the menu.

student@bchd:~/mycode$ curl -X DELETE localhost:2227/menu?item=Kung%20Pao%20Shrimp

Note that any space characters in a URL must be turned into a %20


Successfully Deleted Kung Pao Shrimp from the databas
Now let's verify that the shrimp has been removed from the menu.

student@bchd:~/mycode$ curl localhost:2227/menu


[{"item": "Teriyaki Chicken", "description": "Best chicken ever!", "price": 10.01}]
Awesome work!

You have just designed an API using SwaggerHub (OpenAPI Specifications) and created the code that actually is the API! Way to go!


