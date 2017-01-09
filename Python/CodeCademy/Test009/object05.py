from itertools import count as cnt


def count(start, stop, step=1):
    start, stop = (start, stop) if start < stop else (stop, start)
    for i in cnt(start, step):
        yield i
        if i >= stop:
            break

mylist = list(count(1, 10))
mytuple = tuple(count(1, 10))
myset = set(count(1, 10))

print(mylist)
print(mytuple)
print(myset)

cu = lambda y: (x for x in range(y, -1))

for i in cu(10):
    print(i, end=", ")
    if i > 20:
        break

f = open("ggg.txt", "a")

try:
    pass
except FileNotFoundError:
    pass
else:
    pass
finally:
    pass
