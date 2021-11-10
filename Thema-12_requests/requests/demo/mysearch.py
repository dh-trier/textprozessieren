#!/usr/bin/env python3


"""
# Script to search for words in a text collection.
"""

# ========================================
# Imports
# ========================================

# Generic imports
from os.path import join
import os
import glob
import pandas as pd
import numpy as np

# Specific imports
import re
import requests as rq
import html
from collections import Counter
import shutil
import csv


# ========================================
# Parameters
# ========================================

wdir = ""
txtfolder = join(wdir, "txt", "")
#query = "houses?"
query = "\W(go|goes|went|gone)\W"
query = "\Wf[\w]{3,4}r\W"


# ========================================
# Functions 
# ========================================


def get_textid(textfile): 
    textid, ext = os.path.basename(textfile).split(".")
    #print(textid)
    return textid


def get_text(textfile): 
    with open(textfile, "r", encoding="utf8") as infile: 
        text = infile.read() 
        text = re.sub("\n", " <br/> ", text)
        text = re.sub("\t", "   ", text)
        return text


def get_wordcount(text, query, textid): 
        count = re.findall(query, text) 
        count = len(count)
        if count != 0:
            print("\n===\nFound \'" + str(query) + "\' " + str(count) + " times in text " + textid + ".")
        return count


def get_hits(text, query): 
    hits = re.findall(query, text)
    hits = list(set(hits))
    print("Found the following items:", " ".join(hits))
    return hits


def get_context(text, textid, query): 
    hits = re.finditer(query, text)
    print("Found the following hits shown in context:")
    contexts = []
    for hit in hits: 
        hitstart = hit.start()
        hitend = hit.end()
        context = str(textid) + "\t" + str(hitstart) +"\t"+ text[hitstart-25:hitstart]+"\t"+text[hitstart:hitend]+"\t"+text[hitend:hitend+25] 
        print(context)
        contexts.append(context)
    return contexts


def save_results(allcontexts, query): 
    queryfilename = "query_"+str(query)+".csv"
    with open(queryfilename, "a") as outfile: 
        for item in allcontexts: 
            outfile.write(item+"\n")
    


# ========================================
# Main function 
# ========================================

def main(wdir, txtfolder, query): 
    allcontexts = []
    for textfile in glob.glob(txtfolder + "*.txt"): 
        textid = get_textid(textfile)
        text = get_text(textfile)
        count = get_wordcount(text, query, textid)
        if count != 0: 
            hits = get_hits(text, query)
            contexts = get_context(text, textid, query)
            allcontexts.extend(contexts)
    save_results(allcontexts, query)
    
    
main(wdir, txtfolder, query)
