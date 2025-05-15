c = float(input())
i = float(input())
t = float(input())

m = c*(1+ i/100)**t
juros = m-c
rendimento = juros/c

print(f"A aplicacao rendeu {juros:.2f} reais que equivale a um rendimento percentual de {100*rendimento:.2f}%.\n")