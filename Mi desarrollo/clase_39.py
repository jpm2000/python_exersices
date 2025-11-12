# Uso de los docstrings """" para comentar el código, con el fin de informar lo que hace el código


def calculate_average(numbers):
    """
    Calcula el promedio de una lista de números.

    Parámetros:
    numbers (list): una lista de numeros enteros o flotantes

    Retorna:
    float: el promedio de los numeros en la lista
    """
    return sum(numbers) / len(numbers)


print(calculate_average([1, 2, 3, 4, 5, 6]))
