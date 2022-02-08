"""
Skript zur Berechnung von Kookurrenzen.

Die Ergebnisse können mit den Ergebnissen von TXM verglichen werden.

Für "la" und "maison" in "FRA01402_Fleuriot.txt":
- TXM: "la"=697, "maison"=18, cooc=10 bei window= -5,5 words, score=3
- TXM: "fille"=5, "petite"=70, cooc=3 bei window= -5,5 words, score=3.
- TXM: "neptune"=140, "père"=19, cooc=15 bei window= -5,5 words, score=14.
- TXM: "neptune"=140, "bateau"=19, cooc=5 bei window= -5,5 words, score=2.
- TXM: "maman"=96, "chère"=38, cooc=27 bei window= -5,5 words, score=28.
- TXM: "maman"=96, "bonne"=87, cooc=12 bei window= -5,5 words, score=3.

"""

# Importe

import re
import numpy as np

# Funktionen

def read_textfile(textfile):
    with open(textfile, "r", encoding="utf8") as infile:
        text = infile.read().lower()
        text = re.split("\W+", text)
        #print(text[0:10])
        return text


def get_frequency(text, word):
    freq = text.count(word)
    return freq


def get_cooccurrences(text, word1, word2, windowsize):
    # Liste der Positionen, an denen word1 vorkommt
    posword1 = []
    for position,word in enumerate(text):
        if word == word1:
            posword1.append(position)
    #print(posword1)
    #print(len(posword1)) # Test: == freq1?
    
    # Kompakte Alternative mit List comprehension
    #posword1 = [pos for pos, word in enumerate(text) if word == word1]
    #print(posword1) # Identisch zu Langfassung!
    
    # Wie oft kommt word2 im Fenster um word1 herum vor?
    offset = int(windowsize/2)
    coocs = 0
    for pos in posword1:
        textwindow = text[pos-offset:pos+offset+1] # x + word1 + x
        #print(textwindow)
        for pos,word in enumerate(textwindow):
            if word == word2:
                coocs +=1
    return coocs
        


    """
    # Brauchbarer Ansatz mit text als string
    resultsword1 = re.finditer(word1, text)
    sidesize = int((windowsize-len(word1))/2)
    coocs = 0
    for match in resultsword1:
        window = text[match.start()-sidesize:match.end()+sidesize]
        #print(window)
        if word2 in window:
            coocs +=1
    print(coocs)
    """
    
    
        
    """
    # Kein guter Ansatz
    numwindows = len(text) // windowsize
    print(len(text), windowsize, numwindows)
    coocs = 0
    for i in range(0, numwindows):
        window = text[i:i+windowsize]
        if word1 in window and word2 in window:
            coocs +=1
    print(coocs)
    """

def calculate_coocscore(text, freq1, freq2, coocs, windowsize):
    numwords = len(text)
    relfreq1 = freq1/numwords
    relfreq2 = freq2/numwords
    relcooc = coocs/numwords
    #print(relfreq1, relfreq2, relcooc)
    mutinf = np.log(relcooc/(relfreq1*relfreq2))
    #print(mutinf)
    return np.round(mutinf,2)
        

# Parameters

#word1,word2,window = "neptune","père",10  # gleiche Häufigkeit, große Kookurrenz
#word1,word2,window = "neptune","bateau",10 # gleiche Häufigkeit, seltenere Kookurrenz

#word1,word2,window = "maman","chère",10 # größere Häufigkeit, seltenere Kookurrenz
word1,word2,window = "maman","bonne",10 # geringere Häufigkeit, höhere Kookurrenz



# Main

def main(textfile, word1, word2, windowsize):
    text = read_textfile(textfile)
    freq1 = get_frequency(text, word1)
    freq2 = get_frequency(text, word2)
    coocs = get_cooccurrences(text, word1, word2, windowsize)
    score = calculate_coocscore(text, freq1, freq2, coocs, windowsize)
    print(word1, freq1, "|", word2, freq2, "| windowsize", windowsize, "| coocs", coocs, "| score", score)

main("FRA01402_Fleuriot.txt", word1, word2, window)