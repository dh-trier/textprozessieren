# Prinzip von Schleifen (= teils Wiederholung)

# Unsere "Daten" für heute

input = "All models are wrong, but some are useful."
print(type(input))


# (a) for-Schleife
# Iteration über eine Sequenz von Objekten.
# Nützlich für alle sequentiellen Datentypen: string, liste, etc. 


for item in input:
    print(item)


# (b) Bedingungen (if / else)

for item in input:
    if item == "m":
        print(item)


for item in input:
    if item == "m":
        print("one character:", item)
    elif item == "n":
        print("other character:", item)
    else:
        print("rest")


# Es geht auch mit einer Liste

input = ["All", "models", "are", "wrong", ",", "but", "some", "are", "useful", "."]
print(type(input))

for item in input:
    if item not in ",.":
        print(item)
    else:
        print("PUNC")



# Das "break"-Kommando (aus dem Klein-Buch)

essbares = ["Nüsse", "Tomaten", "Spinat", "Apfel"]
for gericht in essbares:
    if gericht == "Spinat":
        print("Ich mag keinen Spinat.")
    else:
        print("Lecker,", gericht)
print("Jetzt bin ich satt.")


essbares = ["Nüsse", "Tomaten", "Spinat", "Apfel"]
for gericht in essbares:
    if gericht == "Spinat":
        print("Ich mag keinen Spinat.")
        break
    print("Lecker,", gericht)
else:
    print("Glück gehabt, kein Spinat.")
print("Jetzt bin ich satt.")




# (c) while-Schleife

value = 2
while value < 15:
    print(value)
    value += 3

string = "ab"
while len(string) < 100:
    print("1", string, len(string))
    string = string * len(string)
    print("2", string, len(string))
print("Ende.")

    
    
    





