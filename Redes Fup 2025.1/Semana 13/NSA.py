text = input()
find = input()

text = text.lower()
find = find.lower()

j=0

for i in text:
    if i == find[j]:
        j+=1
    if j== len(find):
        break

if(j==len(find)):
    print("Sim")

else:
    print("Nao")