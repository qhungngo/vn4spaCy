# coding: utf8
from __future__ import unicode_literals

from ...symbols import POS, PUNCT, SYM, ADJ, CCONJ, NUM, DET, ADV, ADP, X, VERB
from ...symbols import NOUN, PROPN, PART, INTJ, SPACE, PRON, AUX

TAG_MAP = {
    ".": {POS: PUNCT, "PunctType": "peri"},
    ",": {POS: PUNCT, "PunctType": "comm"},
    "-LRB-": {POS: PUNCT, "PunctType": "brck", "PunctSide": "ini"},
    "-RRB-": {POS: PUNCT, "PunctType": "brck", "PunctSide": "fin"},
    "(": {POS: PUNCT, "PunctType": "brck", "PunctSide": "ini"},
    ")": {POS: PUNCT, "PunctType": "brck", "PunctSide": "fin"},
    "``": {POS: PUNCT, "PunctType": "quot", "PunctSide": "ini"},
    '""': {POS: PUNCT, "PunctType": "quot", "PunctSide": "fin"},
    "''": {POS: PUNCT, "PunctType": "quot", "PunctSide": "fin"},
    ":": {POS: PUNCT},
    ";": {POS: PUNCT},
    "$": {POS: SYM, "Other": {"SymType": "currency"}},
    "£": {POS: SYM, "Other": {"SymType": "currency"}},
    "€": {POS: SYM, "Other": {"SymType": "currency"}},
    "#": {POS: SYM, "Other": {"SymType": "numbersign"}},
    "A": {POS: ADJ},
    "N": {POS: NOUN, "Number": "sing"},
    "Np":{POS: PROPN, "NounType": "prop", "Number": "sing"},
    "Nc": {POS: NOUN},
    "Nu": {POS: NOUN},
    "Ny": {POS: NOUN},
    "P": {POS: PRON, "PronType": "prs"},
    "R": {POS: ADV},
    "V": {POS: VERB},
    "E": {POS: ADP},
    "M": {POS: NUM, "NumType": "card"},
    "CC": {POS: CCONJ, "ConjType": "coor"},
    "T": {POS: INTJ},
    "PUNCT": {POS: PUNCT},
    "AUX": {POS: AUX},
    "X": {POS: X},
    "C": {POS: CCONJ},
    "CC": {POS: CCONJ},
    "L": {POS: DET},
}
