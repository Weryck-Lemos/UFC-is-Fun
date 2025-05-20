i=0
cara = 0
coroa = 0
while i<9:
    n = int(input())

    if n==1: cara+=1
    else: coroa +=1

    i+=1

if cara>coroa:
    print("Cara")

else:
    print( "Coroa")