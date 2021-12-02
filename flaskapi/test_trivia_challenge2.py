#!/usr/bin/env python3
"""how to use the requests module to send a POST"""

import requests

url= "http://10.2.224.247:2224"

nv = {
          "name": "Chicken",
          }

requests.post(url, json=nv)
