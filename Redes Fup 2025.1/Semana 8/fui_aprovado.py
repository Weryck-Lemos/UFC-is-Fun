def maior(a,b,c):
    if a>=b and a>=c:
        return a
    
    if b>=a and b>=c:
        return b
    
    return c

def menor(a,b,c):
    if a<=b and a<=c:
        return a
    
    if b<=a and b<=c:
        return b
    
    return c

def aprov(n1,n2,n3):
    media = (n1+n2+n3)/3
    if  media>=7:
        return True
    
    if media>5 and n3>=7:
        return True
    
    if maior(n1,n2,n3)- menor(n1,n2,n3) <=3:
        return True
    
    return False

n1 = float(input())
n2 = float(input())
n3 = float(input())
if(aprov(n1,n2,n3)):
    print("Aprovado")

else:
    print("Reprovado")