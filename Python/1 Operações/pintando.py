import math
a = float(input())
b = float(input())
c = float(input())

p = (a+b+c)/2.0

area = p * ((p-a)) * ((p-b)) * ((p-c))
area = math.sqrt(area)

print(f"{area:.2f}")