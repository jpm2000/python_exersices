import math


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def mult(a, b):
    return a * b


def div(a, b):
    if b == 0:
        raise ValueError("El denominador no puede ser 0")
    return a / b


if __name__ == "__main__":
    print("operaciones")
    res1 = add(1, 2)
    print(f"Suma: {res1}")
    res2 = subtract(10, 2)
    print(f"Resta: {res2}")
