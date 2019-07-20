|NAME |	COMPONENT	| CREATES | DESCRIPTION |
|-----|-----------|---------|-------------|
|tokenizer |Tokenizer	|Doc	|Segment text into tokens.|
|tagger	| Tagger	| Doc[i].tag	| Assign part-of-speech tags.|
|parser	| DependencyParser	| Doc[i].head, Doc[i].dep, Doc.sents, Doc.noun_chunks	| Assign dependency labels.|
|ner	| EntityRecognizer	| Doc.ents, Doc[i].ent_iob, Doc[i].ent_type	| Detect and label named entities.|
|textcat | TextCategorizer	| Doc.cats	| Assign document labels.|
|…	|custom components	| Doc._.xxx, Token._.xxx, Span._.xxx	| Assign custom attributes, methods or properties.|
