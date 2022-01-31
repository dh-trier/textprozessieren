#!/usr/bin/env python3


"""
# Script to demo requests
"""

# ========================================
# Imports
# ========================================

# Generic imports
from os.path import join
import os
import glob

# Specific imports
import re
import requests


# ========================================
# Parameters
# ========================================

base_url = "http://theatre-classique.fr/"

filenames = ["ABEILLE_ARGELIE.txt", "ABEILLE_LYNCEE.txt"]


# ========================================
# Functions 
# ========================================


def build_urls(base_url, filenames): 
    myurls = []
    for name in filenames: 
        print(name)
        myurl = base_url + "pages/txt/" + name
        myurls.append(myurl)
    #print(myurls)
    return myurls
        

def get_content(myurl): 
    try: 
        data = requests.get(myurl, timeout=4)
        print("Success!")
        content = data.text
        print(data.encoding)
        data.encoding = "utf8"
        content = data.text
        print(data.encoding)
        #print(content)
        return content
    except: 
        print("Something went wrong in get_content.")


def main(base_url, filenames): 
    myurls = build_urls(base_url, filenames)
    #print(myurls)
    for myurl in myurls: 
        content = get_content(myurl)

main(base_url, filenames)

