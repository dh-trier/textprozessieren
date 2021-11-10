"""
pandas
Series = 1-dimensional
+++ DataFrame = 2-dimensional (Tabelle) +++ 
Panel = 3-dimensional ("Datenwürfel")

Infos hier: 
https://pandas.pydata.org/docs/getting_started/index.html#getting-started

"""

import pandas as pd
import numpy as np


# Daten

korpora = ["cze", "deu", "eng"]
numnovels = [100, 94, 100]
numwords = [5621667, 12738842, 12227703]
e5c = [80, 97, 100]


rohdaten = [korpora, {"numnovels" : numnovels, "numwords" : numwords, "e5c" : e5c}]

#kdaten = pd.DataFrame(rohdaten)
#kdaten = pd.DataFrame(rohdaten, index=korpora) # ODER:
kdaten = pd.DataFrame(rohdaten[1], index=rohdaten[0])
#print(kdaten)

"""
CSV = comma-separated values
TSV = tabulator-separated values
"""


with open("titanic.csv", "r", encoding="utf8") as infile:
    tdaten = pd.read_csv(infile, sep=",")
    print(tdaten.head())

    print(tdaten["Fare"].mean())
    

    

rohdaten = [korpora, {"numnovels" : numnovels, "numwords" : numwords, "e5c" : e5c}]
kdaten = pd.DataFrame(rohdaten[1], index=rohdaten[0])
print(kdaten)

#kdaten.drop("numwords", axis=1, inplace=True)
#print(kdaten)

with open("korpora-daten-reduziert.csv", "w", encoding="utf8") as outfile:
    kdaten.to_csv(outfile, sep=";")


from matplotlib import pyplot as plt


#kdaten["numwords"].plot.bar()
#plt.show()


tdaten.plot.scatter(x="Age", y="Fare")
plt.show()















