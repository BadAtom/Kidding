operation = {}
operation['+'] = operation['add'] = lambda a, b: a + b
operation['-'] = operation['subtract'] = lambda a, b: a - b
operation['*'] = operation['multiply'] = lambda a, b: a * b
operation['/'] = operation['divide'] = lambda a, b: a / b

def get_input(text):
    temp = input(text.capitalize() + ": ").lower()
    if temp == "exit" or temp == "quit":
        exit()
    try:
        return float(temp)
    except:
        return str(temp)

def get_float(text):
    result = get_input(text)
    while type(result) != float:
        print("Data is invalid.")
        result = get_input("input integer or float")
    return result

def get_operation(text):
    result = get_input(text)
    ops = ['add(+)', 'subtract(-)', 'multiply(*)', 'divide(/)']
    while result not in operation:
        print("Data is invalid.")
        print("Valid operations: [" + "] [".join(ops) + "].")
        result = get_input("choose valid operation")
    return result

def calc():
    print("Answer:", operation[get_operation("choose operation")](get_float("first number"), get_float("second number")))
    print()

while True:
    calc()
