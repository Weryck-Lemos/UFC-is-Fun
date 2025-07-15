def contador(l):
    par = 0
    impar = 0
    zero = 0
    for i in l:
        if i==0:
            zero+=1
        elif i%2==0:
            par+=1
        else:
            impar+=1
    return par, impar, zero

txt = input()
txt = txt.split()
l = [int(x) for x in txt]
p,i,z = contador(l)
print(f"A lista contem {p} pares, {i} impares e {z} zeros")