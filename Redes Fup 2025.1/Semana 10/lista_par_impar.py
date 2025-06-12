n = int(input())
vet = [int(input()) for x in range(n)]
vet2 = [x*10 if x%2==0 else x*5 for x in vet]

print(vet2)