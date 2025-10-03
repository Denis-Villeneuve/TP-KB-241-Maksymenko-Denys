def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Ділення на нуль неможливе"

def calculator_match(a, b, op):
    match op:
        case "+":
            return add(a, b)
        case "-":
            return subtract(a, b)
        case "*":
            return multiply(a, b)
        case "/":
            return divide(a, b)
        case _:
            return "Невідома операція"

a = float(input("Введіть перше число: "))
b = float(input("Введіть друге число: "))
op = input("Введіть операцію (+, -, *, /): ")

print("Результат:", calculator_match(a, b, op))
