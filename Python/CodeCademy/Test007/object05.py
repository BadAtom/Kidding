from math import sqrt as sqr


def mult(a, b):
    return a * b


def multifun(func, *args):
    if len(args) == 1:
        return func(args[0])
    else:
        return func(args[0], args[1])

print(multifun(sqr, 25))
print(multifun(mult, 10, 10))
