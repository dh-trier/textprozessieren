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
    data = requests.get(myurl, timeout=4)
    content = data.text
    print(content[0:100])
    print(len(content))
    return content

get_content(myurl)


