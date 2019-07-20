

# vn4spaCy

## 1. Build-in word tokenizer

    from spacy.lang.vi import Vietnamese
    nlp = Vietnamese()
    doc = nlp(u"Tôi là sinh viên năm nhất sống và học tập ở thủ đô Hà Nội.")
    for x in [(w.text, w.lemma_, w.pos_, w.tag_, w.dep_) for w in doc]:
        print(x)

**Output:**

    ('Tôi', 'Tôi', '', '', '')
    ('là', 'là', '', '', '')
    ('sinh_viên', 'sinh_viên', '', '', '')
    ('năm', 'năm', '', '', '')
    ('nhất', 'nhất', '', '', '')
    ('sống', 'sống', '', '', '')
    ('và', 'và', '', '', '')
    ('học_tập', 'học_tập', '', '', '')
    ('ở', 'ở', '', '', '')
    ('thủ_đô', 'thủ_đô', '', '', '')
    ('Hà_Nội', 'Hà_Nội', '', '', '')
    ('.', '.', '', '', '')

## 2. Data as UD format
 - [ ] vi_vtb-ud-dev.conllu 
 - [ ] vi_vtb-ud-test.conllu 
 - [ ] vi_vtb-ud-train.conllu

download from > [https://github.com/UniversalDependencies/UD_Vietnamese-VTB](https://github.com/UniversalDependencies/UD_Vietnamese-VTB)
   
## 3. Training Parser:

    mkdir vn_jsons
    python -m spacy convert UD_Vietnamese-VTB-master\vi_vtb-ud-train.conllu vn_jsons
    python -m spacy convert UD_Vietnamese-VTB-master\vi_vtb-ud-dev.conllu vn_jsons
    python -m spacy convert UD_Vietnamese-VTB-master\vi_vtb-ud-test.conllu vn_jsons
    mkdir vn_models
    python -m spacy train vi vn_models vn_jsons\vi_vtb-ud-train.json vn_jsons\vi_vtb-ud-dev.json


