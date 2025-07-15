def contador(l):
    return max(l), min(l), sum(l)

n = int(input())
l = []

for _ in range(n):
    x = int(input())
    l.append(x)
maior, menor, soma = contador(l)
print(f"O menor valor e {menor}, o maior {maior} e a soma da lista e {soma}.")
