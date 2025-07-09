import ast
Dic = ast.literal_eval(input())

print(f"Turma de Fundamentos de Programação.\n"
     f"Listagem das notas da AP1:")

for a,n in Dic.items():
    print(f"{a}: {n:.2f}")