n = [3, 5, 7]


def total(numbers):
    if not numbers: return

    result = 0
    for a in numbers:
        if type(a) == type(1) or type(a) == type(1.1):
            result += a
        else:
            print('[{0}] not a number!'.format(str(a)))
    return result


m = ['hemma', 5, 1.5, "I'M A COLDWORLD", True]
o = [1, 2]
m.append(o)
print(total(m))
print(total(n))
