def pa(a1, r, n):
    return a1 + r*(n-1)

def sum(a1,r, n):
    an = pa(a1,r,n)

    return (a1+an) *n/2

a1 = int(input())
r = int(input())
n = int(input())
print(f"A soma de uma PA com o primeiro elemento {a1} e {n}-ésimo elemento {pa(a1,r,n)} é igual a {sum(a1,r,n):.0f}")