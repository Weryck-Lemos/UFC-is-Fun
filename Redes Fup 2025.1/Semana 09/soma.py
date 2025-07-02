n = int(input())

l1 = []
l2 = []
soma = []

i = 0
while i<n:
    x = int(input())
    l1.append(x)
    i+=1

i = 0
while i<n:
    x = int(input())
    l2.append(x)

    soma.append(l1[i]+l2[i])
    i+=1

i=0
while i<n:
    print(soma[i])
    i+=1