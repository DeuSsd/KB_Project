import sys

def parametrs_to_string(param):
    str_p = ""

    for item in param:
        str_p+=str(item)
        str_p+=','
    str_p = str_p[:-1]
    return  str_p

# while True:
def execute():
    result = 0
    a =input()
    b = input()
    param = [float(a),float(b)]
    fun1 = input()
    param = parametrs_to_string(param)

    if  "formula."+fun1 not in sys.modules:
        exec("from formula import {}".format(fun1))
    else:
        exec("reload({})".format(fun1))

    exec('result = {}.{}({})'.format(fun1,fun1,param))
    return result





