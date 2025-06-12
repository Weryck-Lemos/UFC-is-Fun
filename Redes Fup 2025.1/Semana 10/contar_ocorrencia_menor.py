n = int(input())
nums=[int(input()) for i in range(n)]
maior = nums[0]
menor = nums[0]

q_maior=0
q_menor=0
for x in nums:
    if x>maior:
        maior = x
        q_maior = 0

    if x==maior:
        q_maior +=1

    if x<menor:
        menor = x
        q_menor = 0

    if x==menor:
        q_menor +=1
    
print(f"({q_menor},{menor}) ({q_maior},{maior})")