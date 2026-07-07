"""
Crea un nuevo script de gestión de empleados con dos funciones: una para agregar empleados y otra para eliminarlos.
Usa la estructura if __name__ == "__main__" para invocarlas y comparte en los comentarios cómo organizaste tu código.
"""

employees = []


# Agregar empleados
def add_employee(name, age, dept):
    employees.append({"name": name, "age": age, "dept": dept})
    return f"Empleado {name}, tiene {age} años, entra al departamento de {dept}"


# Eliminar empleados
def delete_employee(name, age, dept):
    employees.remove({"name": name, "age": age, "dept": dept})
    return f"Empleado {name} ha salido de la empresa"


if __name__ == "__main__":
    print("Empleados actualizados al hoy:")
    print(add_employee("JP", 25, "CEO más crack dek mundo"))
    print(add_employee("Alejo", 60, "Crack en ventas"))
    print(add_employee("Jose", 22, "Maquina operativa"))
    print(add_employee("Ali", 40, "Pilera electrica"))
    print(f"Los empleados de la empresa bluberri hoy son {employees}")
    print("")
    print("Un año depues...")
    print(delete_employee("Jose", 22, "Maquina operativa"))
    print(f"Los empleados de la empresa bluberri hoy son {employees}")
