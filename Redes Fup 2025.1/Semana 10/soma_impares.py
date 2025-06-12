def par(n):
    return n%2==0

def soma(i, j):
    ans = 0

    for x in range(i,j+1):
        if(not par(x)):
            ans+=x
    return ans

i=int(input())
j=int(input())
print(soma(i,j))