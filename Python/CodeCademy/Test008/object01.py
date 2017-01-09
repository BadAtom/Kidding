file = open("file.txt", "w")
file.write("Hello ")
file.write("it's me\n")
file.write("hehehe")
file.close()

try:
    f = open("filename.txt")
    print(f.read())
except FileNotFoundError:
    print("No such file")
    f = open(__file__)
finally:
    f.close()

with open("filename.txt") as f:
    print(f.read())
