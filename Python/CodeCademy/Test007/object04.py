def calc(a, b, operation):
    operations = {
        "+": a + b,
        "-": a - b,
        "*": a * b,
        "/": a / b
    }

    if operation in operations:
        return operations[operation]
    else:
        return "error"


def get_input(text):
    temp = input(text.capitalize() + ": ")
    if temp.lower() == "exit":
        exit()
    try:
        return float(temp)
    except:
        return temp


def get_float(text):
    result = get_input(text)
    while type(result) != float:
        print("Data is invalid.")
        result = get_input("input integer or float")
    return result


def get_operation(text):
    result = get_input(text)
    operations = ['/', '*', '-', '+']
    while result not in operations:
        print("Data is invalid.")
        result = get_input("choose valid operation (/ * + -)")
    return result

print("It's a simple calc. Type exit for exit.")

while True:
    a = get_float("first number")
    b = get_float("second number")
    operation = get_operation("chose the operation")

    try:
        print(calc(a, b, operation))
    except ZeroDivisionError:
        print("inf.")

    print("")
