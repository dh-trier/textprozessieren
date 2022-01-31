# Importe

import re
import os
from os.path import join
from glob import glob as gg


# Funktionen

def read_textfile(textfile):
    """Opens a textfile and reads the content.
    Returns the file content as a string."""
    with open(textfile, "r", encoding="utf8") as infile:
        text  = infile.read()
    return text


def clean_text(text):
    """Simplifies a text, removing anything except words.
    Returns a string."""
    text = text.lower()
    text = re.sub("ſ", "s", text)
    text = re.sub("-\n", "", text)
    text = re.sub("\n", " ", text)
    text = re.sub(",", "", text)
    text = re.sub(r"\.", "", text)
    text = re.sub(";", "", text)
    text = re.sub(r"\(", "", text)
    text = re.sub(r"\)", "", text)
    text = re.sub(r"\d", "", text)
    text = re.sub(" {2,6}", " ", text)    
    # print(text)
    return text


def get_numvowels(text):
    """Counts the vowels contained in a string.
    Returns an integer. """
    vowels = "aeiouöüä"
    counter = 0
    for char in text:
        if char in vowels:
            counter +=1
    return counter


def get_textstats(text):
    """Calculates some basic text statistics.
    Length in chars, in words; number of vowels. 
    Returns a list of integers."""
    len_zeichen = len(text)
    len_worte = len(text.split(" "))
    num_vokale = get_numvowels(text)
    labels = ["len_zeichen", "len_worte", "num_vokale"]
    results = [len_zeichen, len_worte, num_vokale]
    results = dict(zip(labels, results))
    #print(results)
    return results
    
   

# Main

def main(textfolder):
    allresults = {}
    for textfile in gg(textfolder):
        filename = os.path.basename(textfile).split(".")[0]
        text = read_textfile(textfile)
        text = clean_text(text)
        textstats = get_textstats(text)
        allresults[filename] = textstats
    print(allresults)

main(join("texte", "*.txt"))



