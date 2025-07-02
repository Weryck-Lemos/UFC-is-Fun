def pa(a1, r, n):
    return a1 + r*(n-1)

a1 = int(input())
r = int(input())
n = int(input())
print(f"O {n}-ésimo termo da PA de razão {r} e primeiro elemento {a1} é igual a {pa(a1,r,n)}")