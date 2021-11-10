"""
Skript zum Arbeiten mit Wort-Häufigkeiten in einem DataFrame.

Hier: Gruppieren von Texten nach den Metadaten.
Beispielsweise zur Berechnung von Durchschnittswerten pro Textgruppe.

Verwendet die DataFrame.groupby Methode.
https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.groupby.html

Beispiel:
- Die Satorbase enthält für 1100 Topoi rund 2500 Beispiele aus Texten.
- Wir möchten genauer wissen, wie sich diese Beispiele verteilen. 
- Für welche fünf Topoi gibt es die meisten Beispiele?
- Für wieviele Topoi gibt es nur 1 Beispiel?
- Wie verteilen sich die Beispiele insgesamt auf die Topoi?


"""

import pandas as pd
import numpy as np


def load_tdm(topoifile):
    """
    Lädt die TDM mit einigen Daten. 
    Returns: DataFrame.
    """
    ## Lädt Tabelle
    with open(topoifile, "r", encoding="utf8") as infile:
        topoi_raw = pd.read_csv(infile, sep="\t")
        topoi_raw.drop(["exampleTEXT", "researcherID", "toposID"], axis=1, inplace=True) # 1 = Spaltentitel
    print(topoi_raw.head())
    print(topoi_raw.shape)
    return topoi_raw


def grouping(topoi_raw):
    topoi_gpd = topoi_raw.groupby("toposLABEL", axis=0).count()
    topoi_gpd.rename({"exampleID": "exampleCOUNT"}, axis=1, inplace=True)
    print(topoi_gpd.head())
    return topoi_gpd


def analyse_data(topoi_gpd):
    ## Für welche drei Topoi gibt es die meisten Beispiele?
    topoi_gpd.sort_values(by="exampleCOUNT", ascending=False, inplace=True)
    print("\nTopoi mit den meisten Beispielen\n", topoi_gpd.head())
    ## Für wie viele Topoi gibt es nur 1 Beispiel?
    one_example = np.sum(topoi_gpd["exampleCOUNT"] == 1)
    print("\nAnzahl der Topoi mit nur einem Beispiel:", one_example)


def visualize_data(topoi_gpd):
    ## Wie verteilen sich die Topoi auf die Beispiele?
    import pygal
    plot = pygal.Line(show_legend=False)
    plot.title = "Number of examples per Topos"
    plot.x_title = "The 1100 different Topoi"
    plot.y_title = "The number of examples"
    plot.add("exampleCOUNT", topoi_gpd["exampleCOUNT"])
    plot.render_to_file("exampleCOUNT.svg")
    


def main(topoifile):
    topoi_raw = load_tdm(topoifile)
    topoi_gpd = grouping(topoi_raw)
    analyse_data(topoi_gpd)
    visualize_data(topoi_gpd)
    

main(topoifile="topoi.tsv")