dict = {
    1: "apple",
    "orange": [2, 3, 4],
    True: False,
    None: 0
}

print(dict.get(1))
print(dict.get(7))
print(dict.get(None))
print(dict.get(12345, "not in dict"))
