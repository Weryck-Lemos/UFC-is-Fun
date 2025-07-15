def contador(l):
    a=0
    l=0
    u=0
    for x in text:
        if x.isalpha():
            a += 1
            if x.islower():
                l += 1
            if x.isupper():
                u += 1
    return a,l,u
text = input()
a,l,u = contador(text)
print(f"O texto possui {len(text)} caracteres, sendo {a} letras, com {l} minúsculas e {u} maiúsculas.")