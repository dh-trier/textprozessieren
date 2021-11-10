

textdatei = "Kraus.txt"
with open(textdatei, "r", encoding="utf8") as infile:
    text = infile.read()
    print(text[0:100])
    zeichenzahl = len(text)
    print(zeichenzahl)
    counter = 0
    suchzeichen = "n"
    for item in text:
        if item == suchzeichen:
            counter = counter + 1
    print("Das Suchzeichen " + suchzeichen + "kommt im Text " + str(counter) + " Mal vor.")
            
        