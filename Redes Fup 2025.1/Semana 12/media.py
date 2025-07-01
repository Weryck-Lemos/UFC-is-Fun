n = int(input())

ap1 = []
ap2 = []
ap3 = []

for _ in range(n):
    x = float(input())
    ap1.append(x)
    
for _ in range(n):
    x = float(input())
    ap2.append(x)
    
for _ in range(n):
    x = float(input())
    ap3.append(x)
    
media = []
aprovados = 0
for _ in range(n):
    media.append((ap1[_] + ap2[_] + ap3[_])/3)
    if media[_]>=7:
        aprovados+=1
        
print(f"Na turma com {n} alunos, tivemos {aprovados} alunos aprovados e {n-aprovados} reprovados.")
