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

base_url = "http://www.museumsstiftung.de/briefsammlung/post-von-drueben/briefliste.html?action=searchresults&what=letter&le_fulltext="
query = "Trabant"


# ========================================
# Functions 
# ========================================

def get_page(base_url, query):
    url = base_url + query
    result = requests.get(url, timeout=4)
    print(result.url) # the url used to get the object
    print(result.text) # the text content
    return result.text


def find_ids(text):
    return ids


def get_letters(base_url, ids):
    return letter, id


def save_letter(letter, id):


def main(base_url, query):
    text = get_page(base_url, query)

main(base_url, query)



