# your code goes here
s = input()
s = int(s)
for test in range(s):
    p = input()
    p = int(p)
    boys = []
    for boy in range(p):
        temp = input()
        temp = temp.split(" ")
        boys.append((int(temp[0]), temp[1]))

    z = input()
    z = int(z)
    closed_mro = {}
    for mro in range(z):
        temp = input()
        temp = temp.split(" ")
        closed_mro[temp[0]] = temp[1]

    p = input()
    p = int(p)
    recruits = []
    for recruit in range(p):
        temp = input()
        temp = int(temp)
        recruits.append(temp)

    for boy in boys:
        if boy[0] in recruits:
            a = boy[0]
            b = boy[1]
            if b in closed_mro.keys():
                for cls_mro, new_mro in closed_mro.items():
                    if b == cls_mro:
                        b = new_mro

            print(a, b)
    print()
