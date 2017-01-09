
def factorial(x):
    if x == 1:
        return 1
    elif x < 0:
        return 0
    else:
        return x * factorial(x-1)

save = [0, 1]
def fibonachchi_generator(count):
    for i in range(count):
        temp = save[1]
        yield save[0]
        save[1] += save[0]
        save[0] = temp
