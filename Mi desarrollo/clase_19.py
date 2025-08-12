# Uso de funciones como objetos de primera clase

def greet():
    print("Hola mundo")

greet()

def greet_2(name):
    print("Hola ", name)

greet_2("JP")

def greet_3(name, last_name):
    print("Hola ", name, " ", last_name)

greet_3("JP", "Manrique")

# Si no ponen la variable puedo mandar el valor por defecto
def greet_4(name, last_name="No incluye el apellido"):
    print("Hola ", name, " ", last_name)

greet_4("JP")

# Aun asi le cambie el orden a los inputs, va a salir como tengo el print en la funcion
def greet_5(name, last_name="No incluye el apellido"):
    print("Hola ", name, " ", last_name)

greet_5(last_name="Manrique", name="JP")

# Calculadora
print(20*"-")

def sum(a, b):
    return a + b

def extract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b


def calculator():
    while True:
        print("Seleccione la opcion:")
        print("1. Suma")
        print("2. Resta")
        print("3. Multiplicacion")
        print("4. Division")
        print("5. Salir")

        option = int(input("Ingrese un numero del 1-5 según corresponda: "))
        
        if option == 5:
            print("Cerrando la operacion")
            break
        
        if option in [1,2,3,4]:
            num1 = float(input("Primer valor: "))
            num2 = float(input("Segundo valor: "))

            if option == 1:
                print("La suma es: ", sum(num1, num2))
            
            elif option == 2:
                print("La resta es: ", extract(num1, num2))
            
            elif option == 3:
                print("La potencia es: ", multiply(num1, num2))

            elif option == 4:
                print("La division es: ", divide(num1, num2))
            
            else:
                print("Opcion incerracta")

        

calculator()