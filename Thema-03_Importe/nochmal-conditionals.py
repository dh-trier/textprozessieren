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
- break (typischerweise mit if) bricht loop ab,
  ohne dass else-statement ausgeführt wird,.

Das break-statement kommt hinzu, ändert aber nichts daran,
dass das else-Statement auf der Ebene des while-Statements
stehen muss. In diesem Fall bricht die while-Schleife ab,
bevor der nächste Teil der Schleife ausgeführt wird,
hier also bevor der counter hochgesetzt wird. 
"""

"""

counter = -5
while counter < 5:
    print("Bedingung wahr", counter)
    if counter < 0:
        print("Zahl zu klein", counter)
        break 
    counter +=1
else:
    print("Bedingung nicht mehr wahr.", counter)
"""

    
essbares = ["Nüsse", "Tomaten", "Spinat", "Apfel"]    
for gericht in essbares:
    if gericht == "Spinat":
        print("Ich mag keinen Spinat.")
        break
    print("Lecker,", gericht)
else:
    print("Glück gehabt, kein Spinat.")
print("Das wird in jedem Fall angezeigt.")

# "else" bedeutet hier quasi: Wenn der break nicht aktiviert wurde.
# Es steht außerhalb des loops, weil es ja erst nach dem
# Loop ausgeführt werden soll. 
