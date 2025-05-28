def ppt(j1, j2):
    if j1 == j2:
        return 0
    
    if (j1==1 and j2==2) or (j1==2 and j2==3) or (j1==3 and j2==1):
        return 1

    return 2

j1 = int(input())
j2 = int(input())
print(ppt(j1,j2))