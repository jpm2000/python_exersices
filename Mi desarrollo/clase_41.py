# Se pueden poner luego de los doble puntos el tipo de dato que se tiene para esa variable

id1: int = 101
id2: int = 102
id3: int = 103

total_id: int = id1 + id2 + id3

# Print con el resultado
print(total_id)

print("")


# Ahora, esta aclaración del tipo de dato tambien aplica a funcones, listas y de más
def add_id(id1: int, id2: int, id3: int) -> int:
    return id1 + id2 + id3


print(add_id(111, 222, 333))

print("")

# Ahora esto puede ayudar a específicar clases


class Empleados:
    "atributos con el tipo de datos"

    name: str
    age: int
    salary: float

    def __init__(self, name: str, age: int, salary: float):
        self.name = name
        self.age = age
        self.salary = salary

    def intro(self) -> str:
        return f"Hola me llamo {self.name}, tengo {self.age} años y me van a pagar {self.salary}"


empleado_1 = Empleados("Juan", 25, 1000000)
print(empleado_1.intro())

"""
Se puede correr "mypy nombre.py" para verificar si hay errores en el documento
"""

# Prueba de optional

from typing import Optional
from typing import Union


# Dando el Optional, podemos decir que el resultado puede ser int o un None
def find_employees(employee_ids: list[int], employee_id: int) -> Optional[int]:
    if employee_id in employee_ids:
        employee_id
    return None


def process_salary(salary: Union[int, float]) -> float:
    return float(salary)
