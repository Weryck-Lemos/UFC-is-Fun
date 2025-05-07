n1 = float(input())
n2 = float(input())
media = (n1+n2)/2

if media>=7: print("aprovado")
elif media<4: print("reprovado")
else:
    af = float(input())
    media = (media+af)/2
    if media>=5: print("aprovado na final")
    else: print("reprovado na final")