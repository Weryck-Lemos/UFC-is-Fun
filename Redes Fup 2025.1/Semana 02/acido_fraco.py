h = float(input())
ka = float(input())
kw = float(input())
ca = float(input())

ans = (h**3) + ka*(h**2) - (ka*ca+kw)*h - kw*ka
print(f"{ans:.6f}")