def par(l):
    tam = len(l)
    ans = 0
    for x in l:
        if(x%2==0):
            ans+=1
            
    return ans
    
def impar(l):
    tam = len(l)
    ans = 0
    for x in l:
        if(x%2 !=0):
            ans+=1
            
    return ans


n = int(input())
l = []
i = 0
while i<n:
    x = int(input())
    l.append(x)
    i+=1
    
p = par(l)
i = impar(l)

if i==0:
    print(f"Foram fornecidos {n} números inteiros positivos e todos foram pares.")
    
elif p ==0:
    print(f"Foram fornecidos {n} números inteiros positivos com todos foram impares.")
    
else:
    print(f"Foram fornecidos {n} números inteiros positivos, sendo que {p} foram pares e {i} impares.")

