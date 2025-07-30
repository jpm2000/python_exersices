to_do = ["Dirigirnos al hotel",
         "Ir a almorzar",
         "Volver al hotel",
         'Ir a comer'
         ]

print(to_do)

# Tengo libertad al momento de guardar la información

numbers = [1, 2, 3, 4, 5, 'cinco']
print(numbers)

# Esta clase es list 

print(type(numbers))

mix = ["uno", 2, 3, 4, True, [1,2,3]]
print(mix)
print(len(mix))
print("Primer elemento", mix[0])
print("Ultimo elemento", mix[-1])
print(mix[1:4])

string = "Hola mundo"
print('Primer elemento', string[0])
print('Segundo elemento', string[1])
print('Tercer elemento', string[2])


# Metodos
print(mix)
mix.append(False) # se agrega False
print(mix)
mix.append(["A", "b", 100, 1000])
print(mix)
mix.insert(1, ["z", "Y"])
print(mix)
print(mix.index(["z", "Y"]))

numbers = [1,200, 500, 3, 4123,]
print(max(numbers))

# eliminar numeros

del numbers[-1]
print(numbers)