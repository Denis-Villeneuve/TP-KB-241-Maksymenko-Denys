import math

a, b, c = 1, -3, 2
d = b**2 - 4*a*c

if d < 0:
    print("No real roots")
elif d == 0:
    print(-b / (2*a))
else:
    x1 = (-b + math.sqrt(d)) / (2*a)
    x2 = (-b - math.sqrt(d)) / (2*a)
    print(x1, x2)
