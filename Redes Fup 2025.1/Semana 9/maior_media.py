n = int(input())
alunos = []
media = 0
i=0
while i<n:
    x = float(input())
    alunos.append(x)
    media += x
    i+=1

i=0
media /=n

ans = 0
while i<n:
    if alunos[i]>media:
        ans+=1
    i+=1

print(f"{ans} {media:.2f}")