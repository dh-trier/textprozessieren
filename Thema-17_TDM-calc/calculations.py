"""
Skript zum Arbeiten mit Wort-Häufigkeiten in einem DataFrame. 

Verwendet DataFrames und Series aus pandas.
Insbesondere Methoden von DataFrame: head, shape, drop, mean, sub, div. 
Siehe: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.html




"""

import pandas as pd
import numpy as np



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


def make_zscores(tdm_raw):
    """
    Berechnet z-scores für alle Wort-Häufigkeiten:
    Grundlage: 
    - Relative Häufigkeiten (<= Textlängen)
    - mittlere relative Häufigkeit pro Wort im Korpus
    - Standardabweichung pro Wort im Korpus
    Formel:
    z = (x - mw) / std
    """
    ## Relative Häufigkeiten
    tdm_rf = tdm_raw.div(np.sum(tdm_raw, axis=0)) # 0 = sum spaltenweise (pro Text)
    #print(tdm_rf.head())
    ## Mittelwert der relativen Häufigkeit pro Wort (Alternativen)
    #rfmean = np.mean(tdm_rf, axis=1) # 1 = mean zeilenweise (pro Wort)
    rfmean = tdm_rf.mean(axis=1) # 1 = mean zeilenweise (pro Wort)
    #print(rfmean)
    ## Standardabweichung der relativen Häufigkeiten pro Wort (Alternativen)
    ## Vorsicht: Mit Defaults sind die Ergebnisse nicht identisch!!
    ## Siehe: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.std.html
    ## Und: https://en.wikipedia.org/wiki/Standard_deviation#Corrected_sample_standard_deviation
    #rfstd = np.std(tdm_rf, axis=1) # 1 = std zeilenweise (pro Wort)
    rfstd = tdm_rf.std(axis=1, ddof=0) # 1 = std zeilenweise (pro Wort)
    #print(rfstd)
    ## Normalisierung durch Subtraktion der Mittelwerte
    tdm_mn = tdm_rf.subtract(rfmean, axis=0)
    ## Division durch die Standardabweichungen
    tdm_zsc = tdm_mn.div(rfstd, axis=0)
    ## Alternativ direkt in einer Zeile
    tdm_zsc = tdm_rf.subtract(rfmean, axis=0).div(rfstd, axis=0)
    print(tdm_zsc.head())
    return tdm_zsc

    

def main(tdmfile):
    tdm_raw = load_tdm(tdmfile)
    tdm_zsc = make_zscores(tdm_raw)
    

main(tdmfile="doyle-tdm.tsv")