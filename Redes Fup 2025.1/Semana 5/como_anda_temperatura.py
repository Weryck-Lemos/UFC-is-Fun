j1 = float(input())
value = float(input())
chute = input()

if (j1 == value) or (j1<value and chute=="maior") or (j1>value and chute=="menor"):
    print("primeiro")

else:
    print("segundo")