import ast
dic1 = ast.literal_eval(input())
dic2 = ast.literal_eval(input())
dic3 = {}

for c,v in dic1.items():
    dic3[c] = v

for c,v in dic2.items():
    dic3[c] = v

for c,v in sorted(dic3.items()):
    print(f"{c}: {v}")