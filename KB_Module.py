from rdflib import *


g = Graph()

file = open("KB.n3","rb")

result = g.parse(source="KB.n3",format="n3")

for subj, pred, obj in g:
    if (subj, pred, obj) not in g:
        raise Exception("N3 с ошибками!")


print("\033[36mГраф имеет {} триплетов!".format(len(g)))


