def bhaskara(a, b, c):
    delta = b**2 - 4*a*c
    
    if delta < 0:
        print("Sem raízes reais")
    elif delta == 0:
        x = -b / (2*a)
        print(f"Raiz única: {x}")
    else:
        raiz1 = (-b + delta**0.5) / (2*a)
        raiz2 = (-b - delta**0.5) / (2*a)
        print(f"Duas raízes reais: {raiz1} e {raiz2}")

