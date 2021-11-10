"""
Skript to retrieve differences from a wdiff output file.
Anwendungsbeispiel: https://christofs.github.io/martian/#/
"""


import re
import Levenshtein as ld
import pandas as pd


def load_file(inputfile):
    """
    Lädt das Inputfile mit dem wdiff Output.
    Input: TXT-Datei
    Output: String 
    """
    with open(inputfile, "r", encoding="utf8") as infile:
        wdiff = infile.read()
        #print(wdiff[0:100])
    return wdiff


def find_diffs(wdiff):
    """
    Findet und sammelt die Stellen mit Unterschieden. 
    """
    diffs = re.findall(r"\[-(.*?)-\] \{\+(.*?)\+\}", wdiff)
    #print(diffs[0:10])
    return diffs


def analyse_diffs(diffs):
    """
    Klassifiziert und beschreibt die Unterschiede. 
    """
    adiffs = {}
    counter = 0
    for item in diffs:
        old = item[0]
        new = item[1]
        type = ""
        # Get Levenshtein distance
        ldist = ld.distance(old, new)
        # Identify minor changes (Prinzip: Transformation + Test auf Gleichheit)
        if re.sub("['’,\- ]", "", old) == re.sub("['’,\- ]", "", new):
            print(old, new)
            type = "minor"
        else:
            type = "other"
        # Collect info
        adiffs[counter] = {"old":old, "new":new, "ldist":ldist, "type":type}
        counter +=1
    print(adiffs)
    return adiffs


def save_diffs(adiffs):
    """
    Transformation zu DataFrame und Sortierung. 
    Speichert die Unterschiede in einer CSV-Datei ab.
    """
    adiffs = pd.DataFrame(adiffs).T
    adiffs.sort_values(by=["type", "ldist"], ascending=False, inplace=True)
    print(adiffs.head())
    with open("adiffs.csv", "w", encoding="utf8") as outfile:
        adiffs.to_csv(outfile, sep="\t")
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




"""
Denkbare Erweiterungen:

- Alles gleich anfangs in lowercase, um einige trivialen Unterschiede auszuschließen.
- Verbesserung der Erkennung von "minor": weitere unwesentliche Zeichen, bspw. "–".
- Weitere Typen von Unterschieden definieren bzw. feinere Unterschiede machen.
- Beispiele: type "minor" aufsplitten nach Whitespace, Interpunktion, Trennzeichen.
- Beispiele: Unterscheiden, ob ein String länger oder kürzer wird. 
- Statistiken über die Unterschiede: bspw. durchschnittliche Levenshtein-Distanz pro Typ.
- Statt die Unterschiede nur durchzuzählen, auch die Position im Text festhalten. 




"""