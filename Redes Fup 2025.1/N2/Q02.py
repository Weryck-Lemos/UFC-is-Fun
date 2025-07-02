n = int(input())
entrada = []
for _ in range(n):
    entrada.append(int(input()))
    
codigo = input().strip()

resultado = []

if codigo == 'P':
    resultado = [x for x in entrada if x % 2 == 0]
elif codigo == 'I':
    resultado = [x for x in entrada if x % 2 != 0]
elif codigo == '+':
    resultado = [x for x in entrada if x > 0]
elif codigo == '-':
    resultado = [x for x in entrada if x < 0]

print(resultado)