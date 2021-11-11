# (1)  Beispiele für import

# Bibliotheken / Module können strukturiert sein

# - Modul
# - Funktion1
# - Funktion2
# - Submodul1
# - Funktion1-1
# - Funktion1-2


# (a) Ganze Bibliothek importieren

import os

filepath = os.path.join("daten", "models.txt")
print("a", filepath)


# (b) Modul mit "Nickname" importieren 

import os as operatingsystem

filepath = operatingsystem.path.join("daten", "models.txt")
print("b", filepath)


# (c) Submodul importieren

import os.path

filepath = os.path.join("daten", "models.txt")
print("c", filepath)


# (d) Submodul importieren

import os.path as osp

filepath = osp.join("daten", "models.txt")
print("d", filepath)


# (e) Funktion aus Submodul importieren

from os.path import join

filepath = join("daten", "models.txt")
print("e", filepath)
