"""
Script for loading an existing word2vec model and performing a word-level
clustering using the BIRCH clustering algorithm. Results in multiple list
of words that are semantically related. 

Output: A TSV file with cluster number, cluster size and words in each cluster. 

The sample models used here are available from Zenodo: 
- French Novel: https://doi.org/10.5281/zenodo.6004717
- French Wikipedia: https://doi.org/10.5281/zenodo.162792 (2017)
"""


# === Imports === 

from os.path import join
import pandas as pd 

import gensim
from gensim.models import Word2Vec

from sklearn.cluster import Birch
import scipy.sparse



# === Files and parameters === 

modelfolder = join("..", "..", "..", "2017", "w2v", "models")
modelfiles = {"roman20-small" : join(modelfolder, "roman20_mdt=skgr-opt=negsam-itr=10-dim=200-win=6-min=200.gensim"),
              "roman20-medium": join(modelfolder, "roman20_mdt=skgr-opt=negsam-itr=10-dim=300-win=6-min=100.gensim"),
              "romans20-large" : join(modelfolder, "roman20_mdt=skgr-opt=negsam-itr=10-dim=300-win=6-min=50.gensim"),
              "frwiki17-medium": join(modelfolder, "frwiki17_mdt=skgr-opt=negsam-itr=20-dim=200-win=8-min=200.gensim")}

modelname = "frwiki17-medium"
num_clusters = 600
resultsfile = "wordclusters_" + modelname + "-model_" + str(num_clusters) + "-clusters.tsv"



# === Functions === 

def load_model(modelfile): 
    """ Loads an existing word2vec model in Keyed vector format. """
    model = gensim.models.Word2Vec.load(modelfile)
    vocab = model.wv.index_to_key
    return model, vocab


def transform_model(model, vocab): 
    """ Merges model and vocabulary into a DataFrame for scikit-learn. """
    model_df = pd.DataFrame.from_dict(dict(zip(vocab, model.wv)), orient='index')
    print("Model shape (vocabulary x dimensions):", model_df.shape)
    return model_df


def perform_clustering(model_df, num_clusters): 
    """ Performs the clustering of words based on the similarity of their vectors. """
    clusterer = Birch(n_clusters = num_clusters)
    clusterer.fit(model_df)
    clusters = clusterer.predict(model_df)
    return clusters


def transform_results(clusters, vocab): 
    """ Maps the cluster numerical members onto the actual vocabulary.
    Groups all words of a cluster into one list / line in a dataframe. """
    mapped = pd.DataFrame.from_dict(dict(zip(vocab, clusters)), 
        orient="index", columns=["cluster"]).reset_index().rename(columns = {'index':'word'})
    grouped = mapped.groupby(by="cluster")["word"].apply(list).reset_index(name = "words").set_index("cluster")
    grouped["size"] = grouped["words"].apply(len)
    grouped["words"] = grouped["words"].apply(sorted).apply(", ".join)
    grouped.sort_values(by="size", ascending=True, inplace=True)
    word_clusters = grouped[["size", "words"]]
    #print(word_clusters.head())
    return word_clusters


def save_results(word_clusters, resultsfile): 
    """ Saves the results to disk as a TSV file. """
    with open(resultsfile, "w", encoding="utf8") as outfile: 
        word_clusters.to_csv(outfile, sep="\t")
    print("Saved results.")



## === Main === 

def main(modelfiles, modelname, num_clusters, resultsfile): 
    modelfile = modelfiles[modelname]
    model, vocab = load_model(modelfile)
    model_df = transform_model(model, vocab)
    clusters = perform_clustering(model_df, num_clusters)
    word_clusters = transform_results(clusters, vocab)
    save_results(word_clusters, resultsfile)

main(modelfiles, modelname, num_clusters, resultsfile)    
