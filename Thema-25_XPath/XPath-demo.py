"""

Skript für die Demonstration von XPath. 

Dokumentation: 
- lxml: https://lxml.de/xpathxslt.html

Alternative: 
- etree: https://docs.python.org/3/library/xml.etree.elementtree.html

"""


# === Importe ===

from lxml import etree


# === Dateien ===

xmlfile = "document.xml"


# === Funktionen ===

def apply_xpath_lxml(xmlfile): 
    
    ns = {"tei":"http://www.tei-c.org/ns/1.0"}
    tree = etree.parse(xmlfile)
    
    # Absoluter Pfad: Element "title" im "titleStmt"
    #results = tree.xpath("/tei:TEI/tei:teiHeader/tei:fileDesc/tei:titleStmt/tei:title/text()", namespaces=ns)
    
    # Relativer Pfad: Alle Elemente "title" (3)
    #results = tree.xpath("//tei:title", namespaces=ns)
    
    # Der Textinhalt aller Elemente "title (1)
    #results = tree.xpath("//tei:title/text()", namespaces=ns)
    
    # Der Textinhalt aller Elemente "title", deren parent "titleStmt" ist (1)
    #results = tree.xpath("//tei:titleStmt/tei:title/text()", namespaces=ns)
    
    # Der Name der Autorin (Textinhalt eines Elements)
    #results = tree.xpath("//tei:titleStmt/tei:author/text()", namespaces=ns)
    
    # Der VIAF-Link der Autorin (Wert eines Attributs)
    #results = tree.xpath("//tei:author/@ref", namespaces=ns)
    
    # Das Publikationsjahr der Erstausgabe (Element mit bestimmtem Attributwert)
    #results = tree.xpath("//tei:bibl[@type='digitalSource']/tei:date/text()", namespaces=ns)
    
    # Date und Namespace
    #results = tree.xpath("//tei:date", namespaces=ns) # 3x
    #results = tree.xpath("//tei:date/text()", namespaces=ns) #2x
    #results = tree.xpath("//tei:date/@when", namespaces=ns) #1x
    #results = tree.xpath("//tei:date/namespace::*", namespaces=ns)
    
    # Zählung und Funktionen
    #results = tree.xpath("//tei:keywords/tei:term[1]/text()", namespaces=ns)
    #results = tree.xpath("//tei:keywords/tei:term[2]/text()", namespaces=ns)
    #results = tree.xpath("//tei:keywords/tei:term[last()]/text()", namespaces=ns)
    #results = tree.xpath("//tei:keywords/tei:term[position() > 2]/text()", namespaces=ns)

    # Relative Pfade: "//tei:date" ist relativ, aber von "tei:file" bzw. "tei:sourceDesc" aus gesehen
    #results = tree.xpath("//tei:file//tei:date", namespaces=ns)
    #results = tree.xpath("//tei:sourceDesc//tei:date", namespaces=ns)
    
    # Geschwister-Knoten: alle Elemente, die auf "resp" folgen
    #results = tree.xpath("//tei:resp/following-sibling::*", namespaces=ns)
    #results = tree.xpath("//tei:resp/following-sibling::*/text()", namespaces=ns)
    
    # Eltern-Knoten des aktuellen Knotens: "resp" = aktueller Knoten, davon dann der Eltern-Knoten
    #results = tree.xpath("//tei:resp/..", namespaces=ns) # klar, resp in respStmt
    #results = tree.xpath("//tei:resp/../..", namespaces=ns) # zwei Level hoch: besserer Kontext
    results = tree.xpath("name(//tei:resp/..)", namespaces=ns) # zwei Level hoch: besserer Kontext
        
    

    print("\n====")
    if type(results) == list: 
        print(len(results), "result(s)")
        for item in results: 
            print(item)
    else: 
        print(results)
    

apply_xpath_lxml(xmlfile)
