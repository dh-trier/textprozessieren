"""
Eine Re-Implementierung von ELIZA auf Deutsch
unter Verwendung von Python 3. 
"""

# == Importe ==
import random
import re


# == Input-Analyse ==

def check_stopsign(usin):
    usin_stopsign = 0
    stopsigns = ["Tschüss"]
    if stopsigns in usin:
        usin_stopsign = 1
    return usin_stopsign
        

def get_adjectives(usin):
    """
    Find adjectives in the user input.
    Collect them and decide whether they are positive or negative.
    Input: List of tokens.
    Output: List of tokens + string "pos|neg". 
    """
    posadj = ["gut", "glücklich", "fröhlich", "zufrieden"]
    negadj = ["schlecht", "unglücklich", "deprimiert", "frustriert"]
    usin_adj = []
    for item in posadj: 
        if item in usin:
            usin_adj.append(item)
            usin_adj_pol = "pos"
    if len(usin_adj) == 0:
        for item in negadj:
            if item in usin: 
                usin_adj.append(item)
                usin_adj_pol = "neg"
    if len(usin_adj) == 0:
        usin_adj_pol = "neutral"
    return usin_adj, usin_adj_pol


def get_pronouns(usin):
    """
    Find pronouns in the user input.
    Collect them and decide what perspective is expressed. 
    Input: List of tokens.
    Output: List of tokens + string "1sg|2sg|3sg|1pl|2pl|3pl". 
    """
    pron_1sg = ["ich", "mich", "mir"]
    usin_pron = []
    usin_pron_pers = "unknown"
    for item in pron_1sg: 
        if item in usin:
            usin_pron.append(item)
            usin_pron_pers = "1sg"
    return usin_pron, usin_pron_pers



# == Output-Generieren ==


def generate_sysres_adj1sg(usinan):
    sysres = "Warum fühlst du dich " + str(usinan["adj"][0]) + "?"
    return sysres



# == Programmablauf ==

def present_opener():
    print("Mein Name ist Eliza.",
          "Ich berate dich gerne.",
          "\nDu kannst mit mir sprechen.",
          "Tippe 'Ende', wenn du genug hast.")


def request_input():
    # "usin" is short for "user input"
    usin = input("Wie geht es dir?\n> ")
    return usin


def analyse_input(usin):
    usin = re.split("\W+", usin.lower())
    usin_stopsign = check_stopsign(usin)
    usin_adj, usin_adj_pol = get_adjectives(usin)
    usin_pron, usin_pron_pers = get_pronouns(usin)
    usinan = {"usin":usin,
              "stopsign" : usin_stopsign,  
              "adj" : usin_adj,
              "adj_pol" : usin_adj_pol,
              "pron" : usin_pron,
              "pron_pers" : usin_pron_pers}
    #for key,value in usinan.items():
    #    print(key, value)
    return usinan


def generate_response(usinan):
    if usinan["stopsign"] == 0: 
        if usinan["adj"] and usinan["pron_pers"] == "1sg":
            sysres = generate_sysres_adj1sg(usinan)
            usin_next = input(sysres+"\n>")
        else:
            usin_next = input("Aha. Erzähle mir doch etwas mehr darüber, wie du dich fühlst.\n> ")
    else:
        print("Danke für das Gespräch.")
                
    
    



# == Main ==

def main():
    present_opener()
    usin = request_input()
    usin_analysis = analyse_input(usin)
    generate_response(usin_analysis)

main()