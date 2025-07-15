def func(dic):
    return max(dic.values()), min(dic.values())

import ast
dic = ast.literal_eval(input())
mai, men = func(dic)
print(men, mai)