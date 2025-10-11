def divide(x, y):
    try:
        return x / y
    except ZeroDivisionError:
        return "Ділення на нуль неможливе"
