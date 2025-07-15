def calcular(l):
    return sum(l)/len(l)

import ast
dic = ast.literal_eval(input())
print("Listagem dos alunos que foram aprovados na cadeira:")
for c,v in dic.items():
    media = calcular(v)
    if media >= 7.0:
        print(f"{c}: {media:.2f}")