# Started with Django
Lab Objective
The objective of this lab is to explore another web-framework, Django. Per the Django Project homepage, "Django is a high-level Python Web framework that encourages rapid development and clean, pragmatic design. Built by experienced developers, it takes care of much of the hassle of Web development, so you can focus on writing your app."

Django is a full-stack web framework for Python, whereas Flask is a lightweight and extensible Python web framework. Django's batteries-included approach enable programmers to accomplish common web development tasks without using third-party tools and libraries. Django makes it easier for Django developers to accomplish common web development tasks like user authentication, URL routing and database schema migration. Also, Django accelerates custom web application development by providing built-in template engine, ORM system, and bootstrapping tool. However, Django lacks some of the robust features provided by Python.

On the other hand, Flask is a lightweight, minimalist web framework. It lacks some of the built-in features provided by Django, but it helps Python developers to keep the core of a web application simple and extensible.

Still confused? Cars have automatic or standard transmissions. If you find the less-is-more approach to driving with an automatic transmission appealing, Django might be for you. If you feel more in control with a gearbox and clutch, than Flask might be your go to framework. There is not really a right or wrong argument to be had, as much as which solution works best for your brain.

Read more about the Django project here: https://www.djangoproject.com/

Django uses a modeling style called MVT (Model, View, Template). Read more about these concepts here:

Model: https://docs.djangoproject.com/en/2.2/topics/templates/

Procedure
Within a terminal space, move into your home directory.

Now we need to install Django

student@bchd:~$ python3 -m pip install django

Check your version using django-admin.

student@bchd:~$ django-admin --version

The first time using Django, it is required to auto-generate some code that establishes a Django project. A project is, effectively, a collection of settings for an instance of Django, including database configuration, Django-specific options and application-specific settings. This is completed with a django-admin utility. Type the following to create a new project fifthelement

student@bchd:~$ django-admin startproject fifthelement

Locally, fifthelement/ was created.

student@bchd:~$ ls

Let us use tree to explore it. To be clear, tree has nothing to do with Django. It is just a tool for exploring directory structures.

student@bchd:~$ sudo apt install tree

Run tree against your new directory.

student@bchd:~$ tree fifthelement


fifthelement/
 - fifthelement
     - __init__.py
     - settings.py
     - urls.py
     - wsgi.py
 - manage.py
The files the tree utility exposed are:

The outer fifthelement/ root directory is just a container for your project. Its name doesn’t matter to Django; you can rename it to anything you like.
manage.py - A command-line utility that lets you interact with this Django project in various ways. You can read all the details about manage.py in django-admin and manage.py
The inner fifthelement/ directory is the actual Python package for your project. Its name is the Python package name you’ll need to use to import anything inside it (e.g. fifthelement.urls).
fifthelement/__init__.py - An empty file that tells Python that this directory should be considered a Python package. If you’re a Python beginner, read more about packages in the official Python docs.
fifthelement/settings.py - Settings/configuration for this Django project. Django settings will tell you all about how settings work.
fifthelement/urls.py - The URL declarations for this Django project; a “table of contents” of your Django-powered site. You can read more about URLs in URL dispatcher.
fifthelement/wsgi.py - An entry-point for WSGI-compatible web servers to serve your project. See How to deploy with WSGI for more details.
Lets explore the development server we just spawned. Move into the directory, fifthelement/

student@bchd:~$ cd fifthelement/

Verify your Django project works. Change into the outer fifthelement/ directory, then run the following command to launch your server.

student@bchd:~/fifthelement$ python3 manage.py runserver

Split your screen with tmux with the following two commands

CTRL + b (press both keys at the same time)
" (you will need to use the SHIFT key)
In your new screen, try to curl against your webserver (by default Django runs on port 8000)

student@bchd:~/fifthelement$ curl http://localhost:8000/

You should get back something like, "Congratulations!" along with some other HTML data suitable for rendering in a browser.

Close your split-screen by typing exit in your current split-screen.

student@bchd:~/fifthelement$ exit

Within the window hosting your Django server, stop the server with CTRL + c

If you want to change the server’s port, pass it as a command-line argument. For instance, start on port 8080.

student@bchd:~/fifthelement$ python3 manage.py runserver 8080

Notice the service is now listening on port 8080.

Stop your Django server with CTRL + c

If you want to change the server’s IP, pass it along with the port. For example, to listen on all available public IPs (which is useful if you are running Vagrant or want to show off your work on other computers on the network), use:

student@bchd:~/fifthelement$ python3 manage.py runserver 0:8000

Stop your Django server with CTRL + c

Now that your environment – a "project" – is set up, you’re set to start doing work. Each application you write in Django consists of a Python package that follows a certain convention. Django comes with a utility that automatically generates the basic directory structure of an app, so you can focus on writing code rather than creating directories.

Confused by the new terms "project" and "app"? An app is a web application that does something – e.g., a Weblog system, a database of public records or a simple poll app. A project is a collection of configuration and apps for a particular website. A project can contain multiple apps. An app can be in multiple projects.

Issue the following command to create a directory, polls/, for our app:

student@bchd:~/fifthelement$ python3 manage.py startapp polls

Run tree on the new directory to get a visual:

tree polls/


polls/
- __init__.py
- admin.py
- apps.py
- migrations
    - __init__.py
- models.py
- tests.py
- views.py
The above structure will house our poll application.

Lets write our first "view". Run the following command to edit polls/views.py

student@bchd:~/fifthelement$ vim polls/views.py

Create the following code:


from django.http import HttpResponse

def index(request):
   return HttpResponse("Hello, world. You are at the polls index.")
Save and exit with :wq

We made an incredibly simple 'view'. To call it, we'll need to first map it to a URL, which is done in URLconf. For whatever reason, django-admin doesn't make this file, so we'll need to create a file called, polls/urls.py

student@bchd:~/fifthelement$ vim polls/urls.py

Create the following code within polls/urls.py


from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
]
Save and exit with :wq

The next step is to point the root URLconf at the polls.urls module. Edit fifthelement/urls.py

student@bchd:~/fifthelement$ vim fifthelement/urls.py

Add an import for django.urls.include, and insert an include() in the urlpatterns list, so you have:


from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("polls/", include("polls.urls")),
    path("admin/", admin.site.urls),
]
Save and exit with :wq

The include() function allows referencing other URLconfs. Whenever Django encounters include(), it chops off whatever part of the URL matched up to that point and sends the remaining string to the included URLconf for further processing.

The idea behind include() is to make it easy to plug-and-play URLs. Since polls are in their own URLconf (polls/urls.py), they can be placed under /polls/, or under /fun_polls/, or under /content/polls/, or any other path root, and the app will still work.

You've now wired an index view into the URLconf. Verify it is working.

student@bchd:~/fifthelement$ python3 manage.py runserver

Split your screen with tmux with the following two commands

CTRL + b (press both keys at the same time)
" (you'll need to use the SHIFT key)
In your new screen, try to curl against your webserver (by default Django runs on port 8000)

student@bchd:~/fifthelement$ curl http://localhost:8000/polls/

You should see the text, Hello, world. You’re at the polls index., which you defined in the index view. Exit out of your new tmux window.

student@bchd:~/fifthelement$ exit

Stop your Django server with CTRL + c

Open up fifthelement/settings.py

student@bchd:~/fifthelement$ vim fifthelement/settings.py

Inside you'll see a Python module with module-level variables representing Django settings. Check on the following settings:

DATABASES - By default, the configuration uses SQLite. If you’re new to databases, or you’re just interested in trying Django, this is the easiest choice. SQLite is included in Python, so you won’t need to install anything else to support your database. When starting your first real project, however, you may want to use a more scalable database like PostgreSQL, to avoid database-switching headaches down the road. If you wish to use another database, install the appropriate database bindings and change the following keys in the DATABASES "default" item to match your database connection settings:
ENGINE – Popular backends include django.db.backends.sqlite3, django.db.backends.postgresql, django.db.backends.mysql, and django.db.backends.oracle. Other backends are also available.
NAME – The name of your database. If you’re using SQLite, the database will be a file on your computer; in that case, NAME should be the full absolute path, including filename, of that file. The default value, os.path.join(BASE_DIR, "db.sqlite3"), will store the file in your project directory.
If your not going to use SQLite, additional settings, such as, USER, PASSWORD, and HOST must be added.
Within fifthelement/settings.py update TIME_ZONE to your timezone.

Within fifthelement/settings.py, check out INSTALLED_APPS near the top of the file. This holds name of all the Django applications that are activated on this Django instance. Apps can be used in multiple projects, and you can package and distribute them for use by others in their projects. By default, the list is as follows:

django.contrib.admin – The admin site. You’ll use it shortly.
django.contrib.auth – An authentication system.
django.contrib.contenttypes – A framework for content types.
django.contrib.sessions – A session framework.
django.contrib.messages – A messaging framework.
django.contrib.staticfiles – A framework for managing static files.
Save and exit with :wq

Some of the above applications make use of at least one database table, though, so we need to create the tables in the database before we can use them. To do that, run the following command:

student@bchd:~/fifthelement$ python3 manage.py migrate

The migrate command looks at the INSTALLED_APPS setting and creates any necessary database tables according to the database settings in your fifthelement/settings.py file and the database migrations shipped with the app (we’ll cover those later). You’ll see a message for each migration it applies.

Okay, now time for our first model, or our database layout, with additional metadata. In our simple poll app, we’ll create two models: Question and Choice.

A Question has a question and a publication date.
A Choice has two fields: the text of the choice and a vote tally. Each Choice is associated with a Question.
These concepts are represented by simple Python classes. Edit the polls/models.py

student@bchd:~/fifthelement$ vim polls/models.py

Ensure the file looks like this:


from django.db import models

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    # You can use an optional first positional argument to a Field to designate a human-readable name.
    pub_date = models.DateTimeField("date published")

class Choice(models.Model):
    # ForeignKey tells Django each Choice
    # is related to a single Question
    # Django supports common database relationships:
    # many-to-one, many-to-many, and one-to-one
    
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
The code is straightforward. Each model is represented by a class that subclasses django.db.models.Model. Each model has a number of class variables, each of which represents a database field in the model.

Each field is represented by an instance of a Field class – e.g., CharField for character fields and DateTimeField for datetimes. This tells Django what type of data each field holds.

To include the app in our project, we need to add a reference to its configuration class in the INSTALLED_APPS setting.

student@bchd:~/fifthelement$ vim fifthelement/settings.py

The PollsConfig class is in the polls/apps.py file, so its dotted path is "polls.apps.PollsConfig". Add that dotted path to the INSTALLED_APPS setting. It’ll look like this:


INSTALLED_APPS = [
    "polls.apps.PollsConfig",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]
Now Django knows to include the polls app. Let’s run another command:

student@bchd:~/fifthelement$ python3 manage.py makemigrations polls

By running makemigrations, you’re telling Django that you’ve made some changes to your models (in this case, you’ve made new ones) and that you’d like the changes to be stored as a migration. You can view the migration (potential changes to the database) with the following command:

student@bchd:~/fifthelement$ python3 manage.py sqlmigrate polls 0001

To create our model tables within our database (apply changes), use the migrate command.

student@bchd:~/fifthelement$ python3 manage.py migrate

Now, let’s hop into the interactive Python shell and play around with the free API Django gives you. To invoke the Python shell, use this command:

student@bchd:~/fifthelement$ python3 manage.py shell

We’re using this instead of simply typing “python”, because manage.py sets the DJANGO_SETTINGS_MODULE environment variable, which gives Django the Python import path to your fifthelement/settings.py file.


>>> from polls.models import Choice, Question  # Import the model classes we just wrote.

# No questions are in the system yet.
>>> Question.objects.all()
<QuerySet []>

# Create a new Question.
# Support for time zones is enabled in the default settings file, so
# Django expects a datetime with tzinfo for pub_date. Use timezone.now()
# instead of datetime.datetime.now() and it will do the right thing.
>>> from django.utils import timezone
>>> q = Question(question_text="What is new?", pub_date=timezone.now())

# Save the object into the database. You have to call save() explicitly.
>>> q.save()

# Now it has an ID.
>>> q.id
1

# Access model field values via Python attributes.
>>> q.question_text
"What is new?"
>>> q.pub_date
datetime.datetime(2012, 2, 26, 13, 0, 0, 775217, tzinfo=<UTC>)

# Change values by changing the attributes, then calling save().
>>> q.question_text = "What is up?"
>>> q.save()

# objects.all() displays all the questions in the database.
>>> Question.objects.all()
<QuerySet [<Question: Question object (1)>]>

# exit
>>> exit()
Wait a minute. <Question: Question object (1)> isn’t a helpful representation of this object. Let’s fix that by editing the Question model (in the polls/models.py file):

student@bchd:~/fifthelement$ vim polls/models.py

Add a __str__() method to both Question and Choice. It’s important to add str() methods to your models, not only for your own convenience when dealing with the interactive prompt, but also because objects’ representations are used throughout Django’s automatically-generated admin. Let’s also add a custom method to this model.


import datetime

from django.db import models
from django.utils import timezone

class Question(models.Model):
    # ...
    def __str__(self):
        return self.question_text
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Choice(models.Model):
    # ...
    def __str__(self):
        return self.choice_text
Save and exit with :wq

Note the addition of import datetime and from django.utils import timezone, to reference Python’s standard datetime module and Django’s time-zone-related utilities in django.utils.timezone, respectively.

Save these changes and start a new Python interactive shell:

student@bchd:~/fifthelement$ python3 manage.py shell

Run the following commands:


>>> from polls.models import Choice, Question

# Make sure our __str__() addition worked.
>>> Question.objects.all()
<QuerySet [<Question: What s up?>]>

# Django provides a rich database lookup API that's entirely driven by
# keyword arguments.
>>> Question.objects.filter(id=1)
<QuerySet [<Question: What s up?>]>
>>> Question.objects.filter(question_text__startswith="What")
<QuerySet [<Question: What s up?>]>

# Get the question that was published this year.
>>> from django.utils import timezone
>>> current_year = timezone.now().year
>>> Question.objects.get(pub_date__year=current_year)
<Question: What s up?>

# Request an ID that doesn't t exist, this will raise an exception.
>>> Question.objects.get(id=2)
Traceback (most recent call last):
    ...
DoesNotExist: Question matching query does not exist.

# Lookup by a primary key is the most common case, so Django provides a
# shortcut for primary-key exact lookups.
# The following is identical to Question.objects.get(id=1).
>>> Question.objects.get(pk=1)
<Question: What s up?>

# Make sure our custom method worked.
>>> q = Question.objects.get(pk=1)
>>> q.was_published_recently()
True

# Give the Question a couple of Choices. The create call constructs a new
# Choice object, does the INSERT statement, adds the choice to the set
# of available choices and returns the new Choice object. Django creates
# a set to hold the "other side" of a ForeignKey relation
# (e.g. a questions choice) which can be accessed via the API.
>>> q = Question.objects.get(pk=1)

# Display any choices from the related object set -- none so far.
>>> q.choice_set.all()
<QuerySet []>

# Create three choices.
>>> q.choice_set.create(choice_text="Not much", votes=0)
<Choice: Not much>
>>> q.choice_set.create(choice_text="The sky", votes=0)
<Choice: The sky>
>>> c = q.choice_set.create(choice_text="Just hacking again", votes=0)

# Choice objects have API access to their related Question objects.
>>> c.question
<Question: What s up?>

# And vice versa: Question objects get access to Choice objects.
>>> q.choice_set.all()
<QuerySet [<Choice: Not much>, <Choice: The sky>, <Choice: Just hacking again>]>
>>> q.choice_set.count()
3

# The API automatically follows relationships as far as you need.
# Use double underscores to separate relationships.
# This works as many levels deep as you want; there s no limit.
# Find all Choices for any question whose pub_date is in this year
# (reusing the "current_year" variable we created above).
>>> Choice.objects.filter(question__pub_date__year=current_year)
<QuerySet [<Choice: Not much>, <Choice: The sky>, <Choice: Just hacking again>]>

# Lets delete one of the choices. Use delete() for that.
>>> c = q.choice_set.filter(choice_text__startswith="Just hacking")
>>> c.delete()
>>> exit()
Generating admin sites for your staff or clients to add, change, and delete content is tedious work that doesn’t require much creativity. For that reason, Django entirely automates creation of admin interfaces for models. Django was written in a newsroom environment, with a very clear separation between “content publishers” and the “public” site. Site managers use the system to add news stories, events, sports scores, etc., and that content is displayed on the public site. Django solves the problem of creating a unified interface for site administrators to edit content. The admin isn’t intended to be used by site visitors. It’s for site managers.

First, create a user who can login to the admin site.

student@bchd:~/fifthelement$ python3 manage.py createsuperuser

Enter the desired user handle.

Username: admin

You will then be prompted for your desired email address:

Email address: admin@example.com

Provide a password:

Password: alta3

Provide the password again:

Password: alta3

Bypass password validation

y

Start the server so we can activate the admin site:

student@bchd:~/fifthelement$ python3 manage.py runserver

Open a browser in your desktop GUI and navigate to http://127.0.0.1:8000/admin/

Sign in with admin and alta3

But where’s our poll app? It’s not displayed on the admin index page. Just one thing to do: we need to tell the admin that Question objects have an admin interface. To do this, open the polls/admin.py

student@bchd:~/fifthelement$ vim polls/admin.py

Edit the file to look like this:


from django.contrib import admin

from .models import Question

admin.site.register(Question)
Save and exit with :wq

Log out and back into the admin site http://127.0.0.1:8000/admin/

You should now see a Questions, click on it.

This page displays all the questions in the database and lets you choose one to change it. Notice the “What’s up?” question we created earlier.

Click the What is up? question to edit it.

Things to note here:

The form is automatically generated from the Question model.
The bottom part of the page gives you a couple of options:
Save – Saves changes and returns to the change-list page for this type of object.
Save and continue editing – Saves changes and reloads the admin page for this object.
Save and add another – Saves changes and loads a new, blank form for this type of object.
Delete – Displays a delete confirmation page.
If the value of “Date published” doesn’t match the time when you created the question in Tutorial 1, it probably means you forgot to set the correct value for the TIME_ZONE setting. Change it, reload the page and check that the correct value appears.

Change the “Date published” by clicking the “Today” and “Now” shortcuts. Then click “Save and continue editing.” Then click “History” in the upper right. You’ll see a page listing all changes made to this object via the Django admin, with the timestamp and username of the person who made the change.

A view is a “type” of Web page in your Django application that generally serves a specific function and has a specific template. For example, in a blog application, you might have the following views:


 - Blog homepage – displays the latest few entries.
 - Entry “detail” page – permalink page for a single entry.
 - Year-based archive page – displays all months with entries in the given year.
 - Month-based archive page – displays all days with entries in the given month.
 - Day-based archive page – displays all entries in the given day.
 - Comment action – handles posting comments to a given entry.
In our poll application, we’ll have the following four views: - Question “index” page – displays the latest few questions. - Question “detail” page – displays a question text, with no results but with a form to vote. - Question “results” page – displays results for a particular question. - Vote action – handles voting for a particular choice in a particular question.

Edit polls/views.py

student@bchd:~/fifthelement$ vim polls/views.py

Add the following views at the bottom of the file.


def detail(request, question_id):
    return HttpResponse("You re looking at question %s." % question_id)

def results(request, question_id):
    response = "You re looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You re voting on question %s." % question_id)
Save and exit with :wq

Edit polls/urls.py

student@bchd:~/fifthelement$ vim polls/urls.py

Wire the new views into the polls.urls module by adding the following path() calls:


from django.urls import path

from . import views

urlpatterns = [
    # ex: /polls/
    path("", views.index, name="index"),
    # ex: /polls/5/
    path("<int:question_id>/", views.detail, name="detail"),
    # ex: /polls/5/results/
    path("<int:question_id>/results/", views.results, name="results"),
    # ex: /polls/5/vote/
    path("<int:question_id>/vote/", views.vote, name="vote"),
]
Save and exit with :wq

Run your Django server.

student@bchd:~/fifthelement$ python3 manage.py runserver

In the browser on your remote desktop GUI, navigate to the following links:

http://127.0.0.1:8000/polls/
http://127.0.0.1:8000/polls/5/
http://127.0.0.1:8000/polls/5/results
http://127.0.0.1:8000/polls/5/vote
http://127.0.0.1:8000/polls/7/
http://127.0.0.1:8000/polls/7/results
http://127.0.0.1:8000/polls/7/vote
When somebody requests a page from your website – say, “/polls/34/”, Django will load the fifthelement.urls Python module because it’s pointed to by the ROOT_URLCONF setting. It finds the variable named urlpatterns and traverses the patterns in order. After finding the match at 'polls/', it strips off the matching text ("polls/") and sends the remaining text – "34/" – to the 'polls.urls' URLconf for further processing. There it matches 'int:question_id/', resulting in a call to the detail() view.

Within the window hosting your Django server, stop the server with CTRL + c

Let is tweak our index 'view' so that it returns the last 5 poll questions in the system, separated by commas, according to publication date:

student@bchd:~/fifthelement$ vim polls/views.py

Let’s use Django’s template system to separate the design from Python by creating a template that the view can use. The reference to building this template is found at the end of the code.


from django.http import HttpResponse
from django.template import loader

from .models import Question


def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    template = loader.get_template("polls/index.html")
    context = {
        "latest_question_list": latest_question_list,
    }
    return HttpResponse(template.render(context, request))
Save and exit with :wq

Create a directory polls/templates/polls/

student@bchd:~/fifthelement$ mkdir -p polls/templates/polls/

Create the file polls/templates/polls/index.html

student@bchd:~/fifthelement$ vim polls/templates/polls/index.html

Make the following template:


{% if latest_question_list %}
    <ul>
    {% for question in latest_question_list %}
        <li><a href="/polls/{{ question.id }}/">{{ question.question_text }}</a></li>
    {% endfor %}
    </ul>
{% else %}
    <p>No polls are available.</p>
{% endif %}
Save and exit with :wq

Run the server.

student@bchd:~/fifthelement$ python3 manage.py runserver

In the browser on your remote desktop GUI, navigate to http://127.0.0.1:8000/polls/

You should see a bulleted-list containing the "What is up" question we set previously.

Stop the server with CTRL + c

The render() function takes the request object as its first argument, a template name as its second argument and a dictionary as its optional third argument. It returns an HttpResponse object of the given template rendered with the given context. Let is rewrite polls/views.py so that it uses render(), and also returns a 404 error if a question does not exist. Let is rename our old polls/views.py

student@bchd:~/fifthelement$ mv polls/views.py polls/views.py.old

Create a new polls/views.py

student@bchd:~/fifthelement$ vim polls/views.py

Make views.py appear as follows:


from django.http import Http404
from django.shortcuts import render

from .models import Question


def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    context = {"latest_question_list": latest_question_list}
    return render(request, "polls/index.html", context)
    
def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, "polls/detail.html", {"question": question})
Save and exit with :wq

The new concept here: The view raises the Http404 exception if a question with the requested ID doesn’t exist.

Next we want to edit the polls/templates/polls/detail.html template. There is a lot of templating going on here, so an explanation can be found below.

student@bchd:~/fifthelement$ vim polls/templates/polls/detail.html

If you understand Jinja2, then you'll be right at home with Django's template system. Jinja2 was written to copy what Django's template system which is only available if you're actually using Django. Read more about it here: https://docs.djangoproject.com/en/2.2/topics/templates/

Write the following into the file.


<h1>{{ question.question_text }}</h1>

{% if error_message %}<p><strong>{{ error_message }}</strong></p>{% endif %}

<form action="{% url "polls:vote" question.id %}" method="post">
{% csrf_token %}
{% for choice in question.choice_set.all %}
    <input type="radio" name="choice" id="choice{{ forloop.counter }}" value="{{ choice.id }}">
    <label for="choice{{ forloop.counter }}">{{ choice.choice_text }}</label><br>
{% endfor %}
<input type="submit" value="Vote">
</form>
Save and exit with :wq

The above template:

Displays a radio button for each question choice. The value of each radio button is the associated question choice’s ID. The name of each radio button is "choice". That means, when somebody selects one of the radio buttons and submits the form, it’ll send the POST data choice=# where # is the ID of the selected choice. This is the basic concept of HTML forms.

We set the form’s action to {% url "polls:vote" question.id %}. We have not made this change yet, but are about to in upcoming steps. The "polls" is a reference to a "namespace". Basically, it is a way to easily reference an application is URL set.

forloop.counter indicates how many times the for tag has gone through its loop

Since we’re creating a POST form (which can have the effect of modifying data), we need to worry about Cross Site Request Forgeries. Thankfully, you don’t have to worry too hard, because Django comes with a very easy-to-use system for protecting against it. In short, all POST forms that are targeted at internal URLs should use the {% csrf_token %} template tag.

The tutorial project has just one app, polls. In real Django projects, there might be five, ten, twenty apps or more. How does Django differentiate the URL names between them? For example, the polls app has a detail view, and so might an app on the same project that is for a blog. How does one make it so that Django knows which app view to create for a url when using the {% url %} template tag? The answer is to add namespaces to your URLconf. In the polls/urls.py file, go ahead and add an app_name to set the application namespace.

student@bchd:~/fifthelement$ vim polls/urls.py

Make your file look like the following.


from django.urls import path

from . import views

app_name = "polls"  # <--new line
urlpatterns = [
    path("", views.index, name="index"),
    path("<int:question_id>/", views.detail, name="detail"),
    path("<int:question_id>/results/", views.results, name="results"),
    path("<int:question_id>/vote/", views.vote, name="vote"),
]
Save and exit with :wq

Now we can change our polls/templates/polls/index.html template.

student@bchd:~/fifthelement$ vim polls/templates/polls/index.html

Edit your template to point at a name-spaced detail view.


{% if latest_question_list %}
    <ul>
    {% for question in latest_question_list %}
        <li><a href="{% url 'polls:detail' question.id %}">{{ question.question_text }}</a></li>
    {% endfor %}
    </ul>
{% else %}
    <p>No polls are available.</p>
{% endif %}
Save and exit with :wq

Let is update polls/views.py


from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from .models import Choice, Question

def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    context = {"latest_question_list": latest_question_list}
    return render(request, "polls/index.html", context)
    
def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, "polls/detail.html", {"question": question})
    
def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, "polls/detail.html", {
            "question": question,
            "error_message": "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))
        
def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/results.html", {"question": question})        
Save and exit with :wq

Some notes on the above structure:

request.POST is a dictionary-like object that lets you access submitted data by key name. In this case, request.POST['choice'] returns the ID of the selected choice, as a string. request.POST values are always strings.

Note that Django also provides request.GET for accessing GET data in the same way – but we’re explicitly using request.POST in our code, to ensure that data is only altered via a POST call.

request.POST['choice'] will raise KeyError if choice wasn’t provided in POST data. The above code checks for KeyError and redisplays the question form with an error message if choice isn’t given.

After incrementing the choice count, the code returns an HttpResponseRedirect rather than a normal HttpResponse. HttpResponseRedirect takes a single argument: the URL to which the user will be redirected (see the following point for how we construct the URL in this case).

As the Python comment above points out, you should always return an HttpResponseRedirect after successfully dealing with POST data. This tip isn’t specific to Django; it’s just good Web development practice.

We are using the reverse() function in the HttpResponseRedirect constructor in this example. This function helps avoid having to hardcode a URL in the view function.

Finally, let is edit polls/templates/polls/results.html

student@bchd:~/fifthelement$ vim polls/templates/polls/results.html

Create the following file:


<h1>{{ question.question_text }}</h1>

<ul>
{% for choice in question.choice_set.all %}
    <li>{{ choice.choice_text }} -- {{ choice.votes }} vote{{ choice.votes|pluralize }}</li>
{% endfor %}
</ul>

<a href="{% url 'polls:detail' question.id %}">Vote again?</a>
Save and exit with :wq

Let's run our server.

student@bchd:~/fifthelement$ python3 manage.py runserver

Now, go to /polls/1/ in your browser and vote in the question. You should see a results page that gets updated each time you vote. If you submit the form without having chosen a choice, you should see the error message.

Stop your server. Then consider yourself introduced to Django!


