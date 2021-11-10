#!/usr/bin/env python3


"""
Skript, mit dem Texte und Metadaten von AO3 heruntergeladen werden.

- A03 = Archive of Our Own, fanfiction-site: https://archiveofourown.org/
- Python library "requests": https://docs.python-requests.org/en/master/
  (Version 2.25.1 bitte über Thonny installieren) 

Arbeitsschritte
- Suchabfrage überlegen und im Webinterface vornehmen
- Suchabfrage mit requests "nachbauen"
- Liste der Text-IDs einsammeln
- Alle Texte mit den entsprechenden IDs herunterladen
- Metadaten aus den HTML-Dateien extrahieren und abspeichern ("metadata.tsv")
- Volltext aus den HTML-Dateien extrahieren und abspeichern ("/corpus")
- => Dann ist eine Analyse des Korpus möglich.


Suchabfrage: https://archiveofourown.org/menu/search
- Deutsche Texte
- 10000-20000 Wörter Länge
- Harry Potter-Fandom
- No Crossovers
- No Archive Warnings

https://archiveofourown.org/works/30339960?view_full_work=true

"""

# ========================================
# Imports
# ========================================

# Generic imports
from os.path import join
import os

# Specific imports
import re
import requests


# ========================================
# Functions 
# ========================================


def get_ids(): 
    """
    Based on a specific search query encoded in the query body,
    finds the text identifiers for all matching texts.
    Returns them as a list and saves the list to a text file. 
    """
    query = "https://archiveofourown.org/works/search?commit=Search"
    pages = 3
   
    all_ids = []
    for page in range(1,pages+1): 
        print(page)
        parameters = {"utf8" : "%E2%9C%93",
                  "page" : str(page),
                  "work_search[complete]": "T",
                  "work_search[crossover]" : "F",
                  "work_search[fandom_names]" : "Harry+Potter+-+J.+K.+Rowling",
                  "work_search[language_id]" : "de",
                  "work_search[single_chapter]" : "0",
                  "work_search[sort_column]" : "_score",
                  "work_search[sort_direction]" : "desc",
                  "work_search[word_count]" : "10000-20000",
                  "work_search[archive_warning_ids][]" : "16"}
        try:
            queryresponse = requests.get(query, params=parameters, timeout=4)
            #print(queryresponse.url)
            queryhtml = queryresponse.text
            #print(queryhtml)
        except:
            print("Error receiving HTML")
        try: 
            ids = re.findall(r"<a href=\"/works/(\d*?)\">", queryhtml)
            print(ids)
            all_ids.extend(ids)
            #print(len(all_ids))
        except: 
            print("Error extracting IDs")
    print(len(all_ids), "ids collected")
    all_ids = "\n".join(all_ids)
    with open("ids.txt", "w") as output:
        output.write(all_ids)
    return all_ids


def load_ids():
    """
    Loads the saved text file with text identifiers relevant to the query. 
    Gives them back as a list.
    (Only used when not running the whole pipeline at once.)
    """
    all_ids = []
    with open("ids.txt", "r") as infile: 
        all_ids = infile.read().split("\n")
        all_ids = [item for item in all_ids if item]
        #print(all_ids)
        #print(len(all_ids))
        return all_ids


def get_html(all_ids): 
    """
    For each work in the list of work identifiers, downloads the
    complete HTML file with the metadata and full HTML text.
    Saves this file to disk in a separate folder.
    """
    # Parameters
    a3o_base = "https://archiveofourown.org/"
    htmlfolder=join("html", "")
    # Make sure folder exists
    if not os.path.exists(htmlfolder):
        os.makedirs(htmlfolder)
    # Download HTML (with slice for testing only!)
    for item in all_ids[0:2]: 
        url = a3o_base + "works/" + item + "?view_full_work=true"
        #print(url)
        filename = join(htmlfolder, "a3o-"+item+".html")
        print(filename)
        response = requests.get(url, timeout=4)
        html = response.text
        with open(filename, "w") as outfile: 
            outfile.write(html)



# ========================================
# Main function 
# ========================================

def main():
    #all_ids = get_ids()
    all_ids = load_ids()
    html = get_html(all_ids) 
  
main()
