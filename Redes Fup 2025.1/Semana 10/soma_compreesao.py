n = int(input())
l1 = [int(input()) for x in range(n)]
l2 = [int(input()) for x in range(n)]
soma = [l1[i] + l2[n-i-1] for i in range(n)]

for x in soma:
    print(x)