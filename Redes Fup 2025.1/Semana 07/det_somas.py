i = 1
par = 0
impar = 0

while i<=70:
    num = int(input())
    if i%2:
        impar+=num
    else:
        par+=num
    i+=1

print(f"{par} {impar}")