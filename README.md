

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

    Training pipeline: ['tagger', 'parser', 'ner']
    Starting with blank model 'vi'
    Counting training words (limit=0)
    
    Itn    Dep Loss    NER Loss      UAS    NER P    NER R    NER F    Tag %  Token %  CPU WPS  GPU WPS
    ---  ----------  ----------  -------  -------  -------  -------  -------  -------  -------  -------
      0   25478.256       0.000   47.449    0.000    0.000    0.000   81.171  100.000     3611        0
      1   21602.918       0.000   61.044    0.000    0.000    0.000   85.044  100.000     4544        0
      2   19167.105       0.000   64.053    0.000    0.000    0.000   85.974  100.000     4541        0
      3   17028.249       0.000   65.227    0.000    0.000    0.000   86.034  100.000     3660        0
      4   15898.378       0.000   65.691    0.000    0.000    0.000   86.434  100.000     4610        0
      5   14714.223       0.000   65.937    0.000    0.000    0.000   86.660  100.000     4756        0
      6   13696.655       0.000   66.201    0.000    0.000    0.000   86.686  100.000     4936        0
      7   12842.938       0.000   66.319    0.000    0.000    0.000   86.477  100.000     4765        0
      8   12163.123       0.000   66.700    0.000    0.000    0.000   86.486  100.000     4975        0
      9   11333.333       0.000   66.565    0.000    0.000    0.000   86.555  100.000     5026        0
     10   10845.724       0.000   66.677    0.000    0.000    0.000   86.503  100.000     5278        0
     11    9880.339       0.000   66.616    0.000    0.000    0.000   86.477  100.000     4567        0
     12    9603.750       0.000   66.893    0.000    0.000    0.000   86.399  100.000     4955        0
     13    8880.109       0.000   66.724    0.000    0.000    0.000   86.390  100.000     4607        0
     14    8396.288       0.000   66.856    0.000    0.000    0.000   86.382  100.000     3135        0
     15    8067.455       0.000   66.964    0.000    0.000    0.000   86.208  100.000     3691        0
     16    7788.083       0.000   67.089    0.000    0.000    0.000   86.252  100.000     2806        0
     17    7228.533       0.000   67.095    0.000    0.000    0.000   86.165  100.000     3518        0
     18    7051.829       0.000   66.977    0.000    0.000    0.000   86.364  100.000     2971        0
     19    6600.162       0.000   66.886    0.000    0.000    0.000   86.434  100.000     3431        0
     20    6243.790       0.000   66.937    0.000    0.000    0.000   86.425  100.000     4045        0
     21    6003.909       0.000   66.832    0.000    0.000    0.000   86.451  100.000     4063        0
     22    5850.939       0.000   66.603    0.000    0.000    0.000   86.408  100.000     3710        0
     23    5424.487       0.000   66.815    0.000    0.000    0.000   86.451  100.000     3639        0
     24    5256.639       0.000   66.684    0.000    0.000    0.000   86.356  100.000     3548        0
     25    5246.070       0.000   66.700    0.000    0.000    0.000   86.347  100.000     2685        0
     26    4871.565       0.000   66.646    0.000    0.000    0.000   86.312  100.000     3716        0
     27    4669.841       0.000   66.667    0.000    0.000    0.000   86.286  100.000     2750        0
     28    4566.981       0.000   66.771    0.000    0.000    0.000   86.364  100.000     4446        0
     29    4258.587       0.000   66.876    0.000    0.000    0.000   86.347  100.000     3937        0
    ✔ Saved model to output directory
    vn_models\model-final
    ✔ Created best model
    vn_models\model-best
    
## Build package
