dia = int(input())
mes = int(input())
ano = int(input())

diaf = int(input())
mesf = int(input())
anof = int(input())

ans = anof- ano
if mesf < mes: ans -=1

else:
    if mesf == mes:
        if diaf < dia: ans-=1

print(ans)