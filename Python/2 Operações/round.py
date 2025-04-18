import math

op = input()
n = int(input())

if op == 'c': print(math.ceil(n))
elif op == 'f': print(math.floor(n))
else: print(round(n))