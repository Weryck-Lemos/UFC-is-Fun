text = input()
text2="".join([i for i in text if i.isalpha() or i==" "])

list = text2.split()
tam = 0

for i in list:
    if len(i)>tam:
        ans =i
        tam=len(i)

print(f"A palavra de maior tamanho é a {ans}")