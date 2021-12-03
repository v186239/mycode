Swagger
Appropriate API architecting is essential to designing an API that will be easily usable, quickly adopted, and resilient against future changes.

API Design Best Practice
Most modern APIs are designed to use HTTP as the protocol, so it is worth going over the most common HTTP methods that we can use.

CRUD	Method	Description
Create	POST	Create new resources
Read	GET	Retrieve a representation of a resource
Update	PUT	Update existing resources
Delete	DELETE	Delete existing resources
Developers like to use these HTTP Methods as verbs which make things happen on the resource paths. So best practice for designing a URL is to have it include nouns, such as /pets or /users. Then a developer can effectively say GET /users/<username> or DELETE /users/<username>. This allows the developer to use the HTTP Method as the directive on a specific resource and be very clear in what they are trying to do.

Another important aspect of a well designed API is to always have examples. That way a developer can very quickly understand what an appropriate HTTP request should look like, and also what the expected response would be.

Lab Objective
The objective of this lab is to learn to document APIs with Swagger. Swagger is a standard tool that is built with YAML (or JSON). If you've never studied YAML, then be sure to check out the YAML spec here: https://yaml.org/spec/1.2/spec.html

Swagger (v2) and OpenAPI (v3) are public tools free to use and licensed under the Apache 2.0 License. The source code is available here: https://github.com/swagger-api

Swagger also offers Swagger Hub, which you can use to explore Swagger, and document APIs. This tool also allows you to sign up for collaboration across organizations, which is a pay-to-use service.

If you want to read a detailed summary of Swagger Hub, check out the following: https://app.swaggerhub.com/help/

Procedure
Want a FREE personal swagger account? In your browser, navigate to https://swagger.io/. Then click on the top right where it says "Log In". This will give you the option to Log in with GitHub, SSO, or SwaggerHub sign-in. We suggest you use your GitHub login.

swagger_sign_in

Next you should be greeted by a page like this:

swagger_hub

Click on the CREATE API button. You will then see a screen like this:

swagger_create_api

Keep all of the settings as seen here, and give it your own name. Then click on the CREATE API button.

After a few seconds, you should see a new page pop up. The center will have an area to edit the swagger.yaml file which has the design of the API laid out for you. Let's start to dissect it a bit.

Lines 1 - 17: These lines describe the version and information of Swagger itself.


swagger: '2.0'
info:
  description: |
    This is a sample Petstore server.  You can find
    out more about Swagger at
    [http://swagger.io](http://swagger.io) or on
    [irc.freenode.net, #swagger](http://swagger.io/irc/).
  version: 1.0.0
  title: Swagger Petstore
  termsOfService: http://swagger.io/terms/
  contact:
    email: apiteam@swagger.io
  license:
    name: Apache 2.0
    url: http://www.apache.org/licenses/LICENSE-2.0.html
# host: petstore.swagger.io
# basePath: /v2
Lines 18 - 32: These lines describe tags that are being applied inside of your API. Think of these as labels that Swagger uses to group pieces of your API together. Read more about them here: https://swagger.io/docs/specification/grouping-operations-with-tags/


tags:
- name: pet
  description: Everything about your Pets
  externalDocs:
    description: Find out more
    url: http://swagger.io
- name: store
  description: Access to Petstore orders
- name: user
  description: Operations about user
  externalDocs:
    description: Find out more about our store
    url: http://swagger.io
# schemes:
# - http
Lines 33 - 561: These lines describe your paths. For obvious reasons, they are not all shown here. The /pet path has two optional HTTP Request methods: post and put. They each are tagged, have a summary, operationID, consumes, produces, parameters, responses, and security. Each of these will be discussed in depth further into this lab, but for right now, just read through this example to try to figure out for yourself what each one of these may be doing.


paths:
  /pet:
    post:
      tags:
      - pet
      summary: Add a new pet to the store
      operationId: addPet
      consumes:
      - application/json
      - application/xml
      produces:
      - application/json
      - application/xml
      parameters:
      - in: body
        name: body
        description: Pet object that needs to be added to the store
        required: true
        schema:
          $ref: '#/definitions/Pet'
      responses:
        405:
          description: Invalid input
      security:
      - petstore_auth:
        - write:pets
        - read:pets
    put:
      tags:
      - pet
      summary: Update an existing pet
      operationId: updatePet
      consumes:
      - application/json
      - application/xml
      produces:
      - application/json
      - application/xml
      parameters:
      - in: body
        name: body
        description: Pet object that needs to be added to the store
        required: true
        schema:
          $ref: '#/definitions/Pet'
      responses:
        400:
          description: Invalid ID supplied
        404:
          description: Pet not found
        405:
          description: Validation exception
      security:
      - petstore_auth:
        - write:pets
        - read:pets
      ...
Lines 562 - 573: This is where you define all authentication types that will be supported by the API. You then reference these using the security term in your paths to apply one or more specific authentication types to the individual paths. Read more about it here: https://swagger.io/docs/specification/2-0/authentication/


securityDefinitions:
  petstore_auth:
    type: oauth2
    authorizationUrl: http://petstore.swagger.io/oauth/dialog
    flow: implicit
    scopes:
      write:pets: modify pets in your account
      read:pets: read your pets
  api_key:
    type: apiKey
    name: api_key
    in: header
Lines 574 - 682: These definitions are where you define various objects that you will use throughout your API. Think of these like Python Classes, where these Objects each have attributes.


definitions:
  Pet:
    type: object
    required:
    - name
    - photoUrls
    properties:
      id:
        type: integer
        format: int64
      category:
        $ref: '#/definitions/Category'
      name:
        type: string
        example: doggie
      photoUrls:
        type: array
        xml:
          name: photoUrl
          wrapped: true
        items:
          type: string
      tags:
        type: array
        xml:
          name: tag
          wrapped: true
        items:
          $ref: '#/definitions/Tag'
      status:
        type: string
        description: pet status in the store
        enum:
        - available
        - pending
        - sold
    xml:
      name: Pet
Lines 693 - 701: These describe the externalDocs, which host this API is being served on, what the basePath is, as well as what schemes are available.


externalDocs:
  description: Find out more about Swagger
  url: http://swagger.io
# Added by API Auto Mocking Plugin
host: virtserver.swaggerhub.com
basePath: /sgriffith3/python_api_example/1.0.0
schemes:
 - https
 - http
If you are looking for some more details about the basic structure of Swagger API definitions, check out the documentation: https://swagger.io/docs/specification/2-0/basic-structure/

Now let's take a look over at the right hand side of the screen.

swagger_docs

Notice how the path of /pet has two nicely color-coded options of either performing a POST or a PUT command. These get generated from the YAML definition!

Click on the top POST /pet area. When you do this, it will expand and you will be able to see the Parameters and Responses, as well as the example data. NOW LOOK AT THE YAML DEFINITION (lines 34 - 59).

swagger_post_pet

All of this information was generated from your YAML definition.

On line 38, change the summary value to "Add another kitten, doggy, or fluffball to your store". After you do this, you should see that the summary for the POST has gotten updated on the right hand side.

swagger_update_summary

This proves that you can have the documentation get dynamically updated when you make a change to any portion of this API Definition!

Next we will make 3 clicks to have swagger generate a python flask server for you! At the top right, click Export -> Server Stub -> python-flask. See this picture for the flow of your clicks.

swagger_export_server

This will download a python flask server for you. All you have to do now is read through the README.md file, and follow the steps therein to start your server.

Nothing is perfect, and unfortunately this includes their code as well. It is a little bit busted and requires a few tweaks. Thankfully we have a working version ready to go for you. So let's download the working code now.

student@bchd:~$ wget https://static.alta3.com/courses/python/swagger_flask_petstore.tar

Next up we will need to unpack this little tarball.

student@bchd:~$ tar -xvf swagger_flask_petstore.tar

Move into the swagger_flask_petstore directory.

student@bchd:~$ cd swagger_petstore_flask

Perform a pip install of all of our requirements.

student@bchd:~/swagger_petstore_flask$ python3 -m pip install -r requirements.txt

If you have run the pandas lab, you may see an error with one of the requirements versions. As long as the one installed is newer than the requirements.txt asks for, it should be okay.

Now start up your server by calling on the module's name.

student@bchd:~/swagger_petstore_flask$ python3 -m swagger_server

Open up your aux1 terminal and append the following to your URI.

/alta3/python_api_example/1.0.0/ui/

You should be greeted by the following screen

swagger_local


