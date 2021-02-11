from rdflib import *


g = Graph()

file = open("KB.n3","rb")

result = g.parse(source="KB.n3",format="n3")

for subj, pred, obj in g:
    if (subj, pred, obj) not in g:
        raise Exception("N3 с ошибками!")


print("\033[36mГраф имеет {} триплетов!".format(len(g)))


# извлекаем путь к нейросетевым моделям
q = g.query(
    '''
    PREFIX URN: <file:///U:/7%20%D1%81%D0%B5%D0%BC%D0%B5%D1%81%D1%82%D1%80/pythonProject/MyBase/#>
    PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
    SELECT ?path_model
    WHERE  
    {
        :NN_model :path ?path_model .
    }
    ''')

path = ''

for item in q:
    path = item[0]

print("path",path)

# print("путь к нейросетевым моделям",path_model)

# узнаём есть ли нейросетевые модели в базе и если есть забираем последнюю
q = g.query(
    '''
    PREFIX URN: <file:///U:/7%20%D1%81%D0%B5%D0%BC%D0%B5%D1%81%D1%82%D1%80/pythonProject/MyBase/#>
    PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
    
    SELECT ?instance
    WHERE  
    {
        ?instance a :NN_Model .
        ?instance :active true .
    }
    ''')

from NN import *
from test import *

result = False

while True:
    if len(q) == 0:
        print("нейросетевой модели нет")
    else:
        print("нейросетевая модель есть")

        for item in q:
            name = item[0].split("#")[1]
            print(name)

        q = g.query(
            '''
            SELECT ?model_name
            WHERE  
            {
                :'''+name+''' :model_name ?model_name .
            }
            ''')

        for item in q:
            name = item[0]
            print(name)



        nn_model = os.path.join(path, name)

        result = test_nn(nn_model) #проверка нейросети

        if result:
            learn_nn(path,name)  #обучение нейросети



#
#
# q = g.query(
#     '''
#     PREFIX URN: <file:///U:/7%20%D1%81%D0%B5%D0%BC%D0%B5%D1%81%D1%82%D1%80/%D0%9F%D1%80%D0%98%D0%BD%D1%82%D0%A1%D0%B8%D1%81%D1%82/NonExistent/KB.n3#>
#     SELECT ?pred ?obj
#     WHERE
#     {?subj ?pred ?obj.}
#     '''
#
# )
#
# # for pred,obj in q:
# #     print(pred.split("#")[1],obj.split("#")[1])
#
# # for pred,obj in q:
# #     print(pred,obj)
# #
# # query = 'SELECT  ?obj  WHERE { ?obj a rdfs:Class.}'
# #
# # print(g.serialize(query, format = "xml"))
# #
#
#
# # print(g.serialize(format="n3").decode())
