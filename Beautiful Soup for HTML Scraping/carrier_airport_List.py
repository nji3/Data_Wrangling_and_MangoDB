#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Your task in this exercise is to modify 'extract_carrier()` to get a list of
all airlines. Exclude all of the combination values like "All U.S. Carriers"
from the data that you return. You should return a list of codes for the
carriers.

All your changes should be in the 'extract_carrier()' function. The
'options.html' file in the tab above is a stripped down version of what is
actually on the website, but should provide an example of what you should get
from the full file.

Complete the 'extract_airports()' function so that it returns a list of airport
codes, excluding any combinations like "All".

Please note that the function 'make_request()' is provided for your reference
only. You will not be able to to actually use it from within the Udacity web UI.
"""

from bs4 import BeautifulSoup
import requests

html_page = "options.html"


def extract_carriers(page):
    data = {}
    data["carrier"] = []
    data["airport"] = []
    with open(page, "r") as html:
        # do something here to find the necessary values
        soup = BeautifulSoup(html, "lxml")
        data['eventvalidation'] = soup.find(id = '__EVENTVALIDATION')['value']
        data['viewstate'] = soup.find(id = '__VIEWSTATE')['value']
        carrier_list = soup.find(id = 'CarrierList')
        for carrier in carrier_list.find_all('option'):
            data["carrier"].append(carrier['value'])
        airport_list = soup.find(id = 'AirportList')
        for airport in airport_list.find_all('option'):
            if 'All' not in airport['value']:
                data["airport"].append(airport['value'])
    return data["airport"]


def make_request():
    s = requests.Session()
    page = s.get("http://www.transtats.bts.gov/Data_Elements.aspx?Data=2")
    data = extract_carriers(page)

    eventvalidation = data["eventvalidation"]
    viewstate = data["viewstate"]
    airport = data["airport"]
    carrier = data["carrier"]

    r = s.post("https://www.transtats.bts.gov/Data_Elements.aspx?Data=2",
               data = (("__EVENTTARGET", ""),
                       ("__EVENTARGUMENT", ""),
                       ("__VIEWSTATE", viewstate),
                       ("__EVENTVALIDATION", eventvalidation),
                       ("CarrierList", carrier),
                       ("AirportList", airport),
                       ("Submit", "Submit")))

    return r.text


def test(html_page):
    data = extract_carriers(html_page)
    assert len(data) == 16
    assert "FL" in data
    assert "NK" in data

if __name__ == "__main__":
    html_page = "options.html"
    test(html_page)