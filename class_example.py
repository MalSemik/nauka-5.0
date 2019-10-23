class Person:
    def __init__(self, name, surname, cellphone, subject):
        self.name = name
        self.surname = surname
        self.cellphone = cellphone


class Student(Person):
    def __init__(self, name, surname, cellphone, year, subject):
        super().__init__(name, surname, cellphone, subject)
        self.year = year

class Lecturer(Person):
    def __init__(self, name, surname, cellphone, subject):
        super().__init__(name, surname, cellphone, subject)
        self.subject = subject
