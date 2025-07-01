def pg(primeiro,razao,n):
    return(primeiro * razao **(n-1))

primeiro = int(input())
razao = int(input())
n = int(input())
print(pg(primeiro, razao, n))

