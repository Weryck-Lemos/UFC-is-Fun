import ast
dic1 = ast.literal_eval(input())
dic2 = ast.literal_eval(input())
dic3 = {}

for c,v in dic1.items():
    dic3[c] = v

for c,v in dic2.items():
    if c in dic3:
        dic3[c]+=v

    else:
        dic3[c] = v
print(dict(sorted(dic3.items())))