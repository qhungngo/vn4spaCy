# coding: utf8
from __future__ import unicode_literals

from ...symbols import NOUN, PROPN, PRON


def noun_chunks(obj):
    """
    Detect base noun phrases from a dependency parse. Works on both Doc and Span.
    """
    labels = [
        "nsubj",
        "dobj",
        "obl",
        "obj",
        "nsubjpass",
        "pcomp",
        "compound",
        "pobj",
        "dative",
        "appos",
        "attr",
        "ROOT",
    ]
    
    # print("syntax_iterators.py for Vietnamese")
    
    doc = obj.doc  # Ensure works on both Doc and Span.
    np_deps = [doc.vocab.strings.add(label) for label in labels]
    conj = doc.vocab.strings.add("conj")
    np_label = doc.vocab.strings.add("NP")
    seen = set()
    
    print("np_deps:", np_deps)
    
    for i, word in enumerate(obj):
        if word.tag_ not in ("P", "N", "Nc", "Np", "Nu"):
            continue

        # Prevent nested chunks from being produced
        if word.i in seen:
            continue

        #print(word.i, word.text, word.tag_, word.dep, conj)
        if word.dep in np_deps:
            if any(w.i in seen for w in word.subtree):
                continue
            i_left_edge = i_right_edge = word.i
            while i_left_edge > word.left_edge.i:
                if (obj[i_left_edge-1].tag_ in ["E", "R"]):
                    break
                i_left_edge -= 1
            while i_right_edge < word.right_edge.i:
                if (obj[i_right_edge+1].tag_ in ["E", "R"]):
                    break
                i_right_edge += 1
            #print([obj[j].text+"/"+obj[j].tag_ for j in range(word.left_edge.i, word.right_edge.i+1)])
            seen.update(j for j in range(i_left_edge, i_right_edge+1))
            yield i_left_edge, i_right_edge+1, np_label
        elif word.dep == conj:
            head = word.head
            while head.dep == conj and head.head.i < head.i:
                head = head.head
            # If the head is an NP, and we're coordinated to it, we're an NP
            if head.dep in np_deps:
                if any(w.i in seen for w in word.subtree):
                    continue
                seen.update(j for j in range(word.i, word.right_edge.i+1))
                yield word.i, word.right_edge.i+1, np_label


SYNTAX_ITERATORS = {"noun_chunks": noun_chunks}
