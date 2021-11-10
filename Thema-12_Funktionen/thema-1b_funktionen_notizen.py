# Funktionen

"""

Struktur: 

def Funktionsname(Input oder Parameter):
   Docstring
   Anweisungen
   return Output

"""

def greeting(name="Kevin"):
    """Return a greeting based on the name."""
    print(name)
    name = "Maria"
    print(name)
    result = "Hallo " + name + "!"
    print(result)
    return result

greeting() # default
#print(name)
name = "Max Muster"
greeting(name)
print(name)
#greeting("Markus")
#print(greeting(name))
#print(greeting.__doc__)
#help(greeting)


#def main():
#    greeting("Petra")
#main()


