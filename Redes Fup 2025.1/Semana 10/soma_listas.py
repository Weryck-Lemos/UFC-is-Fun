n = int(input())

l1 = [int(input()) for i in range(n)]
l2 = [int(input()) for i in range(n)]

soma = [l1[i]+l2[i] for i in range(n)]
for i in range(n):
    print(soma[i])