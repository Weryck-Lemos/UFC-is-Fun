def func(sub, texto):
    for i in sub:
        if i.isalpha():
            if i not in texto:
                return False
    
    return True

sub = input().lower()
txt = input().lower()

if func(sub,txt):
    print("Sim")

else:
    print("Nao")