import math
x1 = float(input())
y1 = float(input())

x2 = float(input())
y2 = float(input())

ans = math.sqrt( math.pow(x2-x1, 2) + math.pow(y2- y1, 2))
print(f"{ans:.2f}")