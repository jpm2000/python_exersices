# Por ahora lo unique quiero hacer es leer, por eso la r de read. Leer archivo linea por linea
"""
with open(
    "Mi desarrollo/caperucita.txt",
    "r"
) as file:
    for lineas in file:
        # Imprimierlas y eliminar los espacios de las lineas
        print("Ejemplo usando strip()")
        print(lineas.strip())
"""

# Leer todas las lineas en una lista
"""
with open(
    "Mi desarrollo/caperucita.txt",
    "r"
) as file:
    lines = file.readlines()
    print(lines)

"""

# Se hace referencia a una "a" de append para agregar nuestos strings. Se le va a agregar dos salto de linea al final
"""
with open("Mi desarrollo/caperucita.txt", "a") as file:
    file.write("\n\nEdited by: JP")
"""

# Sobreescribir el texto con "w", este es el modo escritura. Cuando veo el archivo solo se ve el texto que he escrito, la información se borra.
"""
with open("Mi desarrollo/caperucita.txt", "w") as file:
    file.write("\n\nEdited by: JP")
"""
"""
Desafío: ¿Cuántas líneas tiene el cuento de Caperucita Roja?

Ahora, te dejo un reto: cuenta el número de líneas en el archivo `caperucita.txt` y comparte tu resultado en los comentarios. 
Este ejercicio no solo reforzará tus habilidades, sino que también te acercará a comprender el poder del manejo de archivos en Python.

¡Sigue explorando y practicando para dominar estas habilidades! 
Python ofrece un camino rico en posibilidades para interactuar con datos y archivos de manera eficiente y efectiva.
"""

with open("Mi desarrollo/cuento.txt", "r") as file:
    lines = file.readlines()
    print(len(lines))
