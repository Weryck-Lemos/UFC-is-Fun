n = int(input())
tot = 0
while n>0:
    num = int(input())

    tot += num*n
    n-=1

print(tot)