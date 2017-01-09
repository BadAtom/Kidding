from math import fsum
answers = []

for i in range(int(input())):
    dimension = int(input())
    if dimension % 2 == 0:
        answers.append(dimension * dimension - int(fsum([i for i in range(1, int(dimension / 2 + 2))])))
    else:
        answers.append(dimension * dimension - int(fsum([i for i in range(1, int((dimension - 1) / 2) + 1)])) - (int(dimension / 2 + 0.5) + dimension) + 1)

for answer in answers:
    print("{} {}".format("DWON", answer))
