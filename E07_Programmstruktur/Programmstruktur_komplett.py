# Beispielaufgabe

# Create simple text

# Wir möchten:
# - eine Textdatei öffnen
# - in lowercase verwandeln
# - die Interpunktion löschen
# - Die Textdatei in einer neuen Datei speichern

# Das ganz soll auch für mehrere Dateien in einer Schleife funktionieren

# Wie würden Sie das Ganze aufbauen? ( Diskussion ) 

# ========================

# Importe

from glob import glob as gg
from os.path import join


# Parameter

datenpfad = join("daten", "*.txt")


# Funktionen

def read_textfile(textdatei):
    with open(textdatei, "r", encoding="utf8") as infile:
        text = infile.read()
        return text


def make_lowercase(text):
    lowertext = text.lower()
    return lowertext


def remove_punctuation(lowertext):
    cleantext = ""
    punctuation = ",.;!?"
    for item in lowertext:
        if item not in punctuation:
            cleantext += item
    return cleantext


# Main

def main(datenpfad):
    for textdatei in gg(datenpfad):
        print(textdatei)
        text = read_textfile(textdatei)
        lowercase = make_lowercase(text)
        cleantext = remove_punctuation(lowercase)
        print(cleantext)
    print("Fertig.")

main(datenpfad)

















