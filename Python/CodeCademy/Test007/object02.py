# Простой калькулятор
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
        return False


def get_float(text):
    temp = input(text.capitalize() + ": ")
    if temp.lower() == "выход":
        exit()
    try:
        return float(temp)
    except:
        return temp


def output(text):
    print(text)
