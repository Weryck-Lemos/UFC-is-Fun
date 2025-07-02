n = int(input())
l = []
i = 0

while i<n:
    x = int(input())
    l.append(x)
    i+=1

find = int(input())
i = 0
id = -1

while i<n:
    if l[i]==find:
        id = i
        break
    i+=1

print(id)