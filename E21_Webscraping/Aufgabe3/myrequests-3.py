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


# ========================================
# Functions 
# ========================================

filename = "ABEILLE_ARGELIE.txt"
myurl = base_url + "pages/txt/" + filename
print(myurl)


def get_content(myurl): 
    try: 
        data = requests.get(myurl, timeout=4)
        print("Success!")
        content = data.text
        #print(content[0:100])
        #print(len(content), "signs")
        return content
    except: 
        print("Something went wrong in get_content.")

get_content(myurl)


