n = int(input())
vet1 = [int(input()) for x in range(n)]

m = int(input())
vet2 = [int(input()) for x in range(m)]

vet3 = []
for i in range(n):
    for j in range(m):
        if(vet1[i]== vet2[j] and vet1[i] not in vet3):
            vet3.append(vet1[i])

print(vet3)