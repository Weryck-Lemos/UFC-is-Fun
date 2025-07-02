def retangulo(l1, l2):
    return l1*l2

def circulo(r):
    return 3.14159* r**2

def triangulo(base, altura):
    (base*altura)/2

id = int(input())

if id == 1:
    l1 = float(input())
    l2 = float(input())
    print(f"O valor da area do Retangulo e igual a {retangulo(l1,l2):.2f}")
       
elif id == 2:
    r = float(input())
    print(f"O valor da area do Circulo e igual a {circulo(r):.2f}")
    
else:
    base = float(input())
    altura = float(input())

    print(f"O valor da area do Triangulo e igual a {triangulo(base,altura):.2f}")
    