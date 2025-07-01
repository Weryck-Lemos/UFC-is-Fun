text = input()
l = text.split()

ans =" ".join([i.title() if len(i)>3 else i for i in l])
print(ans)