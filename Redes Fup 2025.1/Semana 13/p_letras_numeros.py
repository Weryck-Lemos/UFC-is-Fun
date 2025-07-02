def haveNum(texto):
    for x in texto:
        if x.isdigit():
            return True
    return False

def haveWord(texto):
    for x in texto:
        if x.isalpha():
            return True
    return False

txt = input()
txt = txt.replace(".", "").replace(",","")
l = txt.split()

ans = [x for x in l if haveNum(x) and haveWord(x) and len(x)>=3]
print(ans)