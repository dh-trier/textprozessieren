"""
Skript zum Arbeiten mit Wort-Häufigkeiten in einem DataFrame.

Hier: Berechnung des TF-IDF (term frequency / document frequency)
Siehe: https://de.wikipedia.org/wiki/Tf-idf-Ma%C3%9F

- term frequency = Häufigkeit eines Wortes in einem Text,
  in der Regel Normalisiert durch Division mit der größten Häufigkeit eines Wortes im Text.
- document frequency = Anzahl der Dokumente, in dem das Wort mindestens einmal vorkommt
- TF-IDF: gewichtete Häufigkeit: je höher der Wert,
  desto spezifischer ist das Wort für das Dokument. 

"""

import pandas as pd
import numpy as np

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


def calculate_tfidf(tdm_raw):
    """
    Berechnet TF-IDF Scores.
    """
    ## Relative Häufigkeiten
    tdm_rf = tdm_raw.div(np.sum(tdm_raw, axis=0)) # 0 = sum spaltenweise (pro Text)
    #print(tdm_rf.head())
    #print(tdm_rf.tail())
    ## Dokument-Häufigkeiten: Binarisierung + Summierung
    tdm_dfs = (tdm_raw >= 1.0).astype(int)
    #print(dfs.head())
    #print(dfs.tail())
    tdm_tfidf = tdm_rf.div(np.sum(tdm_dfs, axis=0))
    #print(tdm_tfidf.head())
    #print(tdm_tfidf.tail())

    

def main(tdmfile):
    tdm_raw = load_tdm(tdmfile)
    tdm_tfidf = calculate_tfidf(tdm_raw)
    

main(tdmfile="doyle-tdm.tsv")
