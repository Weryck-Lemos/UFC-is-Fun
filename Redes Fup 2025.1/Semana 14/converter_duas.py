L1 = [x for x in input().split()]
L2 = [x for x in input().split()]

dic = {L1[i]: L2[i] for i in range(len(L2))}
for c,v in sorted(dic.items()):
    print(f"{c}: {v}")