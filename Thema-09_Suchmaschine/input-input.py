"""
Kurze Einführung in die Interaktion mit Python via CLI.


Man kann mit Python auf der Kommandozeile interagieren.
Beispielsweise um Parameter interaktiv zu setzen.
Oder um auf Input zu reagieren.
"""

# Beispiel: Name abfragen

#print("Bitte nenne mir deinen Namen:")
#username = input()
#print("Hallo " + str(username) + ", freut mich dich kennenzulernen.")

# Beispiel: Going Dutch

"""
Going Dutch: Planen Sie ein Programm, das dabei hilft, eine Restaurant-Rechnung
auf mehrere Personen aufzuteilen. Beachten Sie dabei die folgenden Punkte:
- Die Nutzenden können angeben, wie hoch die Rechnung ist und wie viele Personen sich die Rechnung teilen.
- Das Programm sollte nur ganze Zahlen als Eingabe akzeptieren.
- Das Programm sollte 5% Trinkgeld berücksichtigen.
- Alle Personen sollten gleich viel bezahlen.
- Alle Personen sollten ganze Eurosummen bezahlen.

"""



# Beispiel-Implemnetierung

import math
 
print("Dieses Programm hilft dabei, eine Rechnung zu splitten.")
rechnung = input("Wie hoch ist die Rechnung des Restaurants in Euro? ")
while rechnung.isnumeric() == False:
    rechnung = input("Bitte eine ganze, positive Zahl angeben (aufrunden).")
else: 
    print("Danke für die Angabe.")
personen = input("\nWie viele Personen teilen sich die Rechnung? ")
while personen.isnumeric() == False:
    personen = input("Bitte eine ganze, positive Zahl angeben.")
else:
    print("Danke für die Angabe.")
mittrinkgeld = math.ceil(int(rechnung) * 1.05)
print("\nRechnung mit 5% Trinkgeld (aufgerundet)", str(mittrinkgeld), "EUR.")
properson = math.ceil((int(mittrinkgeld) // int(personen) + (int(mittrinkgeld % int(personen) > 0))))
print("Jede Person sollte "+ str(properson) + " EUR bezahlen.") 
print("Das sind dann zusammen "+ str(int(properson) * int(personen)) + " EUR.") 




 









