class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __repr__(self):
        # Este es un nuevo vector del vector anterior
        return f"Vector({self.x}, {self.y})"


variable1 = Vector(1000, 12000)
variable2 = Vector(2000, 500)
variable3 = variable1 + variable2

# Se hace la suma pero solo necesito una linea de código para ejecutar la suma dentro de un vector. En vez de tener que ejecutarlo dos veces
print("Vector")
print(variable3)
print("")


class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def __eq__(self, otra) -> bool:
        return self.nombre == otra.nombre and self.edad == otra.edad

    def __lt__(self, otra) -> bool:
        return self.edad < otra.edad


p1 = Persona("JP", 25)
p2 = Persona("Jose", 21)
p3 = Persona("Gaby", 19)
p4 = Persona("Gaby", 19)

print("Persona iguales")
print(p1 == p2)
print(p2 == p3)
print(p1 == p3)
print(p3 == p4)
print("")

print("Persona menor")
print(p1 < p2)
print(p2 < p1)
print(p2 < p3)
print(p3 < p4)
print("")

print("Ejercicio de la clase")

from math import gcd


class Fraccion:
    def __init__(self, num, dem):
        self.num = num
        self.dem = dem

    def __add__(self, otra):
        nuevo_num = self.num * otra.dem + otra.num * self.dem
        nuevo_dem = self.dem * otra.dem
        comun_divisor = gcd(nuevo_num, nuevo_dem)
        return Fraccion(nuevo_num // comun_divisor, nuevo_dem // comun_divisor)

    def __repr__(self):
        return f"{self.num}/{self.dem}"


f1 = Fraccion(1, 2)
f2 = Fraccion(3, 8)
f3 = f1 + f2

print(f3)
