n = int(input())

l1=[]
l2=[]

for _ in range(n):
    x = int(input())
    l1.append(x)
    
for _ in range(n):
    x = int(input())
    l2.append(x)
    
l3=[]

for _ in range(n):
    l3.append(l2.count(l1[_]))
    
print(l3)

