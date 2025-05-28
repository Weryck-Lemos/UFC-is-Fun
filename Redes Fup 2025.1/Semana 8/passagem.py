def viagem(n):
    ans = 5

    if n<=30:
        return (ans+n*0.5)
    
    else:
        return (ans+n*0.45)
    
dist = float(input())
print(f"{viagem(dist):.2f}")