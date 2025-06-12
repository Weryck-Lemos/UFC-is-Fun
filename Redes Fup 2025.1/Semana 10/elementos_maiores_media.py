n  = int(input())
vet = [float(input()) for x in range(n)]

media = sum(vet)/n
vet2 = [x for x in vet if x>media]

print(f"Média igual a {media:.6f}")
print(f"A lista com os valores maiores que a média: {vet2}")