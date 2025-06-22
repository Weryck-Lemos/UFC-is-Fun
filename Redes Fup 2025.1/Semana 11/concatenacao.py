txt1 = input()
txt2 = input()

if len(txt1) < len(txt2):
    if txt1[len(txt1)-1] != " ":
        txt3 = txt1 + " " + txt2
    else:
        txt3 = txt1 +txt2

else:
    if txt2[len(txt2)-1] != " ":
        txt3 = txt2 + " " + txt1
    else:
        txt3 = txt2 + txt1

print(txt3)
