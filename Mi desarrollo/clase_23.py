# Programación orientada a objetos

"""
Dice que el software debe organizarse en objetos que son instancias de clases

Son una plantilla genérica, debe tener caracteríasticas o atributos
"""

class Person:
    def __init__(self, name, edad):
        # Su nombre va a ser el parámetro que recibimos
        self.name = name
        # Su edad va a ser el parámetro que recibimos
        self.edad = edad

    def greet(self):
        print(f"Hola, mi nombre es {self.name} y tengo {self.edad}")


# Crear el objeto
person = Person("JP", 24)
perosn_1 = Person("Juan", 25)

# Esto es el metodo
person.greet()
perosn_1.greet()

# Bank account

class BankAccount:
    def __init__(self, holder, balance) -> None:
        self.holder = holder
        self.balance = balance
        self.is_active = True
    
    def deposit(self, amount):
        if self.is_active:
            self.balance += amount
            print(f"Se han depositado {amount} y el saldo actual es {self.balance}")
        else:
            print("La cuenta no está activa")

    def withdraw(self, amount):
        if self.is_active:
            if amount <= self.balance:
                self.balance -= amount
                print(f"Se ha retirado {amount} y el saldo actual es de {self.balance}")
    
    def deactivate(self):
        self.is_active = False
        print("La cuenta está desactivadad")
    
    def activate(self):
        self.is_active = True
        print("La cuenta está activadad")


# crear objetos

account = BankAccount("JP", 500)
account_2 = BankAccount("Juan", 200)

# Llamada a los metodos

account.deposit(200)
account_2.deposit(150)
account.deactivate()
account.deposit(150)
account.activate()
account.deposit(50)
account.withdraw(25)