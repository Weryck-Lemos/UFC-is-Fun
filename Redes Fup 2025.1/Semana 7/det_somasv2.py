i = 1
par = 0
impar = 0

j= int(input())

while i<=j:
    num = int(input())
    if i%2:
        impar+=num
    else:
        par+=num
    i+=1

print(f"{par} {impar}")