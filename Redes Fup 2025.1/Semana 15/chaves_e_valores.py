def contador(dic):
    key= 0
    value = 0
    for c,v in dic.items():
        if type(c) == int:
            key+=1
        if type(v) == int:
            value+=1
    return key, value

import ast
dic = ast.literal_eval(input())
c,v = contador(dic)
print(c,v)