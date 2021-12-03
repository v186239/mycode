# Learning sqlite3
Lab Objective
SQLite is a C library that provides a lightweight disk-based database that doesn’t require a separate server process and allows accessing the database using a nonstandard variant of the SQL query language. Some applications can use SQLite for internal data storage. It’s also possible to prototype an application using SQLite and then port the code to a larger database such as PostgreSQL or Oracle.

The sqlite3 module was written by Gerhard Häring. It provides a SQL interface compliant with the DB-API 2.0 specification described by PEP 249.

The library official documentation is available here: https://docs.python.org/3/library/sqlite3.html

Procedure
Create a new directory to work in, ~/mycode/sqldb/

student@bchd:~$ mkdir /home/student/mycode/sqldb

Move into your new directory.

student@bchd:~$ cd /home/student/mycode/sqldb

Create a new script, database01.py. This script will create a database called test.db.

student@bchd:~/mycode/sqldb$ vim database01.py

Following Python code shows how to connect to an existing database. If the database does not exist, then it will be created and finally a database object will be returned. Copy and paste the following into your script.


#!/usr/bin/python3

import sqlite3
conn = sqlite3.connect('test.db')
print("Opened database successfully")
Save and exit with :wq

Run your script.

student@bchd:~/mycode/sqldb$ python3 database01.py

Create a new script, database02.py. This script will create a table called company within our database.

student@bchd:~/mycode/sqldb$ vim database02.py

Copy and paste the following into your script.


#!/usr/bin/env python3

import sqlite3
conn = sqlite3.connect('test.db')
print("Opened database successfully")
conn.execute('''CREATE TABLE COMPANY
 (ID INT PRIMARY KEY     NOT NULL,
 NAME           TEXT    NOT NULL,
 AGE            INT     NOT NULL,
 ADDRESS        CHAR(50),
 SALARY         REAL);''')
print("Table created successfully")
conn.close()
Save and exit with :wq

Run your script.

student@bchd:~/mycode/sqldb$ python3 database02.py

Run your script a second time... this time it will fail

student@bchd:~/mycode/sqldb$ python3 database02.py

The script failed because your table already exists! Create a new script that will not have this issue.

student@bchd:~/mycode/sqldb$ vim database02v2.py

Rather than try to handle the error with Python, we can improve the way we create our table in sqlite. By changing the language to CREATE TABLE IF NOT EXISTS COMPANY, we can prevent the error from ever occurring. Create the following improved script.


#!/usr/bin/env python3

import sqlite3
conn = sqlite3.connect('test.db')
print("Opened database successfully")
conn.execute('''CREATE TABLE IF NOT EXISTS COMPANY
 (ID INT PRIMARY KEY     NOT NULL,
 NAME           TEXT    NOT NULL,
 AGE            INT     NOT NULL,
 ADDRESS        CHAR(50),
 SALARY         REAL);''')
print("Table created successfully")
conn.close()
Save and exit with :wq

Run your new script. It should no longer cause an error.

student@bchd:~/mycode/sqldb$ python3 database02v2.py

Run your script a second time, just to make sure we no longer are throwing errors.

student@bchd:~/mycode/sqldb$ python3 database02v2.py

Write a script that will place some data into our database. Create database03.py.

student@bchd:~/mycode/sqldb$ vim database03.py

Copy and paste the following into your script.


#!/usr/bin/env python3

import sqlite3
conn = sqlite3.connect('test.db')
print("Opened database successfully")

conn.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) VALUES (1, 'Paul', 32, 'California', 20000.00 )")

conn.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) VALUES (2, 'Allen', 25, 'Texas', 15000.00 )")

conn.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) VALUES (3, 'Teddy', 23, 'Norway', 20000.00 )")

conn.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) VALUES (4, 'Mark', 25, 'Rich-Mond ', 65000.00 )")

conn.commit()
print("Records created successfully")
conn.close()
Save and exit with :wq

Run your script.

student@bchd:~/mycode/sqldb$ python3 database03.py

Create a new script, database04.py. This script will select some of our data from the database and print it out.

student@bchd:~/mycode/sqldb$ vim database04.py

Copy and paste the following into your script.


#!/usr/bin/env python3

import sqlite3
conn = sqlite3.connect('test.db')
print("Opened database successfully")
cursor = conn.execute("SELECT id, name, address, salary from COMPANY")
for row in cursor:
    print("ID = ", row[0])
    print("NAME = ", row[1])
    print("ADDRESS = ", row[2])
    print("SALARY = ", row[3], "\n")

print("Operation done successfully")
conn.close()
Save and exit with :wq

Run your script.

student@bchd:~/mycode/sqldb$ python3 database04.py

Create a new script, database05.py. This script will update some of our data from the database and print it out.

student@bchd:~/mycode/sqldb$ vim database05.py

Copy and paste the following into your script.


#!/usr/bin/env python3

import sqlite3

conn = sqlite3.connect('test.db')
print("Opened database successfully")

conn.execute("UPDATE COMPANY set SALARY = 25000.00 where ID = 1")
conn.commit()
print("Total number of rows updated :", conn.total_changes)

cursor = conn.execute("SELECT id, name, address, salary from COMPANY")
for row in cursor:
    print("ID = ", row[0])
    print("NAME = ", row[1])
    print("ADDRESS = ", row[2])
    print("SALARY = ", row[3], "\n")

print("Operation done successfully")
conn.close()
Save and exit with :wq

Run your script.

student@bchd:~/mycode/sqldb$ python3 database05.py

Create a new script, database06.py. This script will delete some of our data from the database and print out the modified database.

student@bchd:~/mycode/sqldb$ vim database06.py

Copy and paste the following into your script.


#!/usr/bin/env python3

import sqlite3

conn = sqlite3.connect('test.db')
print("Opened database successfully")

conn.execute("DELETE from COMPANY where ID = 2;")
conn.commit()
print("Total number of rows deleted :", conn.total_changes)

cursor = conn.execute("SELECT id, name, address, salary from COMPANY")
for row in cursor:
    print("ID = ", row[0])
    print("NAME = ", row[1])
    print("ADDRESS = ", row[2])
    print("SALARY = ", row[3], "\n")

print("Operation done successfully")
conn.close()
Save and exit with :wq

Run your script.

student@bchd:~/mycode/sqldb$ python3 database06.py

Be sure to check up on Python sqlite3 module's official documentation: https://docs.python.org/3/library/sqlite3.html

If you're tracking your code in GitHub, issue the following commands:

cd ~/mycode
git add *
git commit -m "sql operations and python3"
git push origin main
