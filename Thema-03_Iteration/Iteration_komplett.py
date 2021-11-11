# Iteration

# Unsere "Daten" für heute

mystr = "All models are wrong, but some are useful."
print(type(input))

mylist = ["All", "models", "are", "wrong", ",", "but", "some", "are", "useful", "."]
print(type(input))


# (a) for-Schleife
# Iteration über eine Sequenz von Objekten.
# Nützlich für alle sequentiellen Datentypen: string, liste, etc. 


for item in mystr:
    print(item)


for item in mylist:
    print(item)



# str zu list

print(mystr.split(" "))

for item in mystr.split(" "): 
    print(item)


# split mit regex

import re

print(re.split("\W+", mystr))

for item in re.split("\W+", mystr): 
    print(item)


# Dicts are not iterable per se, but can be made to be so.    

mydict = {1: "All", 3 : "are", 2: "models", 5 : ".", 4 : "wrong"}
print(type(mydict))

for key,value in mydict.items(): 
    print(key, value)

for value in mydict.values(): 
    print(value)

for key in mydict.keys(): 
    print(key)


