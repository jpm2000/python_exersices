class LivingBeing:
    def __init__(self, name):
        self.name = name


class Person(LivingBeing):
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age


class Student(Person):
    def __init__(self, name, age, id):
        super().__init__(name, age)
        self.id = id

    def greet(self):
        print(
            f"Hi my name is {self.name}, I'm {self.age} years old, and my student ID is {self.id}"
        )


student = Student("JP", 25, 1000000)
student.greet()
