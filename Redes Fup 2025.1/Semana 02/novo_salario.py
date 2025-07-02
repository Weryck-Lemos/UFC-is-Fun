salario = float(input())
percentual = int(input())

ans = salario * (1+ percentual/100)

print(f"Salário atual é R$ {salario:.2f} com o aumento de {percentual}%, o novo salário fica de R$ {ans:.2f}")