n = int(input())
l = []

for _ in range(n):
    x = int(input())
    l.append(x)
    
print(f"O menor valor e {min(l)}, o maior {max(l)} e a soma da lista e {sum(l)}.")
