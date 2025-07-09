L = [int(x) for x in input().split()]
dic = {i:L[i]**3 if L[i]%2==0 else L[i]**7 for i in range(len(L))}
print(dic)