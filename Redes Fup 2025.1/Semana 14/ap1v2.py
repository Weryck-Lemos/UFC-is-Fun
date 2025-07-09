import ast
Dic = ast.literal_eval(input())

tot = 0
for x in Dic.values():
    tot +=x

media = tot/len(Dic)

print(f"Média da turma: {media:.2f}\n"
      f"Alunos com notas maior ou igual a média da turma:")

for aluno, nota in Dic.items():
    if nota >media:
        print(f"{aluno}: {nota:.2f}")