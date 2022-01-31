"""
Skript zum Arbeiten mit Wort-Häufigkeiten in einem DataFrame.

Hier: Gruppieren von Texten nach den Metadaten.
Beispielsweise zur Berechnung von Durchschnittswerten pro Textgruppe.

Verwendet die DataFrame.groupby Methode.
https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.groupby.html



"""

import pandas as pd
import numpy as np

pd.set_option("display.precision", 3)


def load_tdm(tdmfile):
    """
    Lädt die TDM mit den Korpushäufigkeiten.
    Returns: DataFrame.
    """
    ## Lädt TDM
    with open(tdmfile, "r", encoding="utf8") as infile:
        tdm_raw = pd.read_csv(infile, sep="\t", index_col=0)
        tdm_raw.fillna(0, inplace=True)
        tdm_raw.drop("totals", axis=1, inplace=True) # 1 = Spaltentitel
    #print(tdm_raw.head())
    #print(tdm_raw.shape)
    return tdm_raw


def replace_labels(tdm_raw):
    """
    Lädt die Metadatendatei, erstellt Dictionary mit Idnos und Titeln.
    Ersetzt die Spaltentitel durch die Information aus den Metadaten.
    Returns: DataFrame. 
    """
    with open("metadata.csv", "r", encoding="utf8") as infile:
        metadata = pd.read_csv(infile, sep=",")
    idnos = list(metadata.loc[:,"idno"])
    labels = list(metadata.loc[:,"subgenre"]) # title, subgenre, decade
    renamingdata = dict(zip(idnos, labels))
    tdm_lbs = tdm_raw.rename(columns=renamingdata)
    #print(tdm_lbs.head())
    return tdm_lbs


def make_relfreqs(tdm_lbs):
    ## Relative Häufigkeiten
    tdm_lbs_rf = tdm_lbs.div(np.sum(tdm_lbs, axis=0)) # 0 = sum spaltenweise (pro Text)
    return tdm_lbs_rf



def apply_grouping(tdm_lbs):
    """
    Berechnet den Mittelwert der relativen Worthäufigkeiten pro Untergattung.
    Verwendet dafür .groupby und .mean
    Returns: DataFrame. 
    """
    tdm_grp = tdm_lbs.groupby([tdm_lbs.columns], axis=1).mean()
    print(tdm_grp.head())
    return tdm_grp
    
  

def main(tdmfile):
    tdm_raw = load_tdm(tdmfile)
    tdm_lbs = replace_labels(tdm_raw)
    tdm_lbs_rf = make_relfreqs(tdm_lbs)
    tdm_grp = apply_grouping(tdm_lbs_rf)
    

main(tdmfile="doyle-tdm.tsv")