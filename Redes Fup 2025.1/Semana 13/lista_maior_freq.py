txt = input()
n = 0
l = ""

for x in txt:
    if x.isalpha():
        if txt.count(x)>n:
            n = txt.count(x)
            l = x

if l.isupper():
    ans ="maiúscula"
else:
    ans = "minúscula"

print(f"A letra de maior frequência foi a letra {l} {ans} que ocorre {n} vezes.")