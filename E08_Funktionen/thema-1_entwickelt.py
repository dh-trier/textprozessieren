textdatei = "data/Kraus.txt"

with open(textdatei, "r", encoding="utf8") as infile:
    text = infile.read()
    print(text[0:50])
    print(text.lower()[0:50])
    print(type(text))
    print(len(text))


# =====================

import os
from os.path import join
from os.path import join as oj

textdatei = oj("data", "Kraus.txt")

with open(textdatei, "r", encoding="utf8") as infile:
    text = infile.read()
    print(text[0:50])
    print(text.lower()[0:50])
    print(type(text))
    print(len(text))


# ===============================

import glob
from glob import glob as gg

for file in gg(join("data", "*.txt")):
    #print(file)
    with open(file, "r", encoding="utf8") as infile:
        text = infile.read()
        print(text[0:50])
    
            


