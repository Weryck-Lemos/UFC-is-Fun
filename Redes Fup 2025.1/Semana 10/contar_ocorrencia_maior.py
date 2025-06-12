n = int(input())
nums=[int(input()) for i in range(n)]
maior = nums[0]

ans=0
for x in nums:
    if x>maior:
        maior = x
        ans=0

    if x==maior:
        ans +=1
    


print(f"({ans},{maior})")

