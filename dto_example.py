points_x = [0, 2, 3, 4]
points_Y = [5, 7, 3, 10]

person_names = ['andrzej', 'rafal']
person_last_names = ['duda', 'slaby']


class Person:
    def __init__(self, name, last_name):
        self.name = name
        self.last_name = last_name


people = [Person('andrzej', 'duda'), Person('rafal', 'slaby')]

wszyscy_slabi = []
for person in people:
    if person.last_name == 'slaby':
        wszyscy_slabi.append(person)

wszyscy_slabi = [person for person in people if person.last_name == 'slaby']


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


points = [Point(0, 5), Point(2, 7)]
