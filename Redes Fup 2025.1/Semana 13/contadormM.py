text = input()

a=0
l =0
u=0

for x in text:
    if x.isalpha():
        a+=1
        if x.islower():
            l+=1
        if x.isupper():
            u+=1

print(f"O texto possui {len(text)} caracteres, sendo {a} letras, com {l} minúsculas e {u} maiúsculas.")    