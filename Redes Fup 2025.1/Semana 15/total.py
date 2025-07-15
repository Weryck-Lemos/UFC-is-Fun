def calcular(prod, carr):
    total = 0
    for x in carr:
        if x in prod:
            total += prod[x]
    return total

import ast
prod = ast.literal_eval(input())
carr = ast.literal_eval(input())

total = calcular(prod, carr)
print(f"Valor total do carrinho: R$ {total:.2f}")
