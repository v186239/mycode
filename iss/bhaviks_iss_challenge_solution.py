#!/usr/bin/python3
# Note must install pip install reverse_geocoder to use this script
"""tracking the iss using
   api.open-notify.org/astros.json | Alta3 Research"""
import requests
import datetime
import reverse_geocoder as rg
from pprint import pprint
## Define URL
URL= 'http://api.open-notify.org/iss-now.json'
def main():
    """runtime code"""
    ## Call the URL
    locationresp= requests.get(URL)
    ## strip the json off the 200 that was returned by our API
    ## translate the json into python lists and dictionaries
    locationjson= locationresp.json()
    #pprint(locationjson)
    TIMESTAMP= datetime.datetime.fromtimestamp(locationjson['timestamp'])
    LONGITUDE= locationjson['iss_position']['longitude']
    LATITUDE= locationjson['iss_position']['latitude']
    coords_tuple= (LATITUDE, LONGITUDE)
    result= rg.search(coords_tuple)
    CITY= result[0]['name']
    COUNTRY= result[0]['cc']
    # display the results
    print("\n\nCURRENT LOCATION OF THE ISS:")
    #print(f"Timestamp  : {datetime.datetime.fromtimestamp(locationjson['timestamp'])}")
    #print(f"Longitude : {locationjson['iss_position']['longitude']}")
    #print(f"Latitude  : {locationjson['iss_position']['latitude']}")
    print(f"Timestamp    : {TIMESTAMP}")
    print(f"Longitude    : {LONGITUDE}")
    print(f"Latitude     : {LATITUDE}")
    print(f"City/Country : {CITY}/{COUNTRY}\n\n")
if __name__ == "__main__":
    main()
