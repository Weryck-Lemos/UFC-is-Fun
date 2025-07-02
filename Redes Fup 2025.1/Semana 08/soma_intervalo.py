def soma(i, j):
    ans = 0

    while i<=j:
        ans+=i
        i+=1
    return ans

i=int(input())
j=int(input())
print(soma(i,j))