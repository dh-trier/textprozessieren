"""
Programmierung einer Volltextsuche mit RegEx und KWIC-Ansicht.
Hier für mehrere Texte in einem Ordner und ein paar Erweiterungen.

===
Aufgabe: Programmieren einer parametrisierten Suchfunktion mit KWIC-Ansicht.

Schreiben Sie ein Programm, das es erlaubt, in mehreren Textdateien zu suchen.
Das Programm soll als Output einerseits eine KWIC-Ansicht anzeigen.
Diese KWIC-Ansicht soll den Textname, eine Positionsangabe, das gefundene Wort und den Kontext anzeigen. 
Das Programm soll außerdem diese Suchergebnisse auch als CSV-Datei abspeichern.
Als Parameter soll die Suche nach einem ganzen Wort oder einem beliebigen String möglich sein.
Als weiter Parameter soll die Breite des Kontext-Fensters in Zeichen angegeben werden können.
Das Suchwort und die Parameter-Setzung sollen interaktiv von den Usern abgefragt werden. 
Nutzen Sie möglichst bekannte Techniken: list (oder dict), glob, DataFrame, input() etc.
Planen Sie das Programm mit einem Prozessmodell, das auch die Gliederung in Funktionen beinhaltet. 
=== 

"""





# === Funktionen ===

def read_textfile(textfile):
    """
    Öffnet und liest eine plain text-Datei ein.
    Input: txt-Datei in UTF8-Kodierung. 
    Output: Textinhalt als String. 
    """
    # return text


def search_text(text, query, qtype):
    """
    Durchsucht den Text nach einem Suchbegriff.
    Query wird als Einzelwort oder reiner String gebildet. 
    Input: Text als String, Query als String.
    Output: Ein Iterator mit 1 match object pro Treffer. 
    """
    # return results


def display_kwic(text, textname, results, window):
    """
    Shows the results as a KWIC view.
    Collects the results as a list of lists.
    Input: Text and results as iterator of match objects.
    Output: List of lists. 
    """
    # return kwiclines_text
        

def save_kwic(kwiclines_corpus, query, filename):
    """
    Speichert die gesammelten Treffer für alle Text als CSV ab.
    Input: Liste von Listen, eine Liste pro Treffer.
    Output: DataFrame, der als CSV abgespeichert wird. 
    """
    # save            

# === Main ===

def main(textfolder, query, qtype, window):
    """
    Koordiniert den Prozess
    - Schleife über alle Texte
    - Parameter vom User (Suchstring, Querytype, KWIC-Breite)
    































# === Importe ===

import re
import pandas as pd
import glob
import os
from os.path import join


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


def search_text(text, query, qtype):
    """
    Durchsucht den Text nach einem Suchbegriff.
    Query wird als Einzelwort oder reiner String gebildet. 
    Input: Text als String, Query als String.
    Output: Ein Iterator mit 1 match object pro Treffer. 
    """
    if qtype == "wort":
        query = re.compile(r"\b" + query + r"\b", re.I)
    elif qtype == "string": 
        query = re.compile(query, re.I)
    results = re.finditer(query, text)
    return results


def display_kwic(text, textname, results, window):
    """
    Shows the results as a KWIC view.
    Collects the results as a list of lists.
    Input: Text and results as iterator of match objects.
    Output: List of lists. 
    """
    kwiclines_text = []
    for item in results:
        preceding = text[item.start()-window:item.start()]
        following = text[item.end():item.end()+window]
        hit = item.group()
        position = item.start()
        print(textname, position, preceding, hit, following)
        kwicline = [textname, position, preceding, hit, following]
        kwiclines_text.append(kwicline)
    return kwiclines_text
        

def save_kwic(kwiclines_corpus, query, filename):
    """
    Speichert die gesammelten Treffer für alle Text als CSV ab.
    Input: Liste von Listen, eine Liste pro Treffer.
    Output: DataFrame, der als CSV abgespeichert wird. 
    """
    print("\nTotal number of results ", len(kwiclines_corpus))
    columns = ["text", "position", "preceding", "hit", "following"]
    kwiclines = pd.DataFrame.from_records(kwiclines_corpus, columns=columns)
    with open(filename, "w+", encoding="utf8") as outfile:
        kwiclines.to_csv(filename, sep="\t")
        print("\nSaved file \'" + str(filename) + "\' to disk.")
            

# === Main ===

def main(textfolder, query, qtype, window):
    kwiclines_corpus = []
    filename = "kwic_" + str(query) + "_" + str(qtype) + ".csv"
    for textfile in glob.glob(textfolder): 
        textname = os.path.basename(textfile).split(".")[0]
        text = read_textfile(textfile)
        results = search_text(text, query, qtype)
        kwiclines_text = display_kwic(text, textname, results, window)
        kwiclines_corpus.extend(kwiclines_text)
    save_kwic(kwiclines_corpus, query, filename)

main(join("corpus", "*.txt"), "sich", "wort", 40)  
# Parameter: Korpusordner, Suchstring, Querytpe (wort/string), KWIC-Breite)


"""
Interessante Suchbegriffe:

art (als wort oder string)
ohne (als wort oder string)
sich (als wort oder string)

"""

    
    
    