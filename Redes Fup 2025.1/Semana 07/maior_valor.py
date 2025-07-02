n = int(input())
i = 0
maior = 0

while i <n:
    num = int(input())
    if i==0: maior = num
    maior = max(num, maior)
    i+=1

print(maior)