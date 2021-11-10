"""
Programmierung einer Volltextsuche mit RegEx und KWIC-Ansicht.
Hier für einen Text. 

"""


# === Importe ===

import re
import pandas as pd


# === Funktionen ===

def read_textfile(textfile):
    """
    Öffnet und liest eine plain text-Datei ein.
    Input: txt-Datei in UTF8-Kodierung. 
    Output: Textinhalt als String. 
    """
    with open(textfile, "r", encoding="utf8") as infile:
        text =  infile.read()
        #print(text[0:100])
        return text


def search_text(text, query):
    """
    Durchsucht den Text nach einem Suchbegriff.
    Input: Text als String, Query als String.
    Output: Ein Iterator mit 1 match object pro Treffer. 
    """
    results = re.finditer(query, text, re.I)
    print("Perfomed query \'" + str(query) + "\' on text.\n")
    #for item in results:
    #    print(item)
    return results


def display_kwic(text, results):
    """
    Shows the results as a KWIC view.
    Collects the results as a list of lists.
    Input: Text and results as iterator of match objects.
    Output: List of lists. 
    """
    kwiclines = []
    for item in results:
        preceding = text[item.start()-30:item.start()]
        following = text[item.end():item.end()+30]
        hit = item.group()
        print(preceding, hit, following)
        kwicline = [preceding, hit, following]
        kwiclines.append(kwicline)
    return kwiclines
        

def save_kwic(kwiclines, query, filename):
    columns = ["preceding", "hit", "following"]
    kwiclines = pd.DataFrame.from_records(kwiclines, columns=columns)
    with open(filename, "w+", encoding="utf8") as outfile:
        kwiclines.to_csv(filename, sep="\t")
        print("\nSaved file \'" + str(filename) + "\' to disk.")
            


# === Main ===

def main(textfile, query):
    text = read_textfile(textfile)
    filename = "kwic_" + str(query) + ".csv"
    results = search_text(text, query)
    kwiclines = display_kwic(text, results)
    save_kwic(kwiclines, query, filename)

main("Münchhausen.txt", "sowohl")
    
    
    
    