import math
def dist(x1,y1, x2,y2):
    return math.sqrt( (x2-x1)**2  + (y2-y1)**2)

x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())

ans = dist(x1,y1,x2,y2)
print(f"As coordenadas dos pontos são ({x1:.2f},{y1:.2f}) e ({x2:.2f},{y2:.2f}) e sua distancia e: {ans:.2f}.")