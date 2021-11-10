"""
Skript zur Visualisierung von Daten aus einer TDM.

Dieses Beispiel: Lineplot für mehrere Wörter in allen Texten. 

Verwendet pygal: http://www.pygal.org/en/stable/documentation/index.html

"""

import pandas as pd
import re
import pygal
import numpy as np



def load_tdm(tdmfile):
    """
    Lädt die TDM mit den Korpushäufigkeiten.
    Berechnet relative Häufigkeiten (Vergleichbarkeit)
    Returns: DataFrame.
    """
    # Lädt TDM
    with open(tdmfile, "r", encoding="utf8") as infile:
        tdmdata = pd.read_csv(infile, sep="\t", index_col=0)
    # Berechnet Häufigkeiten pro 10,000 Wörter
    tdmdata = tdmdata.div(np.sum(tdmdata, axis=0))*10000
    #print(tdmdata.head())
    return tdmdata


def get_textlabels():
    """
    Lädt die Metadatendatei, erstellt Dictionary mit Idnos und Titeln.
    Returns: Dict
    TODO: Dateiname als Parameter.
    """
    with open("metadata.csv", "r", encoding="utf8") as infile:
        metadata = pd.read_csv(infile, sep=",")
    #print(metadata)
    idnos = list(metadata.loc[:,"idno"])
    titles = list(metadata.loc[:,"title"])
    textlabels = dict(zip(idnos, titles))
    #print(textlabels)
    return textlabels


def prepare_data(tdmdata):
    """
    Wählt die Daten aus und transformiert sie für pygal.
    Returns: list of lists.
    TODO: Auswahl als Parameter.
    """
    # (Optional) Ersetzt Identifier durch Kurztitel
    textlabels = get_textlabels()
    prepdata = tdmdata.rename(columns=textlabels)
    # Wählt Datenbereich aus (Types und Texte)
    # Mit Zahl via iloc oder label via loc.
    #prepdata = prepdata.iloc[[112, 120],0:12] # Types + Texte per Zahl
    prepdata = prepdata.iloc[:,0:12] # Texte
    prepdata = prepdata.loc[["hound", "house", "hand"],:] # Texte
    #print(prepdata)
    return prepdata


def make_plot(prepdata):
    """
    Legt einen plot an.
    Parameter, Labels, Daten. 
    """
    # Plot initialisieren, mit Parametern
    plot = pygal.Line(legend_at_bottom=False)
    # Labels
    plot.title = "Häufigkeiten pro 10.000 Wörter im Doyle-Korpus"
    plot.x_title = "Texte im Doyle-Korpus"
    plot.y_title = "Häufigkeit pro 10.000 Wörter"
    plot.x_labels = prepdata.columns
    plot.x_label_rotation=-40
    # Daten einfüttern: Label (Wort) und Liste der Werte
    for i in range(0,prepdata.shape[0]):  # Anzahl der Wörter/Zeilen
        plot.add(prepdata.iloc[i,:].name, list(prepdata.iloc[i,:]))
        plot.value_formatter = lambda x: "%.2f" % x
    # Plot abspeichern
    plot.render_to_file("doyle-lineplot_multiple.svg")
    

def main(tdmfile):
    tdmdata = load_tdm(tdmfile)
    pdata = prepare_data(tdmdata)
    make_plot(pdata)

main(tdmfile="doyle-tdm.tsv")