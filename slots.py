import sys

class Person:
    __slots__ = ["name", "age"]

    def __init__(self, name, age):
        self.name = name
        self.age = age

class NormalPerson:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p = Person("Sujan", 21)
n = NormalPerson("Sujan", 21)

print("Person Memory:", sys.getsizeof(p))
print("Normal Person Memory:", sys.getsizeof(n))

p.address = "Kathmandu"
