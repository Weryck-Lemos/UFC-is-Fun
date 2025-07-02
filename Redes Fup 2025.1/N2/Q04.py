n = int(input())
numeros = [int(input()) for _ in range(n)]

acumulada = [sum(numeros[:i+1]) for i in range(n)]
print(acumulada)