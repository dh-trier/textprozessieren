"""
Script zur Einführung in pandas.

Grundidee von pandas ist, einige Datentypen bereitszustellen.
Insbesondere Series und DataFrame.
Series = Eindimensionaler Array (Liste), aber mit Index und Name.
DataFrame = Zweidimensionaler Array (Matrix), mit Index.
(Außerdem: Panel, dreidimensional, eine Art Datenwürfel. 

Dazu effiziente mathematische Operationen auf diesen Datentypen.
Hier kommt auch numpy (numerical python) zum Einsatz. 

Infos hier: 
https://pandas.pydata.org/docs/getting_started/index.html#getting-started


"""


# Importe

import pandas as pd 
import numpy as np


# Damit der pandas-Import funktioniert müssen wir pandas ggfs. erst installieren.
# Das machen wir über Tools > Manage packages


# Daten

korpora = ["cze", "deu", "eng"]
numnovels = [100, 94, 100]
numwords = [5621667, 12738842, 12227703]
e5c = [80, 97, 100]

datafile = "rohdaten.tsv"


# (1) DataFrame aus mehreren Listen bzw. aus dict erstellen

# Erst ohne "index"
rohdaten = {"korpora" : korpora, "numnovels" : numnovels, "numwords" : numwords, "e5c" : e5c}
kdaten = pd.DataFrame(rohdaten)
#print(daten)


# Dann mit "index"

rohdaten = {"korpora" : korpora, "numnovels" : numnovels, "numwords" : numwords, "e5c" : e5c}
kdaten = pd.DataFrame(rohdaten, index=korpora) # ODER:
kdaten = pd.DataFrame(rohdaten, index=rohdaten["korpora"])
#print(daten)


# Dann korpora separat in den daten

rohdaten = [korpora, {"numnovels" : numnovels, "numwords" : numwords, "e5c" : e5c}]
#print(rodaten[0])
#print(rohdaten[1])
kdaten = pd.DataFrame(rohdaten[1], index=rohdaten[0])
#print(kdaten)




# Dataframe aus TSV-Datei laden


with open(datafile, "r", encoding="utf8") as rohdaten:
    kdaten = pd.read_csv(rohdaten, sep="\t", index_col="korpora") # Das nach und nach aufbauen
    #print(kdaten)
    

# (2) Slicing von DataFrames

# Slicing wie bei Listen, nur eben zweidimensional.
# Es gibt loc (über labels) und iloc (über numerische Indizes)
# Man beachte die folgende Syntax, wobei immer erst die Zeilen, dann die Spalten angegeben werden.
# Das Ergebnis ist ein df, oder eine Series, oder der Datentype der Zelle, je nachdem. 

# Wir beginnen mit loc

# alles
slice = kdaten.loc[:,:]

# Eine bestimmte Zeile komplett
slice = kdaten.loc["deu",:]

# Eine bestimmte Spalte komplett
slice = kdaten.loc[:,"numwords"] 
slice = kdaten["numwords"] # ODER: Abgekürzte Schreibweise (geht nur hierfür)

# Kombination von Spalte und Zeile
slice = kdaten.loc["deu", "numwords"]

# Mit Bereich
slice = kdaten.loc["deu", ["numnovels", "e5c"]]

#print(slice)
#print(type(slice))



# Das gleiche mit iloc


# alles
slice = kdaten.iloc[:,:]

# Eine bestimmte Zeile komplett
slice = kdaten.iloc[0,:]

# Eine bestimmte Spalte komplett
slice = kdaten.iloc[:,0]

# Kombination von Spalte und Zeile
slice = kdaten.iloc[1,1]

# Mit Bereich
slice = kdaten.iloc[0, 0:2]

#print(slice)
#print(type(slice))



# (3) Kleine Berechnungen auf dem Dataframe

# Spaltenweise Summen
result = sum(kdaten.loc[:,"numnovels"])
result = kdaten.loc[:,"numwords"].sum()

# Spaltenweise Mittelwert
result = kdaten.loc[:,"numwords"].mean()
result = np.mean(kdaten.loc[:,"numnovels"])
result = kdaten["numnovels"].mean()

# Spaltenweise Standard-Abweichung
result = np.std(kdaten.loc[:,"numwords"])
result = kdaten.loc[:,"numnovels"].std()

# Division einer Spalte durch die andere, zeilenweise
#result = daten.loc[:,"numwords"].div(daten.loc[:,"numnovels"])
#result = list(daten.loc[:,"numwords"].div(daten.loc[:,"numnovels"]))
result = kdaten["numwords"].div(kdaten["numnovels"])

#print(result)


# Solche Ergebnisse pro Zeile in einer Spalte können wir auch dem df hinzufügen
kdaten["numwords_pernovel"] = kdaten["numwords"].div(kdaten["numnovels"])
#print(kdaten)

# Umgekehrt können wir auch Zeilen oder Spalten entfernen
# Hierfür brauchen wir das Achsen-Konstrukt: 0 = Zeilen, 1 = Spalten
kdaten.drop("e5c", axis=1, inplace=True)
#print(kdaten)

kdaten.drop("cze", axis=0, inplace=True)
#print(kdaten)


# (4) Jetzt versuchen wir das alles nochmal mit einem größeren DataFrame

with open("titanic.csv", "r", encoding="utf8") as rohdaten:
    tdaten = pd.read_csv(rohdaten, sep=",") # Das nach und nach aufbauen
    #print(tdaten)
    

# Das ist ziemlich unübersichtlich, wie bekommen wir einen Eindruck vom Inhalt?

#print(tdaten.shape)  # Zeilen, Spalten
#print(tdaten.head()) # Anfang
#print(tdaten.tail()) # Ende
#print(tdaten.dtypes) # Welche Datentypen sind in den Spalten enthalten?
#print(tdaten.info()) # Übersicht
#print(tdaten.columns) # Spaltentitel
#print(tdaten.index.values) # Index der Zeilen (Fehler ohne ".values")#

#print(tdaten["Age"].mean()) # Mittleres Alter
#print(tdaten["Fare"].mean()) # Mittlerer Ticketpreis ?

#print(tdaten["Survived"].sum()) # Wie viele haben überlebt?
#print(len(tdaten)) # Wie viele Reisende sind im Datensatz enthalten?
#print("Anteil der Überlebenden", str(tdaten["Survived"].sum() / len(tdaten))) # Anteil (38%)




# (6) Abspeichern als CSV / TSV-Datei

# Wir laden die Daten nochmal neu

rohdaten = [korpora, {"numnovels" : numnovels, "numwords" : numwords, "e5c" : e5c}]
kdaten = pd.DataFrame(rohdaten[1], index=rohdaten[0])
#print(daten)


with open("korpora-daten.csv", "w", encoding="utf8") as outfile:
    kdaten.to_csv(outfile, sep="\t")



# (7) Bonusfeature: Schnelle Visualisierungen direkt in pandas

# Dafür müssen wir matplotlib installieren! (Kein Problem)
# Und wir müssen pyplot importieren

from matplotlib import pyplot as plt

# Korpusdaten

#kdaten["numnovels"].plot() # Default: lineplot
#kdaten["numnovels"].plot.bar() # barchart
#kdaten["numwords"].plot.bar() # barchart
#plt.show()


# Titanic-Daten
tdaten.plot()  # Sinnlos, alles zusammen; wir können aber ja indizieren
#plt.show()

tdaten["Age"][0:50].plot.bar() # Und einen barchart wählen
#plt.show()

tdaten["Age"][0:50].plot.bar() 
#plt.show()

tdaten.sort_values(by="Age", ascending=False)["Age"].plot.bar()
#plt.show()

tdaten.plot.scatter(x="Age", y="Survived")
#plt.show()

tdaten["Fare"].plot.box()
#plt.show()





