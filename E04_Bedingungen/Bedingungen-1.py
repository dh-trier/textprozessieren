
mylist = ["All", "models", "are", "wrong", ",", "but", "some", "are", "useful", "."]


# TEIL 1: for-Schleife mit Bedingungen =========================




# Einfache for-Schleife mit if-Bedingung

for item in mylist:
    if item not in [",", "."]:
        print(item)
    else:
        print("PUNC")


# For-Schleife mit if und else

for item in mylist:
    if item not in [",", "."]:
        print(item)
    else:
        print("PUNC")


# For-Schleife mit if und erneutes if (beide werden geprüft)

for item in mylist:
    if item not in ["are", "some"]:
        print(item)
    if "o" in item:
        print(item)


# For-Schleife mit if und elif: elif wird nur geprüft, wenn if nicht zutrifft. 

for item in mylist:
    if item not in ["are", "some"]:
        print(item)
    elif "o" in item:
        print(item)


# Zwei Bedingungen in einem if-Statement (Alternative: or)

for item in mylist: 
    if len(item)==3 or item in ["wrong", "useful"]: 
        print(item)



# Zwei Bedingungen in einem if-Statement (Kombination: and)

for item in mylist: 
    if len(item)==5 and item in ["wrong", "useful"]: 
        print(item)




