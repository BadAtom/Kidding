class Animal:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def talk(self, animal, told):
        print(animal.__class__.__name__, "say:", told)

    def info(self, animal):
        print("I'm a ", animal.__class__.__name__.lower(), ". ", "My name is ", self.name, ". My color is ", self.color, ".", sep="")


class Cat(Animal):
    def talk(self):
        super().talk(self, "MEOW!")

    def info(self):
        super().info(self)


class Dog(Animal):
    def talk(self):
        super().talk(self, "WOOF!")

    def info(self):
        super().info(self)

cat1 = Cat("Vincent", "black")
dog1 = Dog("Thunder", "white")
cat1.talk()
dog1.talk()
cat1.info()
dog1.info()


class Dog(dog1.__class__):
    def __init__(self, name, color):
        super().__init__(name, color)
        self.tricks = []


class Cat(cat1.__class__):
    def __init__(self, name, color, mice_caught=0):
        super().__init__(name, color)
        self.mice_caught = mice_caught

cat2 = Cat("", "", 40)
print(cat2.mice_caught)


def printer(*args, separator=" "):
    for arg in args:
        print(arg, end=separator)
    print()

printer(1.2, 8, 14, "hello", True, None)
printer(1.2, 8, 14, "hello", True, None, 99, "Mike", separator=", ")
some_list = ["Hi", 44, 2.2, False]
printer(some_list, separator="..")

dog2 = Dog("Kolya", "pitch")
print(dog2.tricks)
dog3 = Dog("Mitya", "cronch")
print(dog2.tricks)
dog2.tricks.append("bark")
dog4 = Dog("Holy", "dirty blue")
print(dog4.tricks)
print(dog2.tricks)
