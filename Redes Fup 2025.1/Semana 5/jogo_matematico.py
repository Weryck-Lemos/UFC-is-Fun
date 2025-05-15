n1 = int(input())
n2 = int(input())
n3 = int(input())
m1 = int(input())
m2 = int(input())
m3 = int(input())
pivo = int(input())

j1=0 
j2=0
if pivo%2==0:
    if(n1%2==0): j1+=n1
    else: j1-=n1

    if(n2%2==0): j1+=n2
    else: j1-=n2

    if(n3%2==0): j1+=n3
    else: j1-=n3

    if(m1%2==0): j2+=m1
    else: j2-=m1

    if(m2%2==0): j2+=m2
    else: j2-=m2

    if(m3%2==0): j2+=m3
    else: j2-=m3

else:
    if(n1%2==1): j1+=n1
    else: j1-=n1

    if(n2%2==1): j1+=n2
    else: j1-=n2

    if(n3%2==1): j1+=n3
    else: j1-=n3

    if(m1%2==1): j2+=m1
    else: j2-=m1

    if(m2%2==1): j2+=m2
    else: j2-=m2

    if(m3%2==1): j2+=m3
    else: j2-=m3


if j1>j2:
    print(f"Jogador1 {j1}")

elif j1<j2:
    print(f"Jogador2 {j2}")

else:
    print("Empate")