dia = int(input())
hora = int(input())

if dia == 1: print("NAO")

elif dia == 7:
    if hora>=8 and hora<=11: print("SIM")
    else: print("NAO")
    
else:
    if (hora>=8 and hora<=11) or (hora>=14 and hora<=17): print("SIM")
    else: print("NAO")