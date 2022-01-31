# Import

import glob
import re
from os.path import join

# Funktionen

# Funktion-Definition: Text öffnen/lesen
# Funktion-Defintion: Text bereinigen: lowercase, Interpunktion löschen, Umlaute ersetzen.
# Funktion-Definition: Text abspeichern.


# Main
def main()
    for Datei in glob.glob(join("daten", "*.txt")): 
        rawtext = funktion1(Datei)
         cleantext = funktion2(rawtext)
         funktion3(cleantext)
main()
