txt = input()
txt = txt.replace(",", "").replace(".", "").replace(":", "").replace(";", "").replace("!", "").replace("?", "")

txt2 = txt.split()

for x in txt2:
    if(len(x)>3):
        print(f"{x} {txt2.count(x)}")