def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    try:
        return x / y
    except ZeroDivisionError:
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

def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Будь ласка, введіть число!")

def main():
    print("Калькулятор. Введіть 'exit' для завершення.")
    while True:
        command = input("Натисніть Enter для продовження або введіть 'exit': ")
        if command.lower() == "exit":
            print("Завершення роботи калькулятора.")
            break
        a = get_number("Введіть перше число: ")
        b = get_number("Введіть друге число: ")
        op = input("Введіть операцію (+, -, *, /): ")
        result = calculator(a, b, op)
        print("Результат:", result)

main()
