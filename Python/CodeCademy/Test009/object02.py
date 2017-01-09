class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def print_all(self):
        print(self.name, self.age, sep=" : ")

person = Person("David", 25)
person.passport_code = 123456


class Another_Person(person):
    def __init__(self, name, age):
        super().__init__(name, age)

another_person = Another_Person("Angelina", 18)
person.print_all()
another_person.print_all()
