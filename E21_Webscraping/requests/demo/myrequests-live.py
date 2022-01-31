# Importe
import requests

# Parameter
#https://www.worldcat.org/search?q=ti%3Avariation+au%3ABiber
#https://www.worldcat.org/search?q=ti%3Avariation+au%3ABiber


baseurl = "http://www.museumsstiftung.de/briefsammlung/post-von-drueben/briefliste.html?action=searchresults&what=letter&le_fulltext="
query = "Trabant"

# Funktionen

def make_request(baseurl, query):
    url = baseurl + query
    try: 
        result = requests.get(url, timeout=4)
        print(result.url)
        print(result.text)

    except:
        print("Keine Daten unter der URL", url)

make_request(baseurl, query)