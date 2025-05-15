peso = float(input())
altura = float(input())
idade = int(input())
ano = int(input())
dia = int(input())

ans = (((((peso+altura)/idade)+ ano) *dia) -33) *(idade+7)
print(ans)