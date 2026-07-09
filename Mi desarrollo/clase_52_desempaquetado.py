# Desempaquetado de args
def add(a, b, c):
    return a + b + c


print("Args")
values = (1, 2, 3)

# Pasarlo directamente. No pasó los args como tal, si no los pasó por values
print(add(*values))

print("")
print("KWargs")


# Desempaquetado de los kwargs
def show_info(name, age):
    print(f"Name: {name}, Age: {age}")


data = {"name": "Anna", "age": 28}

show_info(**data)
