
"""
Python’s loop statements have a feature that some people love (Hi!),
some people hate, many have never encountered and many just find confusing:
an else clause."
http://python-notes.curiousefficiency.org/en/latest/python_concepts/break_else.html
"""


obst = ["Apfel", "Mango", "Kiwi", "Orange"]

# (1) Einfacher for-loop

def loop1(): 
    for item in obst:
        print("Aha,", item)
        print("Lecker,", item)
    print("All done.")
#loop1()


# (2) Jetzt mit Abbruch-Kriterium: bricht die Schleife komplett ab

def loop2(): 
    for item in obst:
        print("Aha,", item)
        if item == "Kiwi":
            print("Bäh,", item)
            break
        else:
            print("Lecker,", item)
        # ODER# print("Lecker,", item)
    print("Fertig.")
#loop2()


# (3) Mit Abbruch-Kriterium, und else außerhalb

def loop3():
    for item in obst:
        print("Aha,", item)
        if item == "Kiwi":
            print("Bäh,", item)
            break
        else:
            print("Lecker,", item)
    else:
        print("Glück gehabt, kein Kiwi.")  # Wird nur ausgeführt, wenn kein "break" vorkam (!!)
    print("Fertig.")   # Wird immer ausgeführt
#loop3()




# (4) continue statt break: Abbruch nur dee aktuellen Iteration, nächster Iteration wird ausgeführt. 
# Auch "Orange" läuft noch durch.
# Hier funktioniert das mit dem äußeren "else" statement nicht. 

def loop4():
    for item in obst:
        print("Aha,", item)
        if item == "Kiwi":
            print("Bäh,", item)
            continue
        print("Lecker,", item)
    else:
        print("Ist ein continue passiert?") # Wird immer ausgeführt.
    print("Fertig.")   # Wird immer ausgeführt
    
loop4()



# (5) Hier könnte man statt continue/else aber auch einfach elif verwenden

def loop5():
    for item in obst:
        print("Aha,", item)
        if item == "Kiwi":
            print("Bäh,", item)
        else:
            print("Lecker,", item)
    print("Fertig.")   # Wird immer ausgeführt
#loop5()



