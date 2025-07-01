text = input()
ans = 0

for x in text:
    if not(x.isalpha()):
        ans+=1
print(ans)