n = int(input())
precos = [float(input()) for _ in range(n)]
quantidades = [int(input()) for _ in range(n)]

gastos = [precos[i] * quantidades[i] for i in range(n) if quantidades[i] > 0]
total = sum(gastos)

print(f"O total da feira será de R$ {total:.2f} e o valor gasto por produto será de:")
for valor in gastos:
    print(f"R$ {valor:.2f}")
