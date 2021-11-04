textdatei = "data/Kraus.txt"

with open(textdatei, "r", encoding="utf8") as infile:
    text = infile.read()
    print(text[0:50])
    print(text.lower()[0:50])
    print(type(text))
    print(len(text))
