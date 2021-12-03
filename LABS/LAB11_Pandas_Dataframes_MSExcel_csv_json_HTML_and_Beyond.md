# pandas dataframes - MS Excel, csv, json, HTML and beyond
Lab Objective
Reasons for using Python to analyze your data include data analysis, plotting and graphing, moving data to machine learning tools (scikit-learn), or possibly moving data across RESTful API interfaces.

For many the preferred way to interact with Excel is pandas. Using pandas has many advantages over PyExcel, and serious advantages over Excel’s UI. Pandas has excellent methods for reading all kinds of data from Excel files. You can also export your results from pandas back to Excel, if that’s preferred by your intended audience.

The pandas library tools for reading and writing data between in-memory data structures and different formats include Excel, as well as CSV and text files, SQL databases, and the fast HDF5 format.

Read about the Pandas project here:

https://pandas.pydata.org/

The data types pandas can read and write to can be found here:

https://pandas.pydata.org/pandas-docs/stable/user_guide/io.html

Procedure
Open a new terminal

Create a new directory to work in.

student@bchd:~$ mkdir -p ~/mycode/pandas/

Move into that directory.

student@bchd:~$ cd ~/mycode/pandas/

Ensure pandas is installed along with xlrd, and openpyxl, which are optional dependencies for working with MS Excel.

student@bchd:~/mycode/pandas$ python3 -m pip install pandas xlrd openpyxl

We can also create a few graphs. To do that, we'll want matplot lib

student@bchd:~/mycode/pandas$ python3 -m pip install matplotlib

Download the Excel data set we'll be using for this lab. The set itself spans 3 sheets, and contains movie data. You may want to download this dataset on your local laptop, and check it out in Excel.

student@bchd:~/mycode/pandas$ wget https://static.alta3.com/files/movies.xls

Create a new script, pandabear01.py

student@bchd:~/mycode/pandas$ vim pandabear01.py

Create the following solution:


#!/usr/bin/python3

import pandas as pd

# create some graphs
import matplotlib.pyplot as plt

def main():
    # define the name of our xls file
    excel_file = 'movies.xls'

    # create a DataFrame (DF) object. EASY!
    # because we did not specify a sheet
    # only the first sheet was read into the DF
    movies = pd.read_excel(excel_file)

    # show the first five rows of our DF
    # DF has 5 rows and 25 columns (indexed by integer)
    print(movies.head())

    # Choose the first column "Title" as
    # index (index=0)
    movies_sheet1 = pd.read_excel(excel_file, sheet_name=0, index_col=0)
    # DF has 5 rows and 24 columns (indexed by title)
    print(movies_sheet1.head())

    # grab the next 2 sheets as well
    movies_sheet2 = pd.read_excel(excel_file, sheet_name=1, index_col=0)
    # DF has 5 rows and 24 columns (indexed by title)
    print(movies_sheet2.head())

    movies_sheet3 = pd.read_excel(excel_file, sheet_name=2, index_col=0)
    # DF has 5 rows and 24 columns (indexed by title)
    print(movies_sheet3.head())

    # combine all DFs into a single DF called movies
    movies = pd.concat([movies_sheet1, movies_sheet2, movies_sheet3])

    # number of rows and columns (5042, 24)
    print(movies.shape)

    # sort DataFrame based on Gross Earnings
    sorted_by_gross = movies.sort_values(["Gross Earnings"], ascending=False)

    # Data is sorted by values in a column
    # display the top 10 movies by Gross Earnings.
    # passing the 10 values to head returns the top 10 not the default 5
    print(sorted_by_gross.head(10))

    # create a stacked bar graph
    sorted_by_gross['Gross Earnings'].head(10).plot(kind="barh")
    # save the figure as stackedbar.png
    plt.savefig("stackedbar.png")

if __name__ == "__main__":
    main()
Save and exit with :wq

Run your script.

student@bchd:~/mycode/pandas$ python3 pandabear01.py

If you want to check out stackedbar.png, perform a git operation and push to GitHub. Alternatively, let it sit for now and check it out after you perform git operations at the conclusion of this lab.

Let's try combining multiple data sources, CSV and JSON, into a single data frame, then exporting to a few formats, including Excel. Start by downloading a CSV dataset.

student@bchd:~/mycode/pandas$ wget https://static.alta3.com/files/ciscodata.csv

Now, download a JSON dataset.

student@bchd:~/mycode/pandas$ wget https://static.alta3.com/files/ciscodata2.json

Display both datasets. Both have valuable data, but they're in mixed formats. First, display the CSV data.

student@bchd:~/mycode/pandas$ cat ciscodata.csv

Display the json.

student@bchd:~/mycode/pandas$ cat ciscodata2.json

Great. Now write a script that will take those data sets, and combine them into a single dataframe.

Create a new script, pandabear02.py

student@bchd:~/mycode/pandas$ vim pandabear02.py

Create the following script:


#!/usr/bin/python3

import pandas as pd

def main():
    ciscocsv = pd.read_csv("ciscodata.csv")
    ciscojson = pd.read_json("ciscodata2.json")
    
    # display first 5 entries of the ciscocsv dataframe
    print(ciscocsv.head())

    # display first 5 entries of the ciscojson dataframe            
    print(ciscojson.head())
    
    ciscodf = pd.concat([ciscocsv, ciscojson])
    # uncomment the line below to "fix" the index issue
    # ciscodf = pd.concat([ciscocsv, ciscojson], ignore_index=True, sort=False)
    
    print(ciscodf)
    
if __name__ == "__main__":
    main()
Save and exit with :wq

Execute your code.

student@bchd:~/mycode/pandas$ python3 pandabear02.py

Before you go any further, study the results. Notice how the indexes are repeated? There is a fix for this, which is described here: https://pandas.pydata.org/pandas-docs/stable/user_guide/merging.html under, "Ignoring indexes on the concatenation axis".

Let's rewrite that script. This time, we'll fix the indexing issue, and export our data a few different ways. To export to Excel, you'll need to install xlwt with pip. Failure to do so will remind you that you need to install xlwt.

student@bchd:~/mycode/pandas$ python3 -m pip install xlwt

Create a new script, pandabear03.py

student@bchd:~/mycode/pandas$ vim pandabear03.py

Write the following script:


#!/usr/bin/python3

import pandas as pd

def main():
    # create a dataframe ciscocsv
    ciscocsv = pd.read_csv("ciscodata.csv")
    # create a dataframe ciscojson
    ciscojson = pd.read_json("ciscodata2.json")

    # The line below concats and reapplies the index value
    ciscodf = pd.concat([ciscocsv, ciscojson], ignore_index=True, sort=False)

    ## print to the screen the re-indexed dataframe
    print(ciscodf)
    
    ## print a blankline
    print()

    ## export to json
    ciscodf.to_json("combined_ciscodata.json")

    ## export to csv
    ciscodf.to_csv("combined_ciscodata.csv")
    
    ## export to Excel
    ciscodf.to_excel("combined_ciscodata.xls")
    
    ## create a python dictionary
    x = ciscodf.to_dict()
    print(x)
    
if __name__ == "__main__":
    main()
Save and exit with :wq

Execute your code.

student@bchd:~/mycode/pandas$ python3 pandabear03.py

Study the output. First the combined_ciscodata.json file.

student@bchd:~/mycode/pandas$ cat combined_ciscodata.json

Now combined_ciscodata.csv

student@bchd:~/mycode/pandas$ cat combined_ciscodata.csv

Let the XLS file sit for now.

There's a few problems. The JSON data that was produced now has the index numbers included in it, as does the CSV data. Let's see if we can write an improved script that fixes this.

Create a new script, pandabear04.py

student@bchd:~/mycode/pandas$ vim pandabear04.py

Write the following script:


#!/usr/bin/python3

import pandas as pd

def main():
    # create a dataframe ciscocsv
    ciscocsv = pd.read_csv("ciscodata.csv")
    # create a dataframe ciscojson
    ciscojson = pd.read_json("ciscodata2.json")

    # The line below concats and reapplies the index value
    ciscodf = pd.concat([ciscocsv, ciscojson], ignore_index=True, sort=False)
    
    ## export to json
    ## do not include index number
    ciscodf.to_json("combined_ciscodata.json", orient="records")

    ## export to csv
    ## do not include index number
    ciscodf.to_csv("combined_ciscodata.csv", index=False)
    
    ## export to Excel
    ## do not include index number to xls
    ciscodf.to_excel("combined_ciscodata.xls", index=False)
    ## do not include index number to xlsx
    ciscodf.to_excel("combined_ciscodata.xlsx", index=False)
    
    ## create a python dictionary
    ## do not include index number
    x = ciscodf.to_dict(orient='records')
    print(x)
    
if __name__ == "__main__":
    main()
Save and exit with :wq

Execute your code.

student@bchd:~/mycode/pandas$ python3 pandabear04.py

Study the output which no longer includes the index values. First the combined_ciscodata.json file.

student@bchd:~/mycode/pandas$ cat combined_ciscodata.json

Now combined_ciscodata.csv Notice, no more index values.

student@bchd:~/mycode/pandas$ cat combined_ciscodata.csv

Download a new dataset. This data set has information regarding airlines, and has over 58,400 entries

student@bchd:~/mycode/pandas$ wget https://static.alta3.com/files/airline_flights.csv

This dataset is too large to work with alone, but we can use code to answer some questions. Create a new script, pandaflight.py

student@bchd:~/mycode/pandas$ vim pandaflight.py

Write the following script:


#!/usr/bin/python3

import pandas as pd

def main():
    flightcsv = pd.read_csv("airline_flights.csv")

    # organize data by origin and destination airport
    flightcsv_tofrom = flightcsv.groupby(['ORG_AIR', 'DEST_AIR']).size()
    print(flightcsv_tofrom.head())
    
    # Display the number of flights between Huston (IAH)
    # and Atlanta (ATL) in both directions
    print("\nFlight from ATL to IAH and IAH to ATL")
    print(flightcsv_tofrom.loc[[("ATL", "IAH"), ("IAH", "ATL")]])
    
    # display first 5 entries of the flightcsv dataframe
    print(flightcsv_tofrom.head())
    
if __name__ == "__main__":
    main()    
Execute your code.

student@bchd:~/mycode/pandas$ python3 pandaflight.py

If you're tracking your code in GitHub, issue the following commands:

cd ~/mycode
git add *
git commit -m "working with pandas"
git push origin main

