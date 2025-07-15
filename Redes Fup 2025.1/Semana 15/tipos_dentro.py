def contador(dic):
    i = 0
    f = 0
    s = 0
    for x in dic.values():
        if type(x) == int:
            i+=1
        elif type(x) == float:
            f+=1
        else:
            s +=1
    return i,f,s

import ast
dic = ast.literal_eval(input())
i,f,s = contador(dic)
print(f"int={i}\nfloat={f}\nstring={s}")