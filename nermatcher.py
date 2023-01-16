import spacy
from collections import Counter
from spacy import displacy
from string import punctuation

nlp = spacy.load('ru_core_news_lg', disable=['ner'])
config = {
   "phrase_matcher_attr": 'LEMMA',
   "validate": True,
   "overwrite_ents": False,
   "ent_id_sep": "||",
}
ruler = nlp.add_pipe("entity_ruler", config=config)


tlist = open('C:/Main/slovari/ИЗО.txt', encoding='utf-8').read().splitlines()
patterns = []
for i in tlist:
   patterns.append({"label": "TERM", "pattern": i})
ruler.add_patterns(patterns)
doc = nlp(open('C:/Users/user/Desktop/3 класс/изо_готово/Tbook(P)_R_Iz_03_03_GoNe_0_A_0_2014_6962.txt', 'r', encoding='utf-8').read())


terminy = [(ent.text) for ent in doc.ents]
tokens = [token.lemma_ for token in doc if token.lemma_ not in punctuation]


print(f'{terminy}')
print('Количество терминов:',len(terminy))
print('Количество токенов:',len(tokens))
print('Ratio:',len(terminy) / len(tokens))

d = Counter(terminy).most_common()

# for i in d:
#    print(i[1])


displacy.serve(doc, style='ent')