n = int(input())
l = [int(input()) for i in range(n)]

find = int(input())
id = -1

for i in range(n):
    if l[i]==find:
        id = i
        break

print(id)