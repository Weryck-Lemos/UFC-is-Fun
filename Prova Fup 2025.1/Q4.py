classe = int(input())
sexo = input()
idade = int(input())

if sexo=='M' and classe==1:
    print("Sobreviveu")

elif sexo == 'M' and (idade>=30 and idade<=45) and (classe==2 or classe==3):
    print("Sobreviveu")

elif sexo=='F' and classe==1 and idade<=40:
    print("Sobreviveu")

elif idade<=12 and (classe == 1 or classe==2):
    print("Sobreviveu")

elif idade>60 and (classe==2 or classe==3):
    print("Sobreviveu")

elif sexo=='F' and classe == 2 and (idade>=20 and idade<=35):
    print("Sobreviveu")

else:
    print("Morreu")

