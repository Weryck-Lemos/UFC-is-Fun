def par(n):
    return n%2==0

def soma(i, j):
    ans = 0

    while i<=j:
        if(not par(i)):
            ans+=i
        i+=1
    return ans

i=int(input())
j=int(input())
print(soma(i,j))