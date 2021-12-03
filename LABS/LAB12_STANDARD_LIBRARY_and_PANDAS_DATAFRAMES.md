# CSV data - Standard Library and pandas dataframes
Lab Objective
The objective of this lab is to work with CSV data within Python using both the standard library solution import csv, as well as a popular 3rd party solution, import pandas. Pandas is the best abstraction available, but not all students will find themselves in a position to install it (highly secure environments sometimes limit 3rd party installs).

import csv
The standard library solution designed to work out of the box with Excel-generated CSV files, it is easily adapted to work with a variety of CSV formats. The CSV library contains objects and other code to read, write, and process data from and to CSV files.

Reading from a CSV file is done using the reader object. The CSV file is opened as a text file with Python’s built-in open() function, which returns a file object. This is then passed to the reader, which does the heavy lifting.

import pandas
The panadas library will be covered more fully in subsequent labs. For know, know this 3rd party library can work with multiple formats, including CSV, JSON, MS Excel, and many more. Read more about pandas here:
https://pandas.pydata.org/

Procedure
Take a moment to clean up your remote desktop. For now, close all other terminal spaces or windows you might have open.

Open a new terminal, then create a new directory to work in.

student@bchd:~$ mkdir -p /home/student/mycode/csv01/

Move into the new directory.

student@bchd:~$ cd /home/student/mycode/csv01/

We need to start with a example CSV file. Let's create one.

student@bchd:~/mycode/csv01$ vim superbirthday.csv

Copy and paste the following into the file:


name,heroname,birthday month
Selina Kyle,Catwoman,March
Alfred Pennyworth,Butler,April
Clark Kent,Superman,June
Kara Zor-El,Supergirl,September
Alan Scott,Green Lantern,October
Save and exit with :wq

Create the script csvread01.py

student@bchd:~/mycode/csv01$ vim csvread01.py

Copy and paste the following code into the file.


#!/usr/bin/python3
import csv

def main():

    with open('superbirthday.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                # print(f'Column names are {", ".join(row)}')
                # above is the python3.6+ way to do things
                print('Column names are {}'.format(", ".join(row)))
                line_count += 1
            else:
                # print(f'\t{row[0]} aka {row[1]}, was born in {row[2]}.')
                # above is a python3.6+ way to do things
                print('\t{} aka {}, was born in {}.'.format(row[0],row[1],row[2]))
                line_count += 1
        # print(f'Processed {line_count} lines.') # python3.6 way to do things
        print('Processed {} lines.'.format(line_count))
        
if __name__ == "__main__":
    main()
Save and exit with :wq

Change permissions on your code:

student@bchd:~/mycode/csv01$ chmod u+x csvread01.py

Run csvread01.py.

student@bchd:~/mycode/csv01$ ./csvread01.py

Let's try writing the same script with pandas. First, make sure pandas is installed.

student@bchd:~/mycode/csv01$ python3 -m pip install pandas

Write a new script.

student@bchd:~/mycode/csv01$ vim csvread01pandas.py

Create the following:


#!/usr/bin/python3
import pandas

def main():

    #create a dataframe called superdf from our csv data
    superdf = pandas.read_csv("superbirthday.csv")

    # display the column names
    print(f"Column names are {', '.join(superdf)}")

    # uncomment the line below if you need to see what we are looping across
    # orient = 'records' prevents to_dict() from using the index value
    #print(superdf.to_dict(orient='records'))

    for row in superdf.to_dict(orient='records'):
        print(f"\t{row['name']} aka {row['heroname']}, was born in {row['birthday month']}.")
    
    # print the total number of lines (span returns (lines, columns))
    print(f"Total lines processed {superdf.shape[0]}")
    
if __name__ == "__main__":
    main()
Save and exit with :wq

Execute your script.

student@bchd:~/mycode/csv01$ python3 csvread01pandas.py

Looks like pandas was a great replacement tool for the Python standard library solution. Not all students will find themselves able to install pandas in all environments (highly secure environments may limit installs of 3rd party packages). Let's check out another tool from the Python Standard Library, csv.DictReader(). Create the script csvread02.py

student@bchd:~/mycode/csv01$ vim csvread02.py

Copy and paste the following code into the file.


#!/usr/bin/python3
import csv

def main():
    with open('superbirthday.csv', mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                # print(f'Column names are {", ".join(row)}') # python3.6 way
                                                              ## to do things
                print('Column names are {}'.format(", ".join(row)))
                line_count += 1
            # print(f'\t{row["name"]} aka {row["heroname"]} was born in {row["birthday month"]}.')
            # above is the python3.6+ way to do things
            print('\t{} aka {} was born in {}.'.format(row["name"],row["heroname"],row["birthday month"]))
            line_count += 1
    # print(f'Processed {line_count} lines.') # python3.6 way to do things
    print('Processed {} lines.'.format(line_count))
if __name__ == "__main__":
    main()
Save and exit with :wq

Change permissions on your code:

student@bchd:~/mycode/csv01$ chmod u+x csvread02.py

Run csvread02.py.

student@bchd:~/mycode/csv01$ ./csvread02.py

CODE CUSTOMIZATION - Add a section to the script so it creates a file, regularbirthday.csv, that has the heroname data omitted from the dataset. You may use pandas or the csv library to complete this task.

Since you can read our data into a dictionary, it’s only fair that you should be able to write it out from a dictionary as well. Unlike DictReader, the fieldnames parameter is required when writing a dictionary. This makes sense when you think about it: without a list of fieldnames, the DictWriter can’t know which keys to use to retrieve values from your dictionaries. It also uses the keys in fieldnames to write out the first row as column names.

Create the script csvread03.py

student@bchd:~/mycode/csv01$ vim csvread03.py

Copy and paste the following code into the file.


#!/usr/bin/python3

import csv

def main():
    with open('inventory.csv', mode='w') as csv_file:
        fieldnames = ['hostname', 'ip', 'service']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerow({'hostname': 'dumbledore', 'ip': '192.168.9.22', 'service': 'objectstorage'})
        writer.writerow({'hostname': 'hermione', 'ip': '10.0.2.66', 'service': 'httpd'})
if __name__ == "__main__":
    main()
Save and exit with :wq

Change permissions on your code:

student@bchd:~/mycode/csv01$ chmod u+x csvread03.py

Run csvread03.py.

student@bchd:~/mycode/csv01$ ./csvread03.py

Display the contents of the new CSV file, inventory.csv.

student@bchd:~/mycode/csv01$ cat inventory.csv

Let's try that last script again, only using pandas. Create the script csvread03pandas.py

student@bchd:~/mycode/csv01$ vim csvread03pandas.py

Copy and paste the following code into the file.


#!/usr/bin/python3
import pandas

def main():

    ## create a python list
    mydata = [
    {'hostname': 'dumbledore', 'ip': '192.168.9.22', 'service': 'objectstorage'},
    {'hostname': 'hermione', 'ip': '10.0.2.66', 'service': 'httpd'}
    ]
    
    ## create a data frame from our python data
    df = pandas.DataFrame(mydata)
    
    ## create the csv file without the index labels
    df.to_csv("inventorypandas.csv", index=False)

if __name__ == "__main__":
    main()
Save and exit with :wq

Execute your code.

student@bchd:~/mycode/csv01$ python3 csvread03pandas.py

Display the contents of the new CSV file, inventorypandas.csv.

student@bchd:~/mycode/csv01$ cat inventorypandas.csv

Once again, pandas was a lot easier than the standard library solution!

If you're tracking your code in GitHub, issue the following commands:

cd ~/mycode
git add *
git commit -m "csv data and pandas"
git push origin main
