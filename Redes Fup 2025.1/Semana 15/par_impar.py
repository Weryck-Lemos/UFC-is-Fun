def contador(l):
    par = 0
    impar = 0
    for i in l:
        if i%2==0:
            par+=1
        else:
            impar+=1
    return par,impar

n = int(input())
l = []
i = 0
while i < n:
    x = int(input())
    l.append(x)
    i += 1

p,i = contador(l)

if i == 0:
    print(f"Foram fornecidos {n} números inteiros positivos e todos foram pares.")
elif p == 0:
    print(f"Foram fornecidos {n} números inteiros positivos com todos foram impares.")
else:
    print(f"Foram fornecidos {n} números inteiros positivos, sendo que {p} foram pares e {i} impares.")

