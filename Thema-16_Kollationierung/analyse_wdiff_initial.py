"""
Skript to retrieve differences from a wdiff output file. 
"""


import re


def load_file(inputfile):
    """
    Lädt das Inputfile mit dem wdiff Output. 
    """
    return wdiff


def find_diffs(wdiff):
    """
    Findet und sammelt die Stellen mit Unterschieden. 
    """
    return diffs


def analyse_diffs(diffs):
    """
    Klassifiziert die Unterschiede. 
    """
    return adiffs


def save_diffs(adiffs):
    """
    Speichert die Unterschiede in einer CSV-Datei ab. 
    """
    print("All done.")
    

def main():
    """
    Koordinierungsfunktion.
    """
    inputfile = "wdiffed.txt"
    wdiff = load_file(inputfile)
    diffs = find_diffs(wdiff)
    adiffs = analyse_diffs(diffs)
    save_diffs(adiffs)

if __name__ == "__main__":
    main()
