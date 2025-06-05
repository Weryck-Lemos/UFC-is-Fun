n = int(input())
l1 = []
l2 = []
soma = []

i=0

while i<n:
    x = int(input())
    l1.append(x)
    i+=1

i=0
while i<n:
    x = int(input())
    l2.append(x)
    i+=1

i=0
j=n-1
while i<n:
    soma.append(l1[i]+l2[j])
    i+=1
    j-=1

i=0
while i<n:
    print(f"{soma[i]} ")
    i+=1