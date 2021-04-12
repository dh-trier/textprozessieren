

from os.path import join

textdatei = join("Kraus.txt")

with open(textdatei, "r", encoding="utf8") as infile:
    text = infile.read()
    print(text)
    print(type(text))
    print(len(text))