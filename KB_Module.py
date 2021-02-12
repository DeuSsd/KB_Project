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

from NN import *
from test import *
# print("путь к нейросетевым моделям",path_model)

def change_status(new_name):

    data='''
    <U:/7%20%D1%81%D0%B5%D0%BC%D0%B5%D1%81%D1%82%D1%80/pythonProject#'''+new_name+'''>  <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <U:/7%20%D1%81%D0%B5%D0%BC%D0%B5%D1%81%D1%82%D1%80/pythonProject#NN_Model>.
    <U:/7%20%D1%81%D0%B5%D0%BC%D0%B5%D1%81%D1%82%D1%80/pythonProject#'''+new_name+'''> <U:/7%20%D1%81%D0%B5%D0%BC%D0%B5%D1%81%D1%82%D1%80/pythonProject#model_name> "'''+new_name+'''" .
    <U:/7%20%D1%81%D0%B5%D0%BC%D0%B5%D1%81%D1%82%D1%80/pythonProject#'''+new_name+'''> <U:/7%20%D1%81%D0%B5%D0%BC%D0%B5%D1%81%D1%82%D1%80/pythonProject#active true> .
    '''

    g.parse(data,format='n3')

while True:
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


    result = False
    name=""

    if len(q) == 0:
        print("нейросетевой модели нет")
        q = g.query(
            '''
            SELECT ?model_name
            WHERE  
            {
                :NN_model :base_model_name ?model_name.
                    }
                    ''')

        for item in q:
            name = item[0].split("#")[1]
            print(name)
        name+="_1"
        nn_model = os.path.join(path, name+".h5")
        learn_nn(nn_model)  # обучение нейросети
    else:
        print("нейросетевая модель есть")
        print(len(q))
        for item in q:
            name = item[0].split("#")[1]
            print(name)

        q = g.query(
            '''
            SELECT ?Name
            WHERE  
            {
                :'''+name+''' :model_name ?Name .
                :'''+name+''' :active true  .
            }
            ''')

        for item in q:
            name = item[0]
            print(name)

        nn_model = os.path.join(path, name+".h5")

        result = test_nn(nn_model) #проверка нейросети

        if result:
            relearn(nn_model)  #обучение нейросети
        else:

            name,i_num = name.split("_")

            name += "_{}".format(int(i_num)+1)
            nn_model = os.path.join(path, name + ".h5")
            learn_nn(nn_model)  # обучение нейросети
            change_status(name)








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
