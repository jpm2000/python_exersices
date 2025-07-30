numbers = {1:"uno", 2:"tres", 3:"tres"}
print(numbers)

# Para extraer información hay que hacer referenvcia a la llave

print(numbers[2])

# Elimnar un valor

info = {"name": "JP",
        "last name": "Manrique",
        "edad": 24}

print(info)

del info["last name"]
print((info))

# Metodos de los diccionarios

claves = info.keys()
print(claves)
print(type(claves))

values = info.values()
print(values)
print(type(values))

items = info.items()
print(items)
print(type(items)) # da separado en tuplas

contact = {"Juan pablo" : {"name": "JP",
        "last name": "Manrique",
        "edad": 24
    }, "Sylvanita":
    {
        "name": "Sylvana",
        "last name": "Jacqmin",
        "edad": 25
    }
}

print(contact)
print(contact["Sylvanita"])