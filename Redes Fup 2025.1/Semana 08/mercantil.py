def mercantil(j1,price, chute):
    ans = price-j1
    if (j1<price and chute == "maior") or (j1>price and chute=="menor"):
        return "primeiro"
    
    else:
        return "segundo"
    

j1  = float(input())
price = float(input())
chute = input()
print(mercantil(j1, price, chute))