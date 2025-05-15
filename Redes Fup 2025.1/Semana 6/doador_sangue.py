peso = float(input())
idade = int(input())
resp1 = int(input())
resp2 = int(input())

if peso >= 50 and (idade>=16 and idade <=69) and resp1==1 and resp2==0:
    print("Esta Apto")
    
else:
    print("Nao Esta Apto")