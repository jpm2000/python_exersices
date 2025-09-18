"""
Desarrolla una concesionaria de vehículos en la cual se puedan gestionar las compras y ventas de vehículos.
Un usuario podrá ver los vehículos disponibles, su precio y realizar la compra de uno.
Aplica los conceptos de programación orientada a objetos vistos en este ejercicio.

Ahora la empresa va a expenadir su inventario a otros productos como bicicletas


La idea es la que la clase hija herede los parámetros de la super clase

"""


class Cars:
    def __init__(self, brand, year, price):
        self.brand = brand
        self.year = year
        self.price = price
        self.availability = True

    def sold_inventory(self):
        if self.availability:
            self.availability = False
            print(
                f"The car {self.brand} was already bought and is not longer available"
            )
        else:
            print(f"The car {self.brand} is not available")

    def returned_inventory(self):
        self.availability = True
        print(
            f"The car {self.brand} model {self.year} at a price of {self.price} is available"
        )

    def check_availability(self):
        return self.availability

    def check_price(self):
        return self.price


class Driver:
    def __init__(self, name):
        self.name = name
        self.car_bought = []

    def buy_car(self, car):
        if car.check_availability:
            car.sold_inventory()
            self.car_bought.append(car)
        else:
            print(f"The car {car.brand} is not available")

    def return_car(self, car):
        if car in self.car_bought:
            car.returned_inventory()
            self.car_bought.remove(car)
        else:
            print(f"The car {car.brand} is now available")

    def inquire_car(sefl, car):
        available = "available" if car.availability() else "not available"
        print(f"The car {car.brand} {car.brand} is {available} and costs {car.price} ")


class Retail:
    def __init__(self):
        self.buyers = []
        self.cars = []

    def add_car(self, car):
        self.cars.append(car)
        print(f"The car {car.brand} is now available")

    def add_buyer(self, buyer):
        self.buyers.append(buyer)
        print(f"The buyer {buyer.name} is now available")

    def availability(self):
        print("Available cars")
        for car in self.cars:
            if car.check_availability:
                print(
                    f"The car {car.brand} of {car.year} is available at a price of {car.price}"
                )


# Crear el objeto de carros

car1 = Cars("Mercedes", 2025, 100)
car2 = Cars("BMW", 2000, 25)

# Crear el driver
driver1 = Driver("JP")
driver2 = Driver("MB")

# Agregar la info al consecionario

store = Retail()
store.add_car(car1)
store.add_car(car2)
store.add_buyer(driver1)
store.add_buyer(driver2)
store.availability()

driver1.buy_car(car1)
store.availability()

driver2.buy_car(car2)
store.availability()

driver1.return_car(car1)
store.availability()

car1.returned_inventory()
car1.sold_inventory()
