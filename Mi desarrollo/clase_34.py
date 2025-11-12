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

print("")
print("cmath")

import cmath

complex_num = cmath.sqrt(complex(-2, 0))
print(complex_num)

# El resultado va a estar en -pi y pi
phase = cmath.phase(complex(-1, 0))
print(phase)

# Coordenadas polares: Las coordenadas polares son un sistema de coordenadas bidimensional que localiza un punto usando una distancia radial (\(r\)) desde un punto de origen (llamado polo) y un ángulo (\(\theta \)) desde un rayo de referencia (el eje polar).
# Este sistema es una alternativa a las coordenadas cartesianas y es muy útil en física y trigonometría, especialmente cuando se trata de rotaciones y formas circulares.
polar = cmath.polar(2)
print(polar)

polar_negativo = cmath.polar(-2)
print(polar_negativo)

# Coordenadas entre r y po
rect = cmath.rect(1, 5)
print(rect)

# e elevado a la x, donde ingreso x como varaible
exp = cmath.exp(10)
print(exp)

log = cmath.log(2, 100)
print(log)

log10 = cmath.log10(10)
print(log10)

sqrt = cmath.sqrt(10)
print(sqrt)

exp = cmath.exp(10)
print(exp)

acos = cmath.acos(2)
print(acos)

asin = cmath.asin(10)
print(asin)

cos = cmath.cos(10)
print(cos)

sin = cmath.sin(10)
print(sin)

tan = cmath.tan(10)
print(tan)

print("")
print("statistics")
from statistics import median
from math import isnan
from itertools import filterfalse

data = [20.7, float("NaN"), 19.2, 18.3, float("NaN"), 14.4]
print(sorted(data))
print(median(data))
print(sum(map(isnan, data)))
clean = list(filterfalse(isnan, data))
print(clean)

print(sorted(clean))

print(median(clean))
