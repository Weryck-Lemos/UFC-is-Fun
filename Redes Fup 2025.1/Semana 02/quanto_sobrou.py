q1 = float(input())
q2 = float(input())
q3 = float(input())

p1 = float(input())
p2 = float(input())
p3 = float(input())

qp = float(input())

tot = (q1 *p1) + (q2*p2) + (q3*p3)
ans = qp - tot

print(f"Lista de compras")
print(f"Subtotal 1: R$ {q1*p1:.2f}")
print(f"Subtotal 2: R$ {q2*p2:.2f}")
print(f"Subtotal 3: R$ {q3*p3:.2f}")
print(f"Total: R$ {tot:.2f}")
print(f"Troco: R$ {ans:.2f}")