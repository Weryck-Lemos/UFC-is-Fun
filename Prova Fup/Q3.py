d1 = int(input())
d2 = int(input())
d3 = int(input())
d4 = int(input())
d5 = int(input())

cond = 0

if d3 == d1+d2: cond+=1

if d4%2==0:
    if d4== 2*d2: cond+=1
else: 
    if d4==2*d2 +1:cond+=1


if d5%d3==0:
    if(d5== 2*d3): cond+=1
else: 
    if d5==2*d3 -1: cond+=1

if cond==3:
    print("SIM")

else:
    print("NAO")

