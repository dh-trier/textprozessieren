# Funktionen

# def = Definition
# abcd = Name der Funktion
# () = Parameter
# body: was gemacht werden soll
# return: der Rückgabewert

# (A) Beispiel für eine Funktion


def addition(wert1, wert2):
    if type(wert1) == str and type(wert2) == str:
        result = "Ergebnis: " + wert1 + " " + wert2
    elif type(wert1) == int and type(wert2) == int:
        result = "Ergebnis: " + str(wert1 + wert2)
    else:
        result = "Ergebnis kann nicht ermittelt werden."
        
    return result

def main():
    result = addition("maus", 3) 
    print(result)

main()
    


