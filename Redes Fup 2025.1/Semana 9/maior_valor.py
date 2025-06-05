n = int(input())
nums = []
i = 0
maior =0

while i<n:
    x = int(input())
    nums.append(x)
    if i==0:
        maior =nums[0]
    if nums[i]>maior:
        maior = nums[i]
    i+=1

i=0
ans=0
while i<n:
    if nums[i]==maior:
        ans+=1
    i+=1

print(f"({ans},{maior})")

