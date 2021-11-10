"""
Session zu Regulären Ausdrücken.

Dokumentation zum Modul "re" hier: https://docs.python.org/3.7/library/re.html

Sehr gute Einführung: https://docs.python.org/3.7/howto/regex.html#regex-howto

==============

Grundidee: Ein RegEx definiert ein Muster für eine Zeichenfolge, nach dem in Strings gesucht werden kann.

Themen
- Funktionen von re für die Suche
- Quantifier und "Greediness"
- Flags
- Zeichen-Klassen
- Gruppen im Suchergebnis
- Suchen/Ersetzen


"""

# Importe

import re




# Daten einlesen: Hier als String (statt als JSON-Objekt oder XML)

with open("programmieren.rdf", "r", encoding="utf8") as infile:
    data = infile.read() # Als String
    #print(type(data)) # Sollte "str" sein
    #print(data)



# ==== Mehrere Funktionen von re, mit denen man suchen kann ====

"""
"re.match": nur von Anfang des Strings an
"re.search": Erster Treffer im gesamten String als "match object". 
"re.findall": Alle nicht-überlappenden Treffer im gesamten String als Liste von strings.
"re.finditer": Wie re.findall, aber gibt einen Iterator von "match objects" zurück.

Wir fokussieren hier der Einfachheit halber auf "re.findall"; die match objects sind aber auch praktisch.
Erst einmal ein paar Beispiele zum Einstieg. 
"""

# Einfach Suche nach String
r = re.findall("Python", data)

# Mit Wildcard: . = beliebiges Zeichen
r = re.findall(".ython", data)


# Kurz noch zu finditer und search

#result = re.search("Python", data)
#print(result)
#print(result.span(), result.start(), result.end(), result.group())

#r = re.finditer("Python", data)  
#for item in r:
#    print(item.span(), item.start(), item.end(), item.group())


# Flags

"""
Flags sind wie ein zusätzlicher Parameter für die Suche.
Man hängt sie mit der Syntax re.FLAG an die Suche an
Drei nützliche Flags

re.IGNORECASE (I)
re.DOTALL (S)
re.MULTILINE (M)  Normalerweise wird immer nur innerhalb einer Zeile geprüft; so auch über Zeilen hinweg. 

"""

r = re.findall("python", data, re.IGNORECASE)
r = re.findall("python", data, re.I) # Auch kurz
r = re.findall("python", data.lower()) # Auch kurz


# ==== Quantifier =====

"""
* = beliebige Anzahl (auch 0x)
+ = beliebige Anzahl, mindestens aber 1x
? = optional, 0x oder 1x
*? = beliebige Anzahl, aber "non-greedy" # Kontextabhängige Bedeutung von "?"!!
{n} = exakte Anzahl
{n,m} = Range, von n bis m x
"""

r = re.findall("comp.* ", data.lower()) # Siehe das Leerzeichen am Ende! (Problem? Interpunktion)
r = re.findall("comput.+ ", data.lower())
r = re.findall("computer.+ ", data.lower())  # Why is computers not found? Because of the " ". We need better solution.
r = re.findall("computers", data.lower()) # computers kommt vor
r = re.findall("computer.", data.lower()) # The Wildcard also includes the space
r = re.findall("computers?", data.lower()) # Now the final "s" is optional
r = re.findall("comp.*", data.lower()) # Default ist greedy, also so langer match wie möglich = Bis Ende der Zeile.
r = re.findall("comp.*?", data.lower()) # Non-greedy bedeutet, dass das kürzest-mögliche Match genommen wird.
r = re.findall("(comp.*?)[ <]", data.lower()) # Non-greedy bedeutet, dass das kürzest-mögliche Match genommen wird.
r = re.findall("comp.{5}", data.lower()) # Non-greedy bedeutet, dass das kürzest-mögliche Match genommen wird.





# ======== Zeichen-Klassen =====

"""
Es gibt vordefinierte Zeichen-Klassen
Man kann aber auch leicht selbst Zeichen-Klassen definieren

Vordefinierte Zeichen-Klassen

\d = Zahlen (digits)
\w = Wort-zeichen  (words)
\D = Nicht-Zahlen
\W = Nicht-Wort-Zeichen (einschließlich Interpunktion und Whitespaces)
\s = Whitespace
\S = Alles außer Whitespace

Eigene Zeichen-Klassen: innerhalb von [] alle Mitglieder der Klasse auflisten: 
[äüö] (entspricht den Umlauten im Deutschen)
[a-zA-Z] entspricht dem lateinischen Alphabet in Kleinbuchstaben
Besonders mächtig in Kombination mit den Quantifiern.

Wenn man einen "\" matchen möchte, muss man ihn escapen.
Oder besser: die "raw string notation" zu verwenden: mit >> r" <<.
Dadurch werden die "\" zwar von re, aber nicht von Python, als special characters interpretiert. 

"""
# Wir suchen den String \n, der an einer Stelle als Text in der Datei ist. Rest von Markup o.ä.
r = re.findall("\n", data) # Findet alle Newlines!
r = re.findall("\\n", data) # Findet alle Newlines!
r = re.findall("\\\\n", data) # Findet das Richtige! 
r = re.findall(r"\\n", data) # Findet das Richtige, etwas einfacher. 


r = re.findall(r"\d+-\d+", data) # Folge von Zahlen, Bindestrich, Folge von Zahlen; verschiedene Treffer
#r = re.findall(r"\d+", data) # Alle Zahlen, aber nicht solche die durch andere Zeichen unterbrochen werden
#r = re.findall(r"\w+", data) # Alle zusammenhängenden Folgen von Wort-Zeichen (im Text!)




# ==== Gruppen von Zeichen =====

"""
Gruppen von Zeichen werden in Klammern gesetzt;
Die Inhalte der Gruppe sind die Treffer
Der Rest des Musters bietet den Kontext an.
"""

# Wir suchen die Sprachbezeichnungen 
r = re.findall("en|ger", data)   # Alternative Strings; es fehlt "en-US"; zu viele andere Strings.
r = re.findall("en|ger|en-US", data)   # Alternative Strings: es wird "en" gefunden, "en-US" ist dann überlappend. 
r = re.findall(">ger<|>en<|>en-US<", data)   # Treffer; aber wir müssen die Werte kennen
r = re.findall("<z:language>.*?</z:language>", data) # "language", dann beliebiger Inhalt: aber mit "language im Ergebnis"
r = re.findall("<dc:date>.*?(\d{4}).*?</dc:date>", data) # Mit Groups können wir gesuchten Inhalt und Kontext; und mehr! 




# ==== Suchen und Ersetzen =====

"""
Hierfür kommt re.sub zum Einsatz. 
"""

r = re.sub("Python", "##JAVA##", data) # Funktioniert einwandfrei;
r = re.sub("z:language", "z:SPRACHE", data)


# Problem: Suchen/Ersetzen mit flexiblen Mustern. Das löst man mit Gruppen.

# Wir suchen Seitenzahlen und möchten das Trennzeichen korrigieren

r = re.findall(r"\d+-\d+", data) # Zu viele Treffer
r = re.findall(r"<bib:pages>.*?</bib:pages>", data) # Besser mit Kontext
r = re.findall(r"<bib:pages>(.*?)</bib:pages>", data) # Jetzt noch Fokus auf Gruppen
#r = re.findall(r"<bib:pages>(\d+).*?(\d+)</bib:pages>", data) # Jetzt noch präzisere Struktur

# Wir können gefundene Gruppen wieder einsetzen, egal welche Werte enthalten sind.
# Gruppen werden mit "\n" wieder aufgerufen. 

#r = re.sub(r"<bib:pages>(\d+)-(\d+)</bib:pages>", r"<bib:pages>\1–\2</bib:pages>", data)   # Mit Kontext wird es präziser.


# =========== Ausgabe ====

print(len(r), "Ergebnisse:", r)



#text = "Das hier ist mein Text, [p.123] der hier nach dem Seitenumbruch weitergeht."

#text = re.sub(r"\[.*?(\d+)\]", "</pb n=\"\\1\">", text)
#print(text)


