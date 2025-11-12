def local_func():
    x = 10  # variable local
    print(f"el valor de la variable es {x}")


local_func()

# Si intento imprimir la variale "x" me va a dar un error de identación
"""
print(x)
"""

# Crear la variable global
x = 100


def show_global():
    print(f"El valor de la variable global es {x}")


show_global()
print(x)
