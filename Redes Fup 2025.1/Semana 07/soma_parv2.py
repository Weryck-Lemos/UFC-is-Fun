n = int(input())
i = 0
tot = 0
num = 0
while i<n:
    anterior = num
    num = int(input())
    if num%2==0:
        tot += num
    
    else:
        if i != 0:
            tot -=abs(num - anterior)
    i+=1

print(tot)