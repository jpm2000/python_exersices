empleados = [
    {"name": "Juan", "age": 25, "salary": 0},
    {"name": "Pablo", "age": 25, "salary": 1000},
    {"name": "Jimena", "age": 61, "salary": 3000},
    {"name": "Alejandro", "age": 59, "salary": 20000},
    {"name": "Simon", "age": 24, "salary": 10000}
    ]

def cierto_sueldo(empleados):
    """
    Genera una lista de empleados que tienen más de 3000 en salario

    Parametros: una lista con los diccionaios de los empleados

    Retorna: la nueva lista con los salarios filtrados
    """
    x = 3000 # El sueldo minimo
    
    for salary in empleados:
        