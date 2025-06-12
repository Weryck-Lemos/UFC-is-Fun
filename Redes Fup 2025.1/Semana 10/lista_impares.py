n = int(input())
vet = [int(input()) for x in range(n)]
vet2 = [x for x in vet if x%2!=0 ]
print(vet2)