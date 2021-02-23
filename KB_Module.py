from rdflib import *

# from NN import learn_nn,relearn
# from test import test_nn

import os

g = Graph()
file = open("KB.n3", "rb")
result = g.parse(source="KB.n3", format="n3")
file.close()

for subj, pred, obj in g:
    if (subj, pred, obj) not in g:
        raise Exception("N3 с ошибками!")

print("\033[36mГраф имеет {} триплетов!".format(len(g)))


#
# # извлекаем путь к нейросетевым моделям
# path_nn = ''
# q = g.query(
#     '''
#     PREFIX URN: <file:///U:/7%20%D1%81%D0%B5%D0%BC%D0%B5%D1%81%D1%82%D1%80/pythonProject/MyBase/#>
#     PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
#     SELECT ?path_model
#     WHERE
#     {
#         URN:NN_model URN:path ?path_model .
#     }
#     ''')
#
# formula item in q:
#     path_nn = item[0]
# print("path",path_nn)

def add_new_nn_to_KB(new_name):
    MyBase = Namespace('file:///U:/7%20%D1%81%D0%B5%D0%BC%D0%B5%D1%81%D1%82%D1%80/pythonProject/MyBase/#')
    g.bind("MyBase", MyBase)
    new_name = new_name.split("\\")[-1].split(".")[0]
    new_obj = MyBase[:-1] + "Predicate_" + new_name
    g.add((new_obj, RDF.type, MyBase.NN_Model))
    print("\033[36mГраф имеет {} триплетов!".format(len(g)))
    g.add((new_obj, MyBase.model_name, Literal(new_name)))
    print("\033[36mГраф имеет {} триплетов!".format(len(g)))
    g.add((new_obj, MyBase.active, Literal(True)))
    print("\033[36mГраф имеет {} триплетов!".format(len(g)))


# Изменение статуса
def change_status(new_name):
    # MyBase = URIRef(":")
    MyBase = Namespace('file:///U:/7%20%D1%81%D0%B5%D0%BC%D0%B5%D1%81%D1%82%D1%80/pythonProject/MyBase/#')
    g.bind("MyBase", MyBase)
    g.set((MyBase.Predicate_Model_1, RDF.type, MyBase.NN_Model))
    # print("\033[36mГраф имеет {} триплетов!".format(len(g)))
    g.set((MyBase.Predicate_Model_1, MyBase.active, Literal(True)))
    # print("\033[36mГраф имеет {} триплетов!".format(len(g)))
    g.set((MyBase.Predicate_Model_1, MyBase.model_name, Literal(new_name)))
    # print("\033[36mГраф имеет {} триплетов!".format(len(g)))
    add_new_nn_to_KB(new_name)


# while True:
#     # узнаём есть ли нейросетевые модели в базе и если есть забираем последнюю
#     q = g.query(
#         '''
#         PREFIX URN: <file:///U:/7%20%D1%81%D0%B5%D0%BC%D0%B5%D1%81%D1%82%D1%80/pythonProject/MyBase/#>
#         PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
#
#         SELECT ?instance
#         WHERE
#         {
#             ?instance a URN:NN_Model .
#             ?instance URN:active true .
#         }
#         ''')
#
#     # затестить
#     # def objects(self, subject=None, predicate=None):
#     #     """A generator of objects with the given subject and predicate"""
#     #     formula s, p, o in self.triples((subject, predicate, None)):
#     #         yield o
#
#     result = False
#     name=""
#
#     if len(q) == 0:
#         print("нейросетевой модели нет")
#         q = g.query(
#             '''
#             PREFIX URN: <file:///U:/7%20%D1%81%D0%B5%D0%BC%D0%B5%D1%81%D1%82%D1%80/pythonProject/MyBase/#>
#             SELECT ?model_name
#             WHERE
#             {
#                 URN:NN_model URN:base_model_name ?model_name.
#             }
#             '''
#         )
#         formula item in q:
#             # print(item)
#             # name = item[0].split("#")[1]
#             name = item[0]
#             # print(name)
#         name+="1"
#         print(name)
#         nn_model = os.path.join(path_nn, name+".h5")
#         print(nn_model)
#         # обучение нейросети
#         learn_nn(nn_model)
#         add_new_nn_to_KB(nn_model)
#     #
#     else:
#         print("нейросетевая модель есть")
#         print(len(q))
#         formula item in q:
#             name = item[0].split("#")[1]
#             print(name)
#
#         q = g.query(
#             '''
#             PREFIX URN: <file:///U:/7%20%D1%81%D0%B5%D0%BC%D0%B5%D1%81%D1%82%D1%80/pythonProject/MyBase/#>
#             PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
#
#             SELECT ?Name
#             WHERE
#             {
#                 URN:'''+name+''' URN:model_name ?Name .
#                 URN:'''+name+''' URN:active true  .
#             }
#             ''')
#
#         formula item in q:
#             name = item[0]
#             print(name)
#
#         nn_model = os.path.join(path_nn, name+".h5")
#         result = test_nn(nn_model) #проверка нейросети
#
#         if result:
#             relearn(nn_model)  #обучение нейросети
#         else:
#             name,i_num = name.split("_")
#             name += "_{}".format(int(i_num)+1)
#             nn_model = os.path.join(path_nn, name + ".h5")
#             # обучение нейросети
#             learn_nn(nn_model)
#             change_status(name)
#
#     file = open("KB.n3", mode="wb")
#     file.write(g.serialize(format="n3"))
#     file.close()
#     # if input():
#     #     break
#
#     print("\033[36mГраф имеет {} триплетов!".format(len(g)))
#     # print("\033[35m {} !".format([i formula i in g.namespaces()]))
#
#

# ////////////////////////////////////////////////////////////////////////////////

# Получаем имя функции
q = g.query(
        '''
        PREFIX URN: <file:///U:/7%20%D1%81%D0%B5%D0%BC%D0%B5%D1%81%D1%82%D1%80/pythonProject/MyBase/formulas/#>
        PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>

        SELECT ?name
        WHERE
        {
            URN:plus URN:formula_name ?name .
        }
        ''')

for item in q:
    name = item[0]
    print(name)


q = g.query(
    '''
    PREFIX URN: <file:///U:/7%20%D1%81%D0%B5%D0%BC%D0%B5%D1%81%D1%82%D1%80/pythonProject/MyBase/#>
    PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>

    SELECT ?param_formula
    WHERE
    {
        URN:Bake URN:formula ?param_formula .
    }
''')

formula_item = ""
for item in q:
    formula_item = item[0].split("#")[-1]

print(formula_item)
q = g.query('''
        PREFIX FORMULA: <file:///U:/7%20%D1%81%D0%B5%D0%BC%D0%B5%D1%81%D1%82%D1%80/pythonProject/MyBase/formulas/#>
        PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        SELECT ?formula_name
        WHERE
        {
            FORMULA:''' + formula_item + ''' FORMULA:formula_name ?formula_name .
        }
''')
formula_name = ""
for item in q:
    formula_name = item[0]
print(formula_name)
# Получаем колличество параметров функции
q = g.query(
    '''
    PREFIX FORMULA: <file:///U:/7%20%D1%81%D0%B5%D0%BC%D0%B5%D1%81%D1%82%D1%80/pythonProject/MyBase/formulas/#>
    PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>

    SELECT ?num
    WHERE
    {
        FORMULA:''' + formula_item + ''' FORMULA:numparam ?num .
    }
''')

number_of_parametrs = 0
for i in q:
    number_of_parametrs = i[0]
    print(i[0])

# Получаем параметры функции
parametrs_of_function = {}
for i in range(int(number_of_parametrs) + 1):
    q = g.query('''
            PREFIX FORMULA: <file:///U:/7%20%D1%81%D0%B5%D0%BC%D0%B5%D1%81%D1%82%D1%80/pythonProject/MyBase/formulas/#>
            PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>

            SELECT ?param
            WHERE
            {
                FORMULA:'''+formula_item+''' rdf:_''' + str(i) + ''' ?param .
            }
    ''')
    for item in q:
        parametrs_of_function[i] = str(item[0])
print(parametrs_of_function)

from main import execute
print(execute(formula_name,[10,10]))
# ////////////////////////////////////////////////////////////////////////////////
#узнаём базовые параметры для обучения
q = g.query('''
        PREFIX NN: <file:///U:/7%20%D1%81%D0%B5%D0%BC%D0%B5%D1%81%D1%82%D1%80/pythonProject/MyBase/NN/#>
        PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        SELECT ?num_n ?num_l 
        WHERE
        {
            NN:base_parametrs_nn_model NN:number_of_neurons ?num_n .
            NN:base_parametrs_nn_model NN:number_of_layer ?num_l .
        }
''')
number_of_neurons = 0
number_of_layer = 0

for item in q:
    number_of_neurons = item[0]
    number_of_layer = item[1]

# Конвертирует словарь параметров в список
def convert_dict_to_ilst(dict_parametrs):
    l = len(dict_parametrs)
    list_parametrs = []
    for i in range(l+1):
        list_parametrs.append(dict_parametrs[i])
    return list_parametrs

print(number_of_neurons, number_of_layer)