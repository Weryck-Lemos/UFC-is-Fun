n = int(input())
l1 = []
i = 0

while i<n:
    x = int(input())
    l1.append(x)
    i+=1


m = int(input())
l2 = []
i = 0

while i<m:
    x = int(input())
    l2.append(x)
    i+=1


ans = []
k = m+n
i=0

while i<k:
    if i<n:
        ans.append(l1[i])
    
    else:
        ans.append(l2[i-n])

    print(ans[i])
    i+=1