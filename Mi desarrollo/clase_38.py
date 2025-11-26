numbers = [1, 2, 3, 4, 5, 6]

# Metodo #1

squares = []

for n in numbers:
    square = n**2
    squares.append(square)

print(squares)

# Método pythonico
print("")

squares_2 = [x**2 for x in numbers]
print(squares_2)


# Calculadora, prácitica P8
print("")


class Calculadora:
    def add_numbers(self, a, b):
        return a + b


calc = Calculadora()

print(calc.add_numbers(1, 2))


# List comprehension: Haz lo mismo pero usando una función nombrada y docstring
print("")


def calculo_lista(list):
    squares_3 = [x**2 for x in list]
    return squares_3


"""
def calculo_lista(list):
    return [x**2 for x in list]

"""


print(calculo_lista(numbers))

range = [x**2 for x in range(1, 11)]

print(range)

names = ["Juan", "Pablo", "Manrique", "Bonilla"]

upper = [n.upper() for n in names]

print(upper)
