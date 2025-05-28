def triangulo(l1,l2,l3):
    if l1+l2 >= l3 and l1+l3>=l2 and l2+l3>=l1:
        return True
    
    else:
        return False
    
l1 = int(input())
l2 = int(input())
l3 = int(input())
if(triangulo(l1,l2,l3)):
    print("SIM")

else:
    print("NAO")