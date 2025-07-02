i = 1
ans=0

while i<=33:
    num = int(input())
    if i%2:
        ans += num/(i+3)
    else:
        ans+= num/(i+2)
    i+=1

print(ans)