
# === Importe ===

import seaborn as sns
import pandas as pd
from os.path import join
import os
import re


# === Funktionen ===

def read_csv(csvfile): 
    with open(csvfile, "r", encoding="utf8") as infile: 
        data = pd.read_csv(infile, sep="\t")
    return data


def prepare_data(pdata): 
    pdata = pdata[pdata["N"] == 10]
    pdata = pdata.drop(["N", "test_statistic"], axis=1)
    pdata.sort_values(by=["measure_1", "measure_2"], axis=0, inplace=True)
    measures = []
    matrix = []
    for name, group in pdata.groupby("measure_1"): 
        measures.append(name)        
        matrix.append(list(group["pvalue"]))
    newdata = pd.DataFrame(matrix, index=measures, columns=measures)
    return newdata


def seaborn_heatmap(pdata, heatmapfile):
    myplot = sns.heatmap(data=pdata,
                         cmap="YlGnBu",
                         annot = False,
                         linewidths = 2,
                         linecolor = "white",
                         cbar = True,
                         square = False
                         ).set_title("Korrelationsmatrix als Heatmap")
    fig = myplot.get_figure()
    fig.savefig(heatmapfile, dpi=300, bbox_inches='tight')


def seaborn_clustermap(pdata, clustermapfile):
    myplot2 = sns.clustermap(data=pdata, 
                             cmap="YlGnBu",
                             dendrogram_ratio=(.2, .2),
                             tree_kws=dict(linewidths=1.5)
                             )
    #fig = myplot2.get_figure()
    myplot2.savefig(clustermapfile, dpi=300, bbox_inches='tight')


   

# === Files and folders ===

csvfile = join("..", "data", "zeta_significance_fra-80s.tsv")
heatmapfile = "heatmap.png"
clustermapfile = "clustermap.png"


# === Main ===

def main(csvfile, heatmapfile, clustermapfile): 
    data = read_csv(csvfile)
    pdata = prepare_data(data)
    seaborn_heatmap(pdata, heatmapfile)    
    seaborn_clustermap(pdata, clustermapfile)    
    
main(csvfile, heatmapfile, clustermapfile)
