txt = input()
txt = txt.replace(",", "").replace(".", "").replace(":", "").replace(";", "").replace("!", "").replace("?", "")

l= txt.split()
dic = {l[i]:l.count(l[i]) for i in range(len(l)) if len(l[i])>3}

print(dic)