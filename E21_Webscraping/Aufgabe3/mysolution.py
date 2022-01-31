#!/usr/bin/env python3


"""
# Musterlösung für Aufgabe 3. 
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
import requests as rq


# ========================================
# Parameters
# ========================================

baseurl_search = "https://archiveofourown.org/works/search?"
baseurl_works = "https://archiveofourown.org/works/" # + "?view_full_work=true"

wordcount = 5000
language = "English"
fandom = "Lord+of+the+Flies+-+William+Golding"

htmlfolder = "html"


# ========================================
# Functions: Teil 1 (Werk-Identifier einsammeln)
# ========================================

def build_queryurl(wordcount, language, fandom):
    if language == "English":
        lang = str(1)
    query = "&work_search%5Bword_count%5D=%3E" + str(wordcount) + "&work_search%5Blanguage_id%5D=" + str(lang) + "&work_search%5Bfandom_names%5D=" + fandom
    #print(query)
    return query


def get_first_url(baseurl_search, query):
    queryurl = baseurl_search + query
    print(queryurl)
    try:
        result = rq.get(queryurl + query, timeout=40)
        first_page = result.text
    except:
        first_page = "ERROR"
    #print(first_page)
    return first_page


def get_all_urls(baseurl_search, query, first_url):
    result = re.search("(\d+) Found", first_url)
    num_items = int(result.group(1))
    print("number of items found:", num_items)
    num_pages = (num_items // 20) + 1
    print("number of pages:", num_pages)
    further_query_urls = []
    for i in range(1, num_pages+1):
        current_url = baseurl_search + "page=" + str(i) + query
        print(current_url)
        further_query_urls.append(current_url)
    print(len(further_query_urls))
    return further_query_urls 


def get_workids(url):
    try:
        result = rq.get(url, timeout=40)
        html = result.text
    except:
        html = "ERROR"
    #print(html)
    workids = re.findall("<a href=\"/works/(\d+)\">", html)
    #print(workids)
    return workids


def collect_ids(baseurl_search, wordcount, language, fandom):
    query = build_queryurl(wordcount, language, fandom)
    first_url = get_first_url(baseurl_search, query)
    all_urls = get_all_urls(baseurl_search, query, first_url)
    all_workids = []
    for url in all_urls:
        workids = get_workids(url)
        all_workids.extend(workids)
    print(all_workids)
    print("number of work ids:", len(all_workids))
    return all_workids
        
all_workids = collect_ids(baseurl_search, wordcount, language, fandom)


# ========================================
# Functions: Teil 2 (HTML der Werke herunterladen)
# ========================================


def get_fullurl(baseurl_works, workid):
    fullurl = baseurl_works + str(workid) + "?view_full_work=true"
    return fullurl


def download_html(fullurl):
    try:
        result = rq.get(fullurl, timeout = 40)
    except:
        print("error downloading work")
        html = ""
    html = result.text
    return html


def save_html(html, workid, htmlfolder):
    filename = join(htmlfolder, str(workid) + ".html")
    with open(filename, "w", encoding="utf8") as outfile:
        outfile.write(html)
    


def get_html(baseurl_works, all_workids, htmlfolder):
    for workid in all_workids:
        fullurl = get_fullurl(baseurl_works, workid)
        html = download_html(fullurl)
        print(workid, len(html))
        save_html(html, workid, htmlfolder)
        
get_html(baseurl_works, all_workids, htmlfolder)








