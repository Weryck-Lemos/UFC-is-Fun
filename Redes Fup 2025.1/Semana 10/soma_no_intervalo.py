def soma(i, j):
    ans = 0

    for x in range(i,j+1):
        ans+=x
    return ans

i=int(input())
j=int(input())
print(soma(i,j))