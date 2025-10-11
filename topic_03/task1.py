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

def calculator(a, b, op):
    if op == "+":
        return add(a, b)
    elif op == "-":
        return subtract(a, b)
    elif op == "*":
        return multiply(a, b)
    elif op == "/":
        return divide(a, b)
    else:
        return "Невідома операція"

def main():
    while True:
        command = input("Введіть 'exit' для завершення або Enter для продовження: ")
        if command == "exit":
            print("Завершення роботи калькулятора.")
            break
        try:
            a = float(input("Введіть перше число: "))
            b = float(input("Введіть друге число: "))
            op = input("Введіть операцію (+, -, *, /): ")
            print("Результат:", calculator(a, b, op))
        except ValueError:
            print("Введено некоректне число!")

main()
