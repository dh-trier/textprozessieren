import wikipedia
import stanza

lang = "de"

#stanza.download(lang)
wikipedia.set_lang(lang)

text = wikipedia.page("Mosel").content
nlp = stanza.Pipeline(lang)

atext = nlp(text)

for sent in atext.sentences[0:2]: 
    for word in sent.words: 
        print(word.text, "\t\t", word.lemma, "\t", word.upos, "\t", word.xpos)


for ent in atext.ents: 
    print(ent.text, ent.type)
