def contador(dic):
    i = 0
    for x in dic.values():
        if type(x) == int:
            i+=1
    return i

import ast
dic = ast.literal_eval(input())
i = contador(dic)
print(i)