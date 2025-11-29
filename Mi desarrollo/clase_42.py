"""

def divie(a: int, b: int) -> float:
    return a / b

# Type error, se da porque estoy usando diferentes tipos de datos.
print(divie(10, "2"))
"""


def divide(a: int, b: int) -> float:
    # Preguntar si el tipo de dato isinstance(). Validar que ambos parametros sean enteros
    if not isinstance(a, int) or not isinstance(b, int):
        print("Error: ambos paramtros deben ser enteros o flotantes")
        return None

    # Verificar que el divisor no sea 0
    if b == 0:
        print("Error: el divisor no puede ser 0")
        return None

    return a / b


print(divide(10, "2"))

print(divide(10, 0))

print(divide(10, 2))


print("")

# Uso de raise para verificar type error


def divide(a: int, b: int) -> float:
    # Preguntar si el tipo de dato isinstance(). Validar que ambos parametros sean enteros
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError("Ambos parametros deben ser enteros o flotantes")

    # Verificar que el divisor no sea 0
    if b == 0:
        raise ValueError("No se puede dividir por 0")
    return a / b


# print(divide(10, "2"))

# print(divide(10, 0))

print(divide(10, 2))


"""
Me da el siguiente resultado en la terminal:

Traceback (most recent call last):
  File "/Users/juanpablomanrique/Documents/Repositories/python_exersices/Mi desarrollo/clase_42.py", line 48, in <module>
    print(divide(10, "2"))
          ~~~~~~^^^^^^^^^
  File "/Users/juanpablomanrique/Documents/Repositories/python_exersices/Mi desarrollo/clase_42.py", line 40, in divide
    raise TypeError("Ambos parametros deben ser enteros o flotantes")
TypeError: Ambos parametros deben ser enteros o flotantes



Traceback (most recent call last):
  File "/Users/juanpablomanrique/Documents/Repositories/python_exersices/Mi desarrollo/clase_42.py", line 50, in <module>
    print(divide(10, 0))
          ~~~~~~^^^^^^^
  File "/Users/juanpablomanrique/Documents/Repositories/python_exersices/Mi desarrollo/clase_42.py", line 44, in divide
    raise ValueError("No se puede dividir por 0")
ValueError: No se puede dividir por 0
"""

print("")

# Ejemplo de uso con try except

try:
    res = divide(10, "2")  # Esto genero un error tipo Type error
    print(res)
except TypeError as e:
    print(f"Error: {e}")

try:
    res = divide(10, 0)  # Esto genero un error tipo Type error
    print(res)
except ValueError as e:
    print(f"Error: {e}")

try:
    res = divide(10, 2)  # Esto genero un error tipo Type error
    print(res)
except (TypeError, ValueError) as e:
    print(f"Error: {e}")

# Ejercicio de practica deliberada

"""
Enunciado del ejercicio
Crea un programa que:

Pida al usuario que ingrese la edad de una persona.

Valide que:

El valor sea un número entero.

La edad esté entre 0 y 120.

Si el usuario escribe algo que no es número, muestra un mensaje de error y vuelve a pedir la edad.

Si el número está fuera de rango, muestra otro mensaje de error y vuelve a pedir.

Cuando la entrada sea válida, imprime un mensaje de éxito usando un f-string, por ejemplo:
[La edad registrada es 35 años.](pplx://action/translate)
"""

print("")
print("Versión #1 deliberate practice")


def edad_persona(edad: int) -> str:
    # Esta parte no es necesaria cuando tengo ya edad: int. Es redundant
    if not isinstance(edad, int):
        raise TypeError("El valor debe ser un entero")

    if edad > 0 and edad < 120:
        return f"la edad registrada es de {edad}"
    else:
        return f"la edad de {edad} esta por fuera del rango esperado de 0 a 120 años"


try:
    response = edad_persona(121)
    print(response)
except TypeError as r:
    print(f"Error: {r}")


print("")
print("Versión #2 deliberate practice")


def edad_persona_2() -> str:
    while True:
        edad = input("Ingrese la edad")
        try:
            edad_int = int(edad)

            if edad_int > 0 and edad_int < 120:
                return f"la edad registrada es de {edad_int}"
            else:
                print(
                    f"la edad de {edad_int} esta por fuera del rango esperado de 0 a 120 años"
                )

        except ValueError:
            print(f"Error: ingresa un valor correcto diferente de {edad}")


print(edad_persona_2())
