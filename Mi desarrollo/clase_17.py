# Ejemplo de iterador

lista = [1,2,3,4,5,6,7,8,9,10]

# Iterador
iterador = iter(lista)

# Print de las iteraciones
print("Iterador #1")

print(next(iterador))

print("")
print("Iterador #2")

print(next(iterador))

print("")
print("Iterador #3")

print(next(iterador))

print("")
print("Iterador #4")

print(next(iterador))


print(20*"-")
# Ireración a traves de cadenas

texto = "Hola soy Juan Pablo"

cadena_iter = iter(texto)

print(next(cadena_iter))
print(next(cadena_iter))
print(next(cadena_iter))
print(next(cadena_iter))
print(next(cadena_iter))
print(next(cadena_iter))
print(next(cadena_iter))
print(next(cadena_iter))
print(next(cadena_iter))
print(next(cadena_iter))

print(20*"-")
# Iterador de números impares

limit = 10

# En un rango de 1 a limit (10) saltar cada 2 valores. Números impares
iterador_impares = iter(range(1, limit+1, 2))

for i in iterador_impares:
    print(i)

print(20*"-")
# En un rango de 0 a limit (10) saltar cada 2 valores. Numeros pares
iterador_impares = iter(range(0, limit+1, 2))

for i in iterador_impares:
    print(i)


print(20*"-")
# Generador simple, utilizando la funcion con yield. Crea una secuencia de numeros de la cual podemso iterar
def generator():
    yield 1
    yield 2
    yield 3
    yield 10

for i in generator():
    print(i)

print(20*"-", " Fibonacci")
# Serie de Fibonacci. Vamos a tener un valor sumando los dos anteriores
def fibo(limit):
    a, b = 0, 1
    # Lo mismo que decir a = 0 y b = 1
    while a < limit:
        yield a
        a, b = b, a+b

for i in fibo(10):
    print(i)

print(20*"-", " Impar")
# Generadores pares e impares
def impar(limit):
    a = 1
    while a < limit:
        yield a
        a = a + 2

for i in impar(10):
    print(i)

print(20*"-", " Par")
# Generadores pares e impares
def impar(limit):
    a = 0
    while a < limit:
        yield a
        a = a + 2

for i in impar(10):
    print(i)