n = int(input())
tot =0

while n>0:
    num = int(input())

    if num%2==0:
        tot+=num

    else:
        tot-=num
    n-=1

print(tot)