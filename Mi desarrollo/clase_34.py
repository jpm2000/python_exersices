import os

cwd = os.getcwd()
print("Directorio: ", cwd)

print("")
txt_files = [
    f
    for f in os.listdir(
        "/Users/juanpablomanrique/Documents/Repositories/python_exersices/Mi desarrollo"
    )
    if f.endswith(".txt")
]
print("Archivos txt: ", txt_files)

# /Users/juanpablomanrique/Documents/Repositories/python_exersices/Mi desarrollo

"""
para ver el de mi repositorio actual

cwd = os.getcwd()
print("Directorio: ", cwd)

print("")
txt_files = [f for f in os.listdir(".") if f.endswith(".txt")]
print("Archivos txt: ", txt_files)
"""

# Para renombrar el archivo

"""


print("")
os.rename("caperucita.txt", "cuento_caperucita.txt")
print("archivo renombrado")

print("")
txt_files = [f for f in os.listdir(".") if f.endswith(".txt")]
print("Archivos txt: ", txt_files)

"""

"""
La forma de variar "." es cambiando de repositorio en el que estoy trabajando. 
En el caso anterior estaba trabajando en el repo que abarca todos los folders. 
Pero acabo de hacer una prueba en la que me movi con cd "Mi desarrollo" y volví a correr el codigo.
Me sale la duda de como editar archivos desde otro folders
"""

print("")
print("math")
import math

# Hallar el area y perimetro del circulo
radius = 5
area = math.pi * radius**2
perimeter = 2 + math.pi * radius
print(f" the area if is: {area}")
print(f"the perimeter is: {perimeter}")

print("")
print("random")

import random

# Numero entero aleatorio
random_num = random.randint(1, 10)
print(f"random number {random_num}")

# Color aleatorio
colors = ["red", "green", "blue"]
random_color = random.choice(colors)
print(f"random color {random_color}")

cards = ["as", "J", "9", "Reina", "10"]
random.shuffle(cards)
print(f"cards shuffled: {cards}")
