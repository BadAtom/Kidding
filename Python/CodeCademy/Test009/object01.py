class Person:
    def __init__(self, name):
        self.name = name

    def GetInfo(self):
        return self.name


class Student(Person):
    def __init__(self, name, studyplace):
        super().__init__(name)
        self.sudyplace = studyplace

    def GetInfo(self):
        print(super().GetInfo(), self.sudyplace)

    def print_name(self):
        print(self.name)


class Worker(Person):
    def __init__(self, name, workplace):
        super().__init__(name)
        self.workplace = workplace

    def GetInfo(self):
        print(super().GetInfo(), self.workplace)


class Academy:
    peoples = []

    def add_person(self, person):
        self.peoples.append(person)

    def show_all(self):
        for i in self.peoples:
            i.GetInfo()

academy = Academy()
student = Student("Vanya", "Tech house of USA")
worker = Worker("Oleksei", "Some really bad place")
academy.add_person(student)
academy.add_person(worker)
academy.show_all()
student.passport_code = 788125
print(student.__class__.__name__)

class aStudent(student):
    def __init__(self, name, studyplace, some, wow):
        super().__init__(name, studyplace)

new_student = aStudent("", "")
print(student.passport_code)
print(new_student.passport_code)
