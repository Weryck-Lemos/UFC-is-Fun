L = [int(x) for x in input().split()]
dic = {i:L[i] for i in range(len(L)) if L[i]%2==0}
print(dic)