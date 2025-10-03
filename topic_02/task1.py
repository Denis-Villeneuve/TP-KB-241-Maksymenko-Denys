import math

def discriminant(a, b, c):
    return b**2 - 4*a*c

def quadrat(a, b, c):
    d = discriminant(a, b, c)
    if d > 0:
        x1 = (-b + math.sqrt(d)) / (2*a)
        x2 = (-b - math.sqrt(d)) / (2*a)
        return f"Два корені: x1 = {x1}, x2 = {x2}"
    elif d == 0:
        x = -b / (2*a)
        return f"Один корінь: x = {x}"
    else:
        return "Коренів немає (дискримінант < 0)"

a = float(input("Введіть a: "))
b = float(input("Введіть b: "))
c = float(input("Введіть c: "))

print(quadrat(a, b, c))
