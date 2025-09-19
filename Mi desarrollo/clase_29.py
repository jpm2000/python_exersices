class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name}, {self.age} años"

    def __repr__(self):
        return f"Person(name={self.name}, age={self.age})"


person1 = Person("Alice", 30)
person2 = Person("JP", 25)

# Uso str
print(person1)

# Uso repr
print(repr(person1))
