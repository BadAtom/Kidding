def count(sequence, item):
    return sequence.count(item)

def median(li):
    myli = sorted(li)
    print(myli)
    if len(myli) % 2 == 0:
        a = myli[int(len(myli) / 2) - 1]
        b = myli[int(len(myli) / 2)]
        return (a + b) / 2.0
    else:
        return myli[int(len(myli) / 2)]

dic = {
    1: "Hello",
    "2": 666,
    'hi': False,
    None: "WATA"
}

# from random import randint as rnd
# sudoku = [[rnd(1, 9) for i in range(9)] for i in range(9)]
# for line in sudoku:
#     for number in line:
#         print(number, end="\t")
#     print()

# a = help(print)
# print(a)

class Person:
    myname, myage = "", 0

    def __init__(self, name, age):
        myname = name
        myage = age
    print(myname, myage)


pe = Person("Kirill", 25)