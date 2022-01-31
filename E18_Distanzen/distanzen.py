
# Hamming-Distanz
# Levenshtein-Distanz

def retrieve_hd(list1, list2): 
    """
    Calculation of hd using scipy.
    https://docs.scipy.org/doc/scipy/reference/spatial.distance.html
    Input: 2 x list
    Output: float
    """
    from scipy.spatial import distance
    hd = distance.hamming(list1, list2)
    # Aufhebung der Normalisierung (dann wie Wikipedia)
    hd = hd * len(list1)
    return hd


def calculate_hd(list1, list2):
    hdc = 0
    for i in range(0,len(list1)):
        if list1[i] != list2[i]:
            hdc +=1
    return hdc
        

def retrieve_ld(str1, str2):
    import Levenshtein as lvn
    ldl = lvn.distance(str1, str2)
    return ldl




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
    list1 = [i for i in str1] # list comprehension
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
   
    # Levenshtein
    ldl = retrieve_ld(str1, str2)
    print(ldl)
    # Hamming Distance
    str1, str2 = match_lengths(str1, str2)
    list1, list2 = turn_into_list(str1, str2)
    hds = retrieve_hd(list1, list2)
    hdc = calculate_hd(list1, list2)
    print(hds, hdc)
    

if __name__ == "__main__":
    main("lawn", "flaw")
