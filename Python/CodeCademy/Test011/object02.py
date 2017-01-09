def make_mass(x):
    result = [[j * 0 for j in range(x)] for mass in range(x)]

    for i in range(x):
        result[i][i] = i + 1

    i = x - 1
    j = 0
    while j < x:
        result[i][j] = x + j + 1
        j += 1
        i -= 1

    temp = result[0][x - 1]
    backrow, frontcolumn, lowrow, backcolumn = (0, 0, x - 1, x - 1)
    myrange = int(x / 2)

    for i in range(myrange):
        for numb in result[backrow][::-1]:
            if numb == 0:
                numb = temp
                temp += 1

    return result


def print_mass(mass):
    for line in mass:
        print(line)

mass1 = make_mass(5)
print_mass(mass1)
