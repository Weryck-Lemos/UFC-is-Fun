i = 0
j = int(input())
ans = 0

while i<j:
    num = int(input())
    ans+=num
    i+=1

print(f"{ans/j:.2f}")