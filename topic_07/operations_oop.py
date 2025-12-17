from calc_class import Calculator

calc = Calculator()

def input_numbers():
    x = float(input("Enter first number: "))
    y = float(input("Enter second number: "))
    return x, y

def do_operation():
    print("Choose operation: +  -  *  /")
    op = input("Enter operation: ")
    a, b = input_numbers()

    if op == "+":
        result = calc.add(a, b)
    elif op == "-":
        result = calc.sub(a, b)
    elif op == "*":
        result = calc.mul(a, b)
    elif op == "/":
        result = calc.div(a, b)
    else:
        print("Wrong operation")
        return

    print("Result:", result)
