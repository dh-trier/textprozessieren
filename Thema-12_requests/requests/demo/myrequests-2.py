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

base_url = "https://www.worldcat.org/search?q="
query = [["au", "biber"], ["ti", "variation"]]


# ========================================
# Functions 
# ========================================

def get_page(base_url, query):
    url = base_url + query[0][0] + "%3A" + query[0][1] + "+" + query[1][0] + "%3A" + query[1][1]
    print(url)
    result = requests.get(url, timeout=4)
    print(result.url)
    print(result.text)


def main(base_url, query):
    get_page(base_url, query)

main(base_url, query)


