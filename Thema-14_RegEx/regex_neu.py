"""
Session zu Regulären Ausdrücken.

Dokumentation zum Modul "re" hier: https://docs.python.org/3.7/library/re.html

Sehr gute Einführung: https://docs.python.org/3.7/howto/regex.html#regex-howto

==============

Grundidee: Ein RegEx definiert ein Muster für eine Zeichenfolge, nach dem in Strings gesucht werden kann.

Themen
- Funktionen von re für die Suche
- Quantifier und "Greediness"
- Flags
- Zeichen-Klassen
- Gruppen im Suchergebnis
- Suchen/Ersetzen


"""

# Importe
import re


# Daten einlesen: Hier als String (statt als JSON-Objekt oder XML)
with open("programmieren.rdf", "r", encoding="utf8") as infile:
    data = infile.read()
    #print(type(data)) # Sollte "str" sein
    #print(data)







print(len(results), "Ergebnisse:", results)


