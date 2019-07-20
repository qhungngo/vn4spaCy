import spacy, random
from spacy.vocab import Vocab
from spacy.language import Language

'''
from spacy.lang.en import English
nlp = spacy.load("en_core_web_md")
doc = nlp(u"I am a first year student living and studying in Hanoi capital.")
for x in [(w.text, w.lemma_, w.pos_, w.tag_, w.dep_) for w in doc]:
    print(x)
for chunk in doc.noun_chunks:
    print(chunk.text, chunk.label_, chunk.root.text)
print('------------')
'''
from spacy.lang.vi import Vietnamese
vi_nlp = Vietnamese()
doc = vi_nlp(u"Tôi là sinh viên năm nhất sống và học tập ở thủ đô Hà Nội.")
for x in [(w.text, w.lemma_, w.pos_, w.tag_, w.dep_) for w in doc]:
    print(x)

print('------------')

from spacy.language import Language
vi_nlp = spacy.load("vn_models\\model-final")
doc = vi_nlp(u"Tôi là sinh viên năm nhất sống và học tập ở thủ đô Hà Nội.")
for x in [(w.text, w.lemma_, w.pos_, w.tag_, w.dep_, w.shape_, w.is_alpha, w.is_stop) for w in doc]:
    print(x)
for X in doc.noun_chunks:
    print(X.text, X.label_, X.root.text)
for X in doc.ents:
    print(X.text, X.label_)

print('------------')

vi_nlp = spacy.load("vn_models\\model-final")

from spacy.language import EntityRecognizer
vnner = EntityRecognizer(vi_nlp.vocab)
vnner.from_disk("vn_models\\vi_nermodel")

vi_nlp.pipeline.append(vnner)

doc = vi_nlp(u"Tôi là sinh viên năm nhất sống và học tập ở thủ đô Hà Nội.")
for x in [(w.text, w.lemma_, w.pos_, w.tag_, w.dep_, w.shape_, w.is_alpha, w.is_stop) for w in doc]:
    print(x)
for X in doc.noun_chunks:
    print(X.text, X.label_, X.root.text)
for X in doc.ents:
    print(X.text, X.label_)
