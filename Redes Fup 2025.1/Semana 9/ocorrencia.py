n = int(input())
nums = []
i = 0
maior =0
menor = 0

while i<n:
    x = int(input())
    nums.append(x)
    if i==0:
        maior =nums[0]
        menor =nums[0]

    if nums[i]>maior:
        maior = nums[i]

    if nums[i]<menor:
        menor = nums[i]
    
    i+=1

i=0
q_maior=0
q_menor=0
while i<n:
    if nums[i]==maior:
        q_maior+=1

    if nums[i]==menor:
        q_menor+=1
    i+=1

print(f"({q_menor},{menor}) ({q_maior},{maior})")

