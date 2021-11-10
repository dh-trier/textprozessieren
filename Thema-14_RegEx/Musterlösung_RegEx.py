"""
Aufgabe zu RegEx: Umwandlung von Markdown in HTML. 

Grundlage der Aufgabe ist die ZIP-Datei im Ordner "Aufgabe RegEx" in StudIP.

Zielsetzung ist es, den Markdown-Datei enthaltenen Text zu bearbeiten:
(a) die historische Schreibweise zu modernisieren
(b) den Text in HTML auszuzeichen.

Abzugeben ist das Python-Skript und die resultierende HTML-Datei.

Berücksichtigt werden sollen die folgenden Merkmale des Textes:

(a) Modernisierung
- Es sollten mindestens 3 wiederholt auftauchende, historische Graphien modernisiert werden. 

(b) HTML
- HTML header sollte den Titel des Textes enthalten. 
- Der Titel des Textes sollte außerdem im HTML body erscheinen. 
- Überschriften erster Ordnung sollten vorhanden sein.
- Die Absätze sollten als solche markiert sein (Element p)
- Die Seitenzahlen sollten kodiert sein, und zwar nach dem Modell <span class="pagebreak">123</span>.
- Kursivierungen sollten kodiert sein (Element em). 


"""

import re


def read_textfile():
    with open("Münchhausen.md", "r", encoding="utf8") as infile:
        text = infile.read() 
        #print(text[0:200])
        return text


def modernize(text):
    modern = re.sub("th", "t", text)
    modern = re.sub("Th", "T", modern) # Wie könnte man das hier in einem Schritt erledigen?
    modern = re.sub("ey", "ei", modern)
    modern = re.sub("ey", "ei", modern)
    modern = re.sub("iren", "ieren", modern)
    # Es bleiben: Dieß, Nahmen, originellesten, Tractatus, Classen,
    return modern


def htmlify(text):
    # HTML Rahmen
    html = "<!doctype html>\n<html>\n" + text + "\n</body>\n</html>"
    # Metadaten mit dem Titel; zugleich Titel als oberste Überschrift im body. 
    html = re.sub("<html>\n##(.*?)\n", "<html\n<meta charset=\"utf-8\">\n<title>\\1</title>\n</meta>\n<body>\n<h1>\\1</h1>", html)
    # Seitenzahlen
    html = re.sub(r"\\\[\*\*(\d+)\*\*\\\]", "<span class=\"pagebreak\">[S. \\1]</span>", html)
    # Kapitelüberschriften
    html = re.sub("\*\*\*(.*?)\*\*\*", "<h2>\\1</h2>", html)
    # Absätze
    html = re.sub(r"\n([^<].*?)\n", "\n<p>\\1</p>", html)
    # Kursivierung
    html = re.sub(r"\*(.*?)\*", "<em>\\1</em>", html)    
    # Nachbesserungen
    html = re.sub(r"<p>\n", "<p>", html)
    html = re.sub("</h1><span", "</h1>\n<span", html)
    html = re.sub("</p><h2>", "</p>\n<h2>", html)
    html = re.sub("<p><span class=\"pagebreak\">(\d+)</span> </p>", "<span class=\"pagebreak\">\\1</span>", html)
    html = re.sub(r"\\!", "!", html)
    return html


def save_htmlfile(html):
    with open("Münchhausen.html", "w", encoding="utf8") as outfile:
        outfile.write(html)


def main():
    text = read_textfile()
    modern = modernize(text)
    html = htmlify(modern)
    save_htmlfile(html)

main()

