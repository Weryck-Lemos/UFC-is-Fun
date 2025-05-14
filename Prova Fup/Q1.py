a1 = int(input())
a2 = int(input())
a3 = int(input())

if a1+a2+a3 != 180:
    print("Não é triângulo")

elif a1<90 and a2<90 and a3<90:
    print("Acutângulo")

elif a1==90 or a2==90 or a3==90:
    print("Retângulo")

else:
    print("Obtusângulo")


