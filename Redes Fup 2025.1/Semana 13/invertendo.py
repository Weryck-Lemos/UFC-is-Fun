text = input()
l = text.split()
l=l[::-1]

ans=""
for i in range(len(l)):
    ans+=l[i]

    if(i!=len(l)-1):
        ans+=" "
    

print(ans)