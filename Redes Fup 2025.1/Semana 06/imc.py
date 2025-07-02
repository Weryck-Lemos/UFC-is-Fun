peso = float(input())
altura = float(input())

imc = peso/(altura**2)

if imc <17:
    print("muito abaixo do peso")
    
elif imc < 18.5:
    print("abaixo do peso")
    
elif imc < 25:
    print("peso normal")
    
elif imc<30:
    print("acima do peso")
    
elif imc < 35:
    print("obesidade")
    
elif imc<40:
    print("obesidade severa")
    
else:
    print("obesidade morbida")