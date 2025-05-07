nome = input()
idade = int(input())

ans = ""
if idade<12: ans = "crianca"
elif idade<18: ans = "jovem"
elif idade<65: ans = "adulto"
elif idade<1000: ans = "idoso"
else: ans = "mumia"

print(f"{nome} eh {ans}")