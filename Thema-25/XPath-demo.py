"""

Skript für die Demonstration von XPath. 

Dokumentation: 
- lxml: https://lxml.de/xpathxslt.html
- etree: https://docs.python.org/3/library/xml.etree.elementtree.html

"""


# === Importe ===

import xml.etree.ElementTree as ET
from lxml import etree


# === Dateien ===

xmlfile = "document.xml"


# === Funktionen ===

def apply_xpath_lxml(xmlfile): 
    
    ns = {"tei":"http://www.tei-c.org/ns/1.0"}
    tree = etree.parse(xmlfile)
    
    # Absoluter Pfad: Element "title" im "titleStmt"
    results = tree.xpath("/tei:TEI/tei:teiHeader/tei:fileDesc/tei:titleStmt/tei:title/text()", namespaces=ns)
    
    # Relativer Pfad: Alle Elemente "title" (3)
    #results = tree.xpath("//tei:title", namespaces=ns)
    
    # Der Textinhalt aller Elemente "title (1)
    #results = tree.xpath("//tei:title/text()", namespaces=ns)
    
    # Der Textinhalt aller Elemente "title", deren parent "titleStmt" ist (1)
    #results = tree.xpath("//tei:titleStmt/tei:title/text()", namespaces=ns)
    
    # Der Name der Autorin
    #results = tree.xpath("//tei:titleStmt/tei:author/text()", namespaces=ns)
    
    # Der VIAF-Link der Autorin
    #results = tree.xpath("//tei:author/@ref", namespaces=ns)
    
    # Das Publikationsjahr der Erstausgabe
    #results = tree.xpath("//tei:bibl[@type='digitalSource']/tei:date/text()", namespaces=ns)

    print("\n====")
    print(len(results), "result(s)")
    for item in results: 
        print(item)
    

apply_xpath_lxml(xmlfile)
