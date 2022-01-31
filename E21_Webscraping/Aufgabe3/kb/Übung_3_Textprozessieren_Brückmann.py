# Leider hängt sich Thonny derzeit bei fast jedem Anstoßen des Skripts komplett auf (auch, wenn ich
# die Schleife über nur zwei html-Dateien laufen lasse; wenn ich kleine Einzelblöcke teste, funktioniert es manchmal).
# Den Grund dafür konnte ich bisher nicht identifizieren; damit geht jedoch einher, dass ich das Skript nicht in der jetzigen
# Form testen konnte und der Feinschliff fehlt.

# Importe
import re
import requests
from os.path import join
import csv

# Funktionsdefinitionen
def make_request(baseurl):
    url = baseurl + "search?utf8=%E2%9C%93&work_search%5B" + query[0][0] + "%5D=" + query[0][1] + "&work_search%5B" + query[1][0] + "%5D=" + query[1][1] + "&work_search%5B" + query[2][0] + "%5D=" + query[2][1]
    print(url)
    try:
        result = requests.get(url, timeout=5)
        resulttext = result.text
    except:
        #if response.status_code == 200:
        #    print("Zeitbegrenzung überschritten. Das Programm kann nicht korrekt ausgeführt werden.")
        #elif response.status_code == 404:
        #    print("Keine Daten unter der URL. Das Programm kann nicht korrekt ausgeführt werden.")
        #else:
        print("Es ist ein Fehler aufgetreten. Das Programm kann nicht korrekt ausgeführt werden.")
    return resulttext, baseurl

def get_id(resulttext):
    pre_id_list = re.findall("/works/(\d+)", resulttext)
    #print(pre_id_list)
    return pre_id_list

def get_id_list(pre_id_list):
    id_list = []
    print(type(id_list))
    for id in pre_id_list:
        if id not in id_list:
            id_list.append(id)
    return id_list

def build_url(baseurl, id_list):
    # falls bereits ein file mit dem Namen existiert, werden die URLs am Dokumentende angefügt
    for id in id_list:
        relevant_url = baseurl + id + "?view_full_work=true"
        #print(relevant_url)
        with open("archive_urls.txt", "a", encoding="utf8") as outfile:
            outfile.write(relevant_url + "\n")
    
def get_text(url):
    html_text = requests.get(url, timeout=10)
    html_text = html_text.text
    pre_plaintext = re.findall(r"<div class=\"userstuff module\" role=\"article\">(.+?)</div>", html_text, re.DOTALL)
    # re.DOTALL sorgt dafür, dass der Punkt auch einer newline entsprechen kann
    print(pre_plaintext)
    plaintext = ""
    for element in pre_plaintext:
        plaintext = plaintext + element
        plaintext = re.sub(r"<(.+)>", "\n", plaintext)
        #print(plaintext)
        #if response.status_code == 200:
        #    print("Zeitbegrenzung überschritten. Betroffene URL: " + url)
        #elif response.status_code == 404:
        #    print("Keine Daten unter der URL: " + url)
        #else:
        #    print("Es ist ein Fehler aufgetreten. Betroffene URL: " + url)
    return html_text, plaintext

def get_metadata(html_text):
    pre_title = re.findall(r"<h2 class=\"title heading\">(.+?)</h2>", html_text, re.DOTALL)
    title = str(pre_title[0])
    author = []
    author = re.findall(r"<a rel=\"author\" href=\".+?\">(.+?)</a>", html_text)
    words = []
    words = re.findall(r"<dd class=\"words\">(\d+)</dd>", html_text)
    return title, author, words

def write_plaintext(title, plaintext):
    path = join("archive_downloads", title + ".txt")
    with open(path, "w", encoding="utf8") as outfile:
        outfile.write(plaintext)

def write_csvheader():
    with open("metadata.csv", "a", encoding="utf8") as outfile:
        header = ["Dateiname", "Pseudonym des Autors", "Titel", "Textlänge in Wörtern"]
        csv_writer = csv.writer(outfile, delimiter =",") 
        csv_writer.writerow(header)
    
def add_metadata_to_csv(title, author, words):
    with open("metadata.csv", "a", encoding="utf8") as outfile:
        csv_writer = csv.writer(outfile, delimiter =",")
        filename = title + ".txt"
        row = [filename, author, title, words]
        csv_writer.writerow(row)

# Koordination
file = "archive_urls.txt"
baseurl = "https://archiveofourown.org/works/"
query = [["word_count", "%3E5000"], ["language_id", "1"], ["fandom_names", "Lord+of+the+Flies+-+William+Golding"]]
# Bei word_count: %3C für < und %3E für >
# Bei language_id: 7 für Deutsch

resulttext, baseurl = make_request(baseurl)
pre_id_list = get_id(resulttext)
id_list = get_id_list(pre_id_list)
relevant_url = build_url(baseurl, id_list)
write_csvheader()
with open(file, "r", encoding="utf8") as infile:
    for url in infile:
        html_text, plaintext = get_text(url)
        title, author, words = get_metadata(html_text)
        write_plaintext(title, plaintext)
        add_metadata_to_csv(title, author, words)
