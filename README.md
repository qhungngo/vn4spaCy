# vnSpaCyAddon

# Start with Standard library in spaCy

    from spacy.lang.vi import Vietnamese
    nlp = Vietnamese()
    doc = nlp(u"Tôi là sinh viên năm nhất sống và học tập ở thủ đô Hà Nội.")
    print([(w.text, w.lemma_, w.pos_, w.tag_, w.dep_) for w in doc])



