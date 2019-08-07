# Example to use BeautifulSoup in python to extract data from html page
# on the example page here, there is a drop-down list tht we can choose
# carrier of the flight and the airport code.
# We are going to extract these information from the html page by beautifulsoup
# You need to inspect the web page source code to figure out where are things you wanna extract
from bs4 import BeautifulSoup
import requests
import json

html_page = "example.html"
soup = BeautifulSoup(open(html_page))

# Store all the values
list_values = []
carrier_list = soup.find(id = 'CarrierList')
print(carrier_list ) # Values all under the 'option'
for carrier in carrier_list.find_all('option'):
    list_values.append(carrier['value'])
print(list_values)

# Print all the texts
for carrier in carrier_list.find_all('option'):
    print(carrier.text)

## Request the specific page first to avoid download the html file
r = requests.get("http://www.transtats.bts.gov/Data_Elements.aspx?Data=2")
soup = BeautifulSoup(r.text)

## Write the result to a html file
# if r stores our result
htm = open('sample.html','w')
htm.write(r.text)

## What if our reqeust broken?
# One common reason of broken request is that the requested text and the request post
# are not in the same session. So the parameters would not valid to request post any more.
# We could use requests.Session() to make sure everything is in the same page.
sess = requests.Session()
r = sess.get("http://www.transtats.bts.gov/Data_Elements.aspx?Data=2")
r = sess.post("https://www.transtats.bts.gov/Data_Elements.aspx?Data=2",
           data = (
                   ("__EVENTTARGET", ""),
                   ("__EVENTARGUMENT", ""),
                   ("__VIEWSTATE", ''),
                   ("__VIEWSTATEGENERATOR", ''),
                   ("__EVENTVALIDATION", ''),
                   ("CarrierList", "VX"),
                   ("AirportList", "BOS"),
                   ("Submit", "Submit")
                  ))
htm = open('sample.html','w')
htm.write(r.text)

#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Please note that the function 'make_request' is provided for your reference only.
# You will not be able to to actually use it from within the Udacity web UI.
# Your task is to process the HTML using BeautifulSoup, extract the hidden
# form field values for "__EVENTVALIDATION" and "__VIEWSTATE" and set the appropriate
# values in the data dictionary.
# All your changes should be in the 'extract_data' function
def extract_data(page):
    data = {"eventvalidation": "",
            "viewstate": ""}
    with open(page, "r") as html:
        # do something here to find the necessary values
        soup = BeautifulSoup(html,"lxml")
        data['eventvalidation'] = soup.find(id = '__EVENTVALIDATION')['value']
        data['viewstate'] = soup.find(id = '__VIEWSTATE')['value']
    return data


def make_request(data):
    eventvalidation = data["eventvalidation"]
    viewstate = data["viewstate"]
    viewstategenerator = data["viewstategenerator"]
    r = requests.post("https://www.transtats.bts.gov/Data_Elements.aspx?Data=2",
           data = (
                   ("__EVENTTARGET", ""),
                   ("__EVENTARGUMENT", ""),
                   ("__VIEWSTATE", viewstate),
                   ("__VIEWSTATEGENERATOR",viewstategenerator),
                   ("__EVENTVALIDATION", eventvalidation),
                   ("CarrierList", "VX"),
                   ("AirportList", "BOS"),
                   ("Submit", "Submit")
                  ))
    return r.text


def test():
    data = extract_data(html_page)
    assert data["eventvalidation"] != ""
    assert data["eventvalidation"].startswith("/wEWjAkCoIj1ng0")
    assert data["viewstate"].startswith("/wEPDwUKLTI")

    
test()