n = int(input())
lista = []

for _ in range(n):
    x = int(input())
    lista.append(x)
    
i = int(input())
j = int(input())
print(sum(lista[i:j]))

