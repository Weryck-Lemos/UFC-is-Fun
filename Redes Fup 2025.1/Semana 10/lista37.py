n = int(input())
vet = [int(input()) for x in range(n)]
vet2 = [x**3 if x%2==0 else x**7 for x in vet ]

print(vet2)