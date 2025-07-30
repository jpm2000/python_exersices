x = 2
if x > 5:
    print("x es mayor a 5")
    print("adentro del print")
else:
    print("x es menor a 5")

print("afuera del if")

if x >= 10:
    print("es mayor o igual a 10")
elif x == 5:
    print("x es igual a 5")
else:
    print("ninguna de las anteriores")


y = 15
z = 20

if y > 10 and z > 25:
    print("y es mayor que 10 y z es mayor que 25")


if y >= 10 or z < 25:
    print("y es mayor que 10 o z es mayor que 25")

if not y > 10:
    print("x no es mayor 10") # con el not estoy diciendo que si sucede ese if, lo hace porque no lo es


is_member = True # probar tambien con False
age = 10 # probar con varias edades

if is_member:
    if age >=15:
        print("tiene acceso porque es miembro y mayor a 15")
    else:
        print("no tiene acceso, aún así seas miembro")
else:
    print("no eres miembro")

