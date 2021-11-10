# Importe

import re
from os.path import join
from glob import glob as gg


# Funktionen

def read_textfile(textfile):
    """Opens a textfile and reads the content.
    Returns the file content as a string."""
    with open(textfile, "r", encoding="utf8") as infile:
        text  = infile.read()
    # print(text[0:100])
    return text


def clean_text(text):
    """Simplifies a text, removing anything except words.
    Returns a string."""
    text = text.lower()
    text = re.sub("ſ", "s", text)
    text = re.sub("-\n", "", text)
    text = re.sub("\n", " ", text)
    text = re.sub(",", "", text)
    text = re.sub(r"\.", "", text)
    text = re.sub(";", "", text)
    text = re.sub(r"\(", "", text)
    text = re.sub(r"\)", "", text)
    text = re.sub(r"\d", "", text)
    text = re.sub(" {2,6}", " ", text)    
    # print(text)
    return text


def get_numvowels(text):
    """Counts the vowels contained in a string.
    Returns an integer. """
    vowels = "aeiouöüä"
    counter = 0
    for char in text:
        if char in vowels:
            counter +=1
    return counter


def get_textstats(text):
    """Calculates some basic text statistics.
    Returns a list of integers."""
    len_chars = len(text)
    len_words = len(text.split(" "))
    num_vowels = get_numvowels(text)
    textstats = [len_chars, len_words, num_vowels]
    print(textstats)
    return textstats
   

# Main

def main(textfolder):
    for textfile in gg(textfolder): 
        text = read_textfile(textfile)
        text = clean_text(text)
        textstats = get_textstats(text)
    
main(join("texte", "*.txt"))

