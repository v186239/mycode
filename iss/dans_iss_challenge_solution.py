#!/usr/bin/python3
"""tracking the iss using
   http://api.open-notify.org/iss-now.json"""

import requests
import datetime
import reverse_geocoder as rg


## Define URL
issurl = 'http://api.open-notify.org/iss-now.json'

def main():
    """runtime code"""

    ## Call the webservice
    isslocation = requests.get(issurl)

    ## Format the response
    issresp = isslocation.json()

    ## Convert Epoch time to datetime
    epoch_time = issresp['timestamp']
    date_time = datetime.datetime.fromtimestamp(epoch_time)

    ## Convert Lat/Lon to geolocation
    iss_geo = (issresp['iss_position']['latitude'],issresp['iss_position']['longitude'])
    geo_result = rg.search(iss_geo)

    ## Display the current locaiton and timestamp of the ISS
    print(f"CURRENT LOCATION OF THE ISS:\n  Timesamp: {date_time}\n  Lon: {issresp['iss_position']['longitude']}\n  Lat: {issresp['iss_position']['latitude']}\n  City/Country: {geo_result[0]['name']}/{geo_result[0]['cc']}")

#    print(issresp)

if __name__ == "__main__":
    main()
