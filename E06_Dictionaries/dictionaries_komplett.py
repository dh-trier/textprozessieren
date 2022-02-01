"""
EINFÜHRUNG IN DICTIONARIES

Alle Infos: https://docs.python.org/3.7/library/stdtypes.html#mapping-types-dict

Oder im Klein-Buch: Kapitel 6

"""

# Datentypen, die Sie schon kennen
# int, float?, list

# Neuer Datentyp: dict ("dictionary")
# Grundidee: Mehrere Schlüssel-Wert-Paare

mydict = {"name" : "kai lan", "farbe" : "grün", "größe (cm)" : 12}

# Ein paar Eigenschaften
# - Man beachte die Syntax: {} : ,
# - keine bedeutungsvolle Reihenfolge
# - kein sequenzieller Datentyp! (keine Iteration)
# - Die values können beliebige Datentypen sein
# - Die keys können strings, ints, floats sein, aber keine lists oder dicts. 
# - man greift über die "keys" auf die "values" zu
# - man kann dicts nach und nach Aufgbauen (Zuweisung über key)


mydict = {} # leeres dict
print(mydict, len(mydict))
mydict["name"] = "kai lan"
print(mydict, len(mydict))


# Zugriff über die keys

mydict = {"name" : "kai lan", "farbe" : "grün", "größe (cm)" : 12}
print(mydict["farbe"])


# Zugriff mit einem nicht-existenten key
# => "KeyError" (klar!)

#print(mydict["essbar"]) 



# Per Zuweisung einen vorhandenen Wert ändern

mydict["farbe"] = "dunkelgrün"
print(mydict["farbe"])


# Per Zuweisung einen neue key-value-Paar hinzufügen

mydict["essbar"] = True
print(mydict)


# Verschachtelung
# Die Werte können bspw. auch listen sein
# Vor allem aber: Die Werte können auch den Datentyp dict haben!
# Diese Struktur kann für die Datenhaltung sehr nützlich sein.

mydict = {"pflanze 1" : {"name" : "kai lan", "farbe" : "grün"},
          "pflanze 2" : {"name" : "Tomate", "farbe" : "rot"}}




# dict aus zwei Listen erstellen

namen = ["Tomate", "Paprika", "Aubergine"]
farben = ["rot", "bunt", "schwarz"]

gemüsefarben = dict(zip(namen, farben))
print(gemüsefarben)


# Methoden von dict
# Es gibt eine Menge Methoden von dict, hier nur ein paar
# nützliche Beispiele

# .keys() - Menge der keys
print(gemüsefarben.keys())
# leicht in eine Liste überführbar
print(list(gemüsefarben.keys()))
# Ebenso .values()
print(gemüsefarben.values())


# .pop() - Entfernt ein key-value Paar nach dem key

gemüsefarben.pop("Aubergine")
print(gemüsefarben)


# .update() - Fügt ein Dictionary hinzu
# Achtung: Überschreibt ggfs. schon vorhandenen Werte!

gemüsefarben = {"Tomate" : "rot", "Aubergine" : "schwarz"}
mehrgemüse = {"Paprika" : "bunt", "Aubergine" : "violett"}

gemüsefarben.update(mehrgemüse)
print(gemüsefarben)

# Die Reihenfolge, in der man die Kombination vornimmt,
# macht hier also einen Unterschied!



# Über dicts kann man nicht iterieren, oder doch?
# Nur mit der Methode ".items()"

for key,value in gemüsefarben.items():
    print(key, value)














