def imposto(value):
    t = 1
    ans = 0

    while t<=12:
        ans += t/100*value
        t+=1

    return ans

num = float(input())
print(f"O total do imposto de renda da pessoa que ganha um salário mensal de {num:.2f} é de {imposto(num):.2f}")