# Clase
class Person:
    # Constructor: con que inicia
    def __init__(self, name, age):
        # Atributos
        self.name = name
        self.age = age

    # Método
    def greet(self):
        print("Hello! I'm a person")


class Student(Person):
    def __init__(self, name, age, student_id):
        # Del super se llama el constructor y los atributos que se usan
        super().__init__(name, age)
        # Solo le pertenece a los estudiantes
        self.student_id = student_id

    def greet(self):
        super().greet()
        print(f"Hello my student ID is {self.student_id}")


student = Student("Ana", 23, 123)
student.greet()

print("")
print(20 * "-")
print("Seres vivos")


class LivingBeing:
    def __init__(self, nombre):
        self.nombre = nombre

    def soy(self):
        print(f"Soy un humano y mi nombre es {self.nombre}")


class Persona(LivingBeing):
    def __init__(self, nombre, edad):
        super().__init__(nombre)
        self.edad = edad

    def saludos(self):
        print(f"Hola mi nombre es {self.nombre} y tengo {self.edad}")


class MenorEdad(Persona):
    def __init__(self, nombre, edad, id):
        super().__init__(nombre, edad)
        self.id = id

    def mi_id(self):
        print(
            f"Hola mi nombre es {self.nombre}, tengo {self.edad} y soy menor de edad y mi documento de identidad es {self.id}"
        )


minor = MenorEdad("JP", 17, 10000000)
minor.mi_id()
