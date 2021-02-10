# exec('from formula import heatQuantity')
# exec('print(heatQuantity.heatQuantity(0, 10, 1))')
#
# exec('from formula import heatTime')
# exec('print(heatTime.heatTime(10, 100))')
#
#
#

# import formula.plus
from importlib import reload
# from formula import f_plus.

import sys


def str_param(param):
    str_p = ""

    for item in param:
        str_p+=str(item)
        str_p+=','
    str_p = str_p[:-1]
    return  str_p

while True:
    result = ''
    a =input()
    b = input()
    param = [float(a),float(b)]
    fun1 = input()
    param = str_param(param)

    if  "formula."+fun1 not in sys.modules:
        exec("from formula import {}".format(fun1))
    else:
        exec("reload({})".format(fun1))

    exec('result = {}.{}({})'.format(fun1,fun1,param))
    print(result)



