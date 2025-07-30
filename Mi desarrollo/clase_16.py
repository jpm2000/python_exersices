# Iteración y bluces

numbers = [1, 2,3,4,5,6,7,8,9,10]

for i in numbers:
    print("Aqui i es igual a: ", i+1)

for i in range(10):
    print(i)

frutas = ["Manzana", "limon", "pera", "uva", "kiwi", "maracuya", "patilla"]

for fruta in frutas:
    if fruta == "naranja":
        print("naranja encontrada")
    elif fruta == "kiwi":
        print("kiwi encotrado")
    else:
        print("na")

x = 0 

while x < 5:
    if x == 3:
        break # se rompe el if
    print(x)
    x += 1


numbers = [1, 2,3,4,5,6,7,8,9,10]

for i in numbers:
    if i == 3:
        continue
    elif i == 8:
        break
    print("Aqui i es igual a: ", i+1)