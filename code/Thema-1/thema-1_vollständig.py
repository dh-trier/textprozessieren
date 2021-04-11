

textdatei = "Kraus.txt"
with open(textdatei, "r", encoding="utf8") as infile:
    text = infile.read()
    print(text[0:100])
    zeichenzahl = len(text)
    print(zeichenzahl)