id = int(input())

if id == 1:
    l1 = float(input())
    l2 = float(input())
    print(f"O valor da area do Retangulo e igual a {l1*l2:.2f}")
    
    
    
elif id == 2:
    r = float(input())
    print(f"O valor da area do Circulo e igual a {3.14159* r**2:.2f}")
 
 
    
else:
    base = float(input())
    altura = float(input())

    print(f"O valor da area do Triangulo e igual a {(base*altura)/2:.2f}")
    