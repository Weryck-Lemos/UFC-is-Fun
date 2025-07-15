def contador(l, n):
    oco = 0
    mult=0
    for x in l:
        if x==n:
            oco+=1
        if x%n==0:
            mult +=1
    return oco, mult

txt = input()
txt = txt.split()
l = [int(x) for x in txt]
n = int(input())

oco, mult = contador(l,n)
print(f"O {n} ocorre {oco} vezes na Lista e tem {mult} múltiplos")