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
        #tdm_raw.fillna(0, inplace=True)
        tdm_raw.drop("totals", axis=1, inplace=True) # 1 = Spaltentitel
    print(tdm_raw.head())
    #print(tdm_raw.shape)
    return tdm_raw


def make_zscores(tdm_raw):
    #textlengths = np.sum(tdm_raw, axis=0)
    #wordtotals = np.sum(tdm_raw, axis=1)
    #print(wordtotals)
    #textlengths = tdm_raw.sum(axis=0) # spaltenweise
    #print(textlengths)
    tdm_rf = tdm_raw.div(tdm_raw.sum(axis=0), axis=1)
    print(tdm_rf.head())
    ## Mittelwert
    rfmean = tdm_rf.mean(axis=1)
    #print(rfmean)
    ## Standardabweichung
    rfstd = tdm_rf.std(axis=1, ddof=0) # zeilenweise
    #print(rfstd)
    ## ZSCORES
    tdm_zsc = tdm_rf.subtract(rfmean, axis=0).div(rfstd, axis=0)
    print(tdm_zsc.head())
    
    
    


def main(tdmfile):
    tdm_raw = load_tdm(tdmfile)
    make_zscores(tdm_raw)

main("doyle-tdm.tsv")
