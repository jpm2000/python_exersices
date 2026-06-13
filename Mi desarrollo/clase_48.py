class Persona:
    def __init__(self, nombre: str, edad: int) -> None:
        self.nombre = nombre
        self.edad = edad

    # metodo magico para un string. Definir como se presenta un objeto convertido a cadena y cuando lo imprimimo
    def __str__(self) -> str:
        """
        Devuleve un string de la persona, para que el usurio lo pueda comprender
        """
        return f"Persona:{self.nombre}, {self.edad} años"

    # Representación oficial o detallada del objeto
    def __repr__(self) -> str:
        """
        Obejto tipo persona tiene un nombre y una edad
        """
        return f"Persona(nombre = '{self.nombre}', edad = {self.edad}"

    # Comparación de un objeto usando el signo de igualdad
    def __eq__(self, otra_persona) -> bool:
        """
        Compara si dos objetos son iguales en función del nombres y su edad
        """
        return self.nombre == otra_persona.nombre and self.edad == otra_persona.edad

    # Comparar que un atributo sea menor al otro
    def __lt__(self, otra_persona) -> bool:
        """
        Comparar si un atributo es menor al otro, usando solo la edad como punto de comparación
        """
        return self.edad < otra_persona.edad

    # Metodo de sumatoria en base a la edad, del primero con el segundo
    def __add__(self, otra_persona):
        # Se suma la edad de las dos personas
        return self.edad + otra_persona.edad


# Crear las instancias
p1 = Persona("JP", 26)
p2 = Persona("JP", 26)
p3 = Persona("Pablo", 25)

# __str__
# print(p1)

# __repr__ especifica todos los atributos el objeto
# print(repr(p1))

# __eq__ comparación de los objetos
# print(p1 == p3)
# print(p1 == p2)

# __lt__ comparación de si un atributo es menor al otro en base a la edad de la persona
# print(p1 < p3)
# print(p3 < p2)

# __ad__ es la suma de las dos edades de las personas
print(p1 + p3)
print(p3 + p2)
