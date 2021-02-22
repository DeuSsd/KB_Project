import sys
from importlib import reload

import formula


def parametrs_to_string(param):
    str_p = ""

    for item in param:
        str_p+=str(item)
        str_p+=','
    str_p = str_p[:-1]
    return  str_p


def execute(formula_name,parametrs):
    results = []
    i = 0
    parametrs_s = parametrs_to_string(parametrs)
    if  "formula."+formula_name not in sys.modules:
        exec('from formula import {}'.format(formula_name))
        print(1)
    else:
        exec("reload(formula.{})".format(formula_name))
        print(2)
    exec("results.append(formula.{}.{}({}))".format(formula_name,formula_name,parametrs_s))
    return results[0]

if __name__ =="__main__":
    while True:
        print(execute("plus",[2,3]))
        input()

