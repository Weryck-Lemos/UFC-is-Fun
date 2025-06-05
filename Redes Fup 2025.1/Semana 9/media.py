n = int(input())

n1 = []
n2 = []
media = []

i=0
while i<n:
    x = float(input())
    n1.append(x)
    i+=1

i=0
while i<n:
    x = float(input())
    n2.append(x)
    
    media.append((n1[i]+n2[i])/2)
    i+=1

i=0
while i<n:
    print(f"{media[i]:.2f} ")
    i+=1