import logging
from functions import add, sub, mul, div

def input_numbers():
    x = float(input("Enter first number: "))
    y = float(input("Enter second number: "))
    return x, y

def do_operation():
    print("Choose operation: +  -  *  /")
    op = input("Enter operation: ")

    a, b = input_numbers()

    if op == "+":
        result = add(a, b)
    elif op == "-":
        result = sub(a, b)
    elif op == "*":
        result = mul(a, b)
    elif op == "/":
        result = div(a, b)
    else:
        print("Wrong operation")
        return

    print("Result:", result)

    logging.info(f"a={a}, b={b}, op='{op}', result={result}")
