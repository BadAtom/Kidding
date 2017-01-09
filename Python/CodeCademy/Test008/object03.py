words = ("spam", "drum", "scum")

dic = {
    words[0]: 1488,
    words[1]: "'n' base",
    words[2]: "DIE TRAITOR"
}

print(dic.get(words[2]) + " " + words[2].upper() + "!!!")

a = {1, 2, 3, 4, 5}
b = {3, 4, 6, 7}

print("a & b")
print(a & b)
print("a - b")
print(a - b)
print("a | b")
print(a | b)

li = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(li[:3:-1])
