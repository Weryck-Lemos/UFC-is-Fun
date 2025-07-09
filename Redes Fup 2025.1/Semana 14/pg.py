a1 = int(input())
r = int(input())
n = int(input())

dic = {i:a1*r**(i-1) for i in range(1,n+1)}
print(dic)