# Crear una lista con un comprehension

square = [x**2 for x in range(1, 20, 2)]

print(square)

print(20*"-", "Cambio de grados")
# Ejemplo de grados celsius a farenheit
c = [0, 10, 20, 30, 40]
f = [(temp * 1.8) + 32 for temp in c]

print( "Temperatura en grados fahrenheit: ", f)

print(20*"-", " Numeros pares")
pares = [n for n in range(0, 21) if n%2 == 0]
print(pares)

print(20*"-", " Transpuesta")
# Transpuesta de una matriz

matrix = [[1,2,3],
          [4,5,6],
          [7,8,9]
]

transpuesta = [[row[i] for row in matrix] for i in range(len(matrix[0]))]

print(matrix)
print(transpuesta)

print(20*"-", " Transpuesta con más lineas de código")
# Transpuesta de una matriz

trans_new = []
for i in range(len(matrix[0])):
    trans = []
    for row in matrix:
        trans.append(row[i])
    trans_new.append(trans)

print(trans_new)

print(20*"-", " Ejercicios")

"""
Ejercicios

1. **Doble de los Números**  
    Dada una lista de números `[1, 2, 3, 4, 5]`, crea una nueva lista que contenga el doble de cada número usando una List Comprehension.
    
2. **Filtrar y Transformar en un Solo Paso**  
    Tienes una lista de palabras `["sol", "mar", "montaña", "rio", "estrella"]` y quieres obtener una nueva lista con las palabras que tengan más de 3 letras y estén en mayúsculas.
    
3. **Crear un Diccionario con List Comprehension**  
    Tienes dos listas, una de claves `["nombre", "edad", "ocupación"]` y otra de valores `["Juan", 30, "Ingeniero"]`. Crea un diccionario combinando ambas listas usando una List Comprehension.
    
4. **Anidación de List Comprehensions**  
    Dada una lista de listas (una matriz):
    
    ```python
    pythonCopiar código
    matriz = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    ```
    
    Calcula la matriz traspuesta utilizando una List Comprehension anidada.
    
5. **Extraer Información de una Lista de Diccionarios**  
    Dada una lista de diccionarios que representan personas:
    
    ```python
    pythonCopiar código
    personas = [
        {"nombre": "Juan", "edad": 25, "ciudad": "Madrid"},
        {"nombre": "Ana", "edad": 32, "ciudad": "Madrid"},
        {"nombre": "Pedro", "edad": 35, "ciudad": "Barcelona"},
        {"nombre": "Laura", "edad": 40, "ciudad": "Madrid"}
    ]
    ```
    
    Extrae una lista de nombres de personas que viven en “Madrid” y tienen más de 30 años.
    
6. **List Comprehension con un `else`**  
    Dada una lista de números `[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]`, crea una nueva lista multiplicando por 2 los números pares y dejando los impares como están.

"""

# Ejercicio #1 

# Dada una lista de números, crea una nueva lista que contenga el doble de cada número usando una List Comprehension.
num = [1, 2, 3, 4, 5]

double = [i*2 for i in num]
print("Ejercicio #1, doblar los valores de la lista: ", double)

# Ejercio #2: Filtrar y Transformar en un Solo Paso**  

# Tienes una lista de palabras `["sol", "mar", "montaña", "rio", "estrella"]` y quieres obtener una nueva lista con las palabras que tengan más de 3 letras y estén en mayúsculas.

natu = ["sol", "mar", "montaña", "rio", "estrella"]

new_natu = [i.upper() for i in natu if len(i) >= 3]
print("Palabras con más de 3 letras: ", new_natu)

# Ejercicio #3: Crear un Diccionario con List Comprehension

# Tienes dos listas, una de claves `["nombre", "edad", "ocupación"]` y otra de valores `["Juan", 30, "Ingeniero"]`. Crea un diccionario combinando ambas listas usando una List Comprehension.

claves = ["nombre", "edad", "ocupación"]
valores = ["Juan", 30, "Ingeniero"]

dictionary = {claves[i]: valores[i] for i in range(len(valores))}

print("Se crea un diccionario con las dos listas: ", dictionary)


'''
claves1 = ["nombre", "edad", "ocupación"]
valores2 = ["Juan", 30, "Ingeniero"]

nuevo = {claves1[i]: valores2[i] for i in range(len(claves1))}
print(nuevo)

'''

# Ejercicio #4: Anidación de List Comprehensions**  

# Dada una lista de listas (una matriz). Calcula la matriz traspuesta utilizando una List Comprehension anidada.

matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
    ]

transp = [[row[i] for row in matriz] for i in range(len(matriz[0]))]

print("Me pide sacar la transpuesta de la matriz: ", transp)

# Ejercicio #5: Extraer Información de una Lista de Diccionarios: Dada una lista de diccionarios que representan personas:
# Extrae una lista de nombres de personas que viven en “Madrid” y tienen más de 30 años.
    
personas = [
    {"nombre": "Juan", "edad": 25, "ciudad": "Madrid"},
    {"nombre": "Ana", "edad": 32, "ciudad": "Madrid"},
    {"nombre": "Pedro", "edad": 35, "ciudad": "Barcelona"},
    {"nombre": "Laura", "edad": 40, "ciudad": "Madrid"}
]

madrid = [persona["nombre"] for persona in personas if persona["ciudad"] == "Madrid" and persona["edad"] > 30]

print(madrid)

# Ejercicio #6: List Comprehension con un `else'

# Dada una lista de números `[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]`, crea una nueva lista multiplicando por 2 los números pares y dejando los impares como están.

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

pares_impares = [i*2 if i%2 == 0 else i for i in lista]
print("Solo los pares se multiplican y los impares se quedan igual: ", pares_impares)