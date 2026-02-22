# Funciones Lambda

add = lambda a, b: a + b

print(add(10, 4))


multiply = lambda a, b: a * b

print(multiply(10, 4))


# Calcular el cuadrado de cada numero

numbers = range(11)

# map() function in Python is used to apply a specific function to each element of an iterable (like a list, tuple, or set) and returns a map object (which is an iterator).

# https://www.geeksforgeeks.org/python/python-map-function/
# https://docs.python.org/3/library/functions.html
squared_numbers = list(map(lambda x: x**2, numbers))
print("cuadrados: ", squared_numbers)

# pares
"""
In Python, filter() is a built-in function used to construct an iterator from elements of an iterable for which a function returns true. It offers a concise way to select specific items from collections based on a given condition.
How filter() Works:
Arguments:
filter() takes two arguments:
function: This is a function (or None) that will be applied to each element of the iterable. It should return a boolean value (True or False). If None is provided, filter() returns elements that are inherently truthy.
iterable: This is any iterable object, such as a list, tuple, string, or set.
"""
even = list(filter(lambda x: x % 2 == 0, numbers))
print("pares: ", even)
