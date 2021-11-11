
# Teil 1: while-Schleife ==========================0


# Beispiel 1 


counter = 0
while counter < 5:
    print("Bedingung wahr", counter)
    counter +=1
print("Bedingung nicht mehr wahr.", counter)




# Beispiel 2

string = "ab"
while len(string) < 100:
    print("1", string, len(string))
    string = string * len(string)
    print("2", string, len(string))
print("Ende.")

    
    


# (1) while und else

"""
- while-loop läuft, solange Bedingung wahr ist.
- else-statement wird ausgeführt, wenn Bedingung nicht wahr ist.

else-statement steht in erster Einrückung, weil while und else
auf der gleichen logischen Ebene sind.
(Aber: Das print-Statement könnte auch direkt auf der
äußersten Einrückungs-Ebene stehen und würde nach dem while-Loop
ausgeführt.)
"""

"""
counter = 0
while counter < 5:
    print("Bedingung wahr", counter)
    counter +=1
print("Bedingung nicht mehr wahr.", counter)
"""

# (2) while und else mit break

"""
Standard-Fall:
- while-loop läuft, solange Bedingung wahr ist.
- else-statement wird ausgeführt, wenn Bedingung nicht wahr ist.

Das break-statement kommt hinzu, ändert aber nichts daran,
dass das else-Statement auf der Ebene des while-Statements
stehen muss. In diesem Fall bricht die while-Schleife ab,
bevor der nächste Teil der Schleife ausgeführt wird,
hier also bevor der counter hochgesetzt wird. 
"""


    
essbares = ["Nüsse", "Tomaten", "Spinat", "Apfel"]    
for gericht in essbares:
    if gericht == "Spinat":
        print("Ich mag keinen Spinat.")
    else: 
        print("Lecker,", gericht)


# Mit break

#- break (typischerweise mit if) bricht loop ab, obwohl noch items da wären.


essbares = ["Nüsse", "Tomaten", "Spinat", "Apfel"]    
for gericht in essbares:
    if gericht == "Spinat":
        print("Ich mag keinen Spinat.")
        break
    else: 
       print("Lecker,", gericht)




# Außerhalb des Loop stehendes "else": Wird nur ausgeführt, wenn kein break vorkam

essbares = ["Nüsse", "Tomaten", "Spinat", "Apfel"]    
for gericht in essbares:
    if gericht == "Spinat":
        print("Ich mag keinen Spinat.")
        break
    else: 
        print("Lecker,", gericht)
else: 
    print("Glück gehabt, kein Spinat dabei gewesen.")




# "else" bedeutet hier quasi: Wenn der break nicht aktiviert wurde.
# Es steht außerhalb des loops, weil es ja erst nach dem
# Loop ausgeführt werden soll. 
