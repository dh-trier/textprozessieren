"""
Skript, um eine Term-Dokument-Matrix für ein Corpus zu erstellen. 
"""


import pandas as pd
from collections import Counter
from os.path import basename
from os.path import join
import glob
import re
import numpy as np



def read_textfile(textfile):
    """
    Textdatei (plain text) einlesen.
    Output: string. 
    """
    with open(textfile, "r", encoding="utf8") as infile:
        text = infile.read()
    return text


def get_termfreqs(text):
    """
    Häufigkeit jedes Wortes im Text erheben.
    Schließt hier die Tokenisierung ein.
    Returns: dict. 
    """
    text = re.split("\W+", text)
    termfreqs = Counter(text)
    return termfreqs


def save_tdm(tdmdata):
    """
    Transformiert das dict of dicts zu DataFrame.
    Ersetzt fehlende Werte durch 0. 
    Berechnet die Summe pro Type (Sortierung). 
    Speichert den DataFrame als TSV-Datei ab.
    """
    tdmdata = pd.DataFrame(tdmdata)
    tdmdata.fillna(0, inplace=True)
    tdmdata["totals"] = np.sum(tdmdata, axis=1)
    tdmdata.sort_values(by="totals", ascending=False, inplace=True)
    with open("doyle-tdm.tsv", "w", encoding="utf8") as outfile:
        tdmdata.to_csv(outfile, sep="\t")


def main():
    corpuspath = join("corpus", "*.txt")
    tdmdata = {}
    for textfile in glob.glob(corpuspath):
        textid = basename(textfile).split(".")[0]
        text = read_textfile(textfile)
        termfreqs = get_termfreqs(text)
        tdmdata[textid] = termfreqs
    save_tdm(tdmdata)

main()