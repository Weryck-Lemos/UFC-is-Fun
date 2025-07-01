n = int(input())

l1 = []
l2 = []

for _ in range(n):
    x = int(input())
    l1.append(x)
    
for _ in range(n):
    x = int(input())
    l2.append(x)

op = input()
l3 = []


if op =="*":
    for _ in range(n):
        l3.append(l1[_]* l2[_])   

elif op=="-":
    for _ in range(n):
        l3.append(l1[_] - l2[_])
       
elif op=="+":
    for _ in range(n):
        l3.append(l1[_] + l2[_])

else:
    for _ in range(n):
        if l2[_]==0:
            l3.append(-1)
        else:
            l3.append(l1[_]/ l2[_])
                     
print(l3)
    
    