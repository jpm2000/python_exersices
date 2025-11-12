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


# Imprimiendo el resultado (este es un comentario). Esto da información de una linea de código
print(
    calculate_average([1, 2, 3, 4, 5, 6])
)  # No importa si agregue informacíon aca, igual no se va a ver en el resultado


def calculate_area(base, height):
    """
    Calcula el area de un triangulo.

    Parámetros: variables de la base y la altura

    Retorna: el area del triangulo
    """
    # Multiplicamos la base por la altura --> este comentario se deberia eliminar y dejar solo el docstring
    return (base * height) / 2
