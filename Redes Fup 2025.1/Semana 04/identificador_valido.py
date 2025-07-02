d1 = int(input())
d2 = int(input())
d3 = int(input())
d4 = int(input())
d5 = int(input())

r1 = (d1%2 !=0 and d3%2 !=0 and d5%2 !=0)
r2 = (d2%2==0 and d4%2==0)
r3 = d3== d1+4
r4 = d5 == d3+2

if(r1 and r2 and r3 and r4): print("SIM")
else: print("NAO")