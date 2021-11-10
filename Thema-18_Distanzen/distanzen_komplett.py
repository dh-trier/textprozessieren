"""
Etwas Input zu Maßen für die Unterschiedlichkeit von Zeichenketten / Strings. 
- Hamming-Distanz
- Levenshtein-Distanz

Siehe:
- https://de.wikipedia.org/wiki/Hamming-Abstand
- https://de.wikipedia.org/wiki/Levenshtein-Distanz

Es gibt immer wieder Situationen, in denen die Ähnlichkeit von Zeichenketten relevant ist.
- Kollationierung (z.B. das "Martian"-Projekt)
- Fuzzy Matching (z.B. bei Suchanfragen)

"""

# Levensthein-Distanz
# Die Anzahl der Edit Operationen (delete, insert, modify) die notwendig sind,
# um einen String in einen anderen String zu überführen.
# Operiert auf Strings, die auch unterschiedlich lang sein können. 
# https://en.wikipedia.org/wiki/Levenshtein_distance

# Hamming-Abstand
# Die Anzahl der unterschiedlichen Zeichen bei alignierter Zeichenliste. 
# Setzt gleiche Länge der Strings voraus; wir füllen ggfs. mit "#" auf.
# Erfordert Konversion zu einer Liste. 
# Wir vergleichen das Ergebnis aus einer Library mit einer eigenen Berechnung

# Aus scipy
# https://docs.scipy.org/doc/scipy/reference/spatial.distance.html
# Achtung: hier wird noch durch n =len(str) geteilt, so dass es um einen Anteil geht (!= Wikipedia)



def retrieve_ld(str1, str2):
    import Levenshtein as lvn
    ldl = lvn.distance(str1, str2)
    return ldl



def retrieve_hd(item1, item2): 
    """
    Calculation of hd using scipy.
    Input: 2 x list
    Output: float
    """
    from scipy.spatial import distance
    hd = distance.hamming(item1, item2)
    # Aufhebung der Normalisierung (dann wie Wikipedia)
    hd = hd * len(item1)
    return hd


def calculate_hd(list1, list2):
    """
    Manual calculation of hd.
    Input: 2 x list
    Output: int or float
    """
    hd = 0
    for i in range(0, len(list1)):
        if list1[i] != list2[i]:
            hd +=1
    # Normalisierung (dann wie scipy)
    #hd = hd / len(list1)
    return hd


def match_lengths(str1, str2):
    """
    Creates strings of equal length from input strings. 
    Input: 2 x str
    Output: 2 x str
    """
    ext = "#"
    if len(str1) > len(str2):
        while len(str1) > len(str2):
            str2 = str2 + ext
    elif len(str1) < len(str2):
        while len(str1) < len(str2):
            str1 = str1 + ext
    return str1, str2


def turn_into_list(str1, str2):
    """
    Input: 2 x str
    Output: 2 x list
    """
    list1 = [i for i in str1]
    list2 = [k for k in str2]
    return list1, list2


def main(str1, str2):
    """
    Calculate the Levenshtein Distance (ld) in two ways:
    (a) using the levenshtein module. 
    (b) using our own calculation. 
    Calculate the Hamming Distance (hd) in two ways:
    (a) using the scipy function.
    (b) using our own calculation. 
    """
    print("Comparison of:\n" + str1 + " \n" + str2 + "\n")
   
    # Levensthein Distance
    ldl = retrieve_ld(str1, str2)
    ldc = calculate_ld(str1, str2)
    print("levenshtein ld: " + str(ldl))

    # Hamming Distance
    str1, str2 = match_lengths(str1, str2)
    list1, list2 = turn_into_list(str1, str2)
    hds = retrieve_hd(list1, list2)
    hdc = calculate_hd(list1, list2)
    # Display results
    print("\nscipy hd: " + str(hds))
    print("calculated hd: " + str(hdc))
    if float(hds) == float(hdc):
        print("Alles ok, die Ergebnisse sehen gut aus.")
    else:
        print("Achtung, mit der Berechnung stimmt etwas nicht.")
  

if __name__ == "__main__":
    main("lawn", "flaw")


# Tests
# - Julia|Jolie => ld 2, hd 2
# - Julie|Jody => ld 4, hd 4
# - flaw|lawn => ld 2, hd 4 (wegen der Veschiebung!)
































