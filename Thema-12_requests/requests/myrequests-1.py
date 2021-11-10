# Imports 

import requests

# Parameters

baseurl = "https://archiveofourown.org/works/"
identifiers = ["17806076"]

# Functions 

def download_html(baseurl, identifier): 
    url = baseurl + identifier + "?view_full_work=true"
    print("https://archiveofourown.org/works/18018923?view_full_work=true")
    print(url)
    result = requests.get(url)
    print(result)
    print(result.text)
    #return text



def main(baseurl, identifiers): 
    for identifier in identifiers: 
        download_html(baseurl, identifier)

main(baseurl, identifiers)
