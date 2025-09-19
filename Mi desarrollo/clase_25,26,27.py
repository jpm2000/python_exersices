"""
Desarrolla una concesionaria de vehículos en la cual se puedan gestionar las compras y ventas de vehículos.
Un usuario podrá ver los vehículos disponibles, su precio y realizar la compra de uno.
Aplica los conceptos de programación orientada a objetos vistos en este ejercicio.

Ahora la empresa va a expenadir su inventario a otros productos como bicicletas


La idea es la que la clase hija herede los parámetros de la super clase

"""


# Clase padre o superclase
class Vehicle:
    # Encapsulación: variables de instancia que tiene variables privadas del objeto
    def __init__(self, brand, year, price):
        self.brand = brand
        self.year = year
        self.price = price
        self.availability = True

    def sell(self):
        if self.availability:
            self.availability = False
            print(f"The {self.brand} was sold")
        else:
            print(f"The {self.brand} is not available")

    # Abstracción:
    def check_availability(self):
        return self.availability

    # Abstracción:
    def check_price(self):
        return self.price

    # No se especifica la funcion para conectarlos con el polimorfismo
    # Iniciar el funcionamiento de los vehiculos
    def start_engine(self):
        raise NotImplementedError("This method needs to be implemented by the subclass")

    def stop_engine(self):
        raise NotImplementedError("This method needs to be implemented by the subclass")


# Herencia; dependen de la superclase
# Sub clase. Hereda los atributos de la clase Vehicle
class Car(Vehicle):
    # Polimorfismo: comportamiento diferente para diferentes formas
    def start_engine(self):
        if not self.availability:
            return f"The motor of the vehicle {self.brand} is running"
        else:
            return f"The vehicle {self.brand} is not available"

    def stop_engine(self):
        if not self.availability:
            return f"The motor of the vehicle {self.brand} is not running"
        else:
            return f"The vehicle {self.brand} is not available"


# Herencia; dependen de la superclase
class Bike(Vehicle):
    # Polimorfismo: comportamiento diferente para diferentes formas. En este caso la bicicleta no cuenta con motor
    def start_engine(self):
        if not self.availability:
            return f"The bike {self.brand} is moving"
        else:
            return f"The bike {self.brand} is not available"

    def stop_engine(self):
        if not self.availability:
            return f"The bike {self.brand} is not moving"
        else:
            return f"The bike {self.brand} is not available"


# Herencia; dependen de la superclase
class Truck(Vehicle):
    # Polimorfismo: comportamiento diferente para diferentes formas
    def start_engine(self):
        if not self.availability:
            return f"The motor of the truck {self.brand} is running"
        else:
            return f"The truck {self.brand} is not available"

    def stop_engine(self):
        if not self.availability:
            return f"The motor of the truck {self.brand} is not running"
        else:
            return f"The truck {self.brand} is not available"


class Custommer:
    def __init__(self, name):
        self.name = name
        self.purchased_vehicles = []

    def buy_vehicle(self, vehicle: Vehicle):
        if vehicle.check_availability():
            vehicle.sell()
            self.purchased_vehicles.append(vehicle)
        else:
            print(f"The vehicle {vehicle.brad} is not available")

    def inquire_vehicle(self, vehicle: Vehicle):
        if vehicle.check_availability():
            availability = "available"
        else:
            availability = "not available"
        print(
            f"The {vehicle.brand} is {availability} and costs {vehicle.check_price()}"
        )


class Dealership:
    def __init__(self):
        self.inventory = []
        self.customers = []

    def add_vehicle(self, vehicle: Vehicle):
        self.inventory.append(vehicle)
        print(f"The vehicle {vehicle.brand} has been added to the inventory")

    def add_customer(self, customer: Custommer):
        self.customers.append(customer)
        print(f"The customer {customer.name} has been added")

    # Cuando solo quiero mostrar y no recibir nada como parametro no necesito poder objetos luego del self
    def available_inventory(self):
        print("Available inventory:")
        for vehicle in self.inventory:
            if vehicle.check_availability():
                print(f"- {vehicle.brand} priced at {vehicle.check_price()}")


car1 = Car("Ferrari", 2025, 10000)
bike1 = Bike("Speacialized", 2024, 1000)
trcuk = Truck("RAM", 2020, 40000)

customer1 = Custommer("JP")
customer2 = Custommer("Juan")
customer3 = Custommer("Pablo")

retail = Dealership()
retail.add_vehicle(car1)
retail.add_vehicle(bike1)
retail.add_vehicle(trcuk)

# Vehiculos disponibles
print("")
retail.available_inventory()

# Cliente consulta un vehiculo
print("")
customer1.inquire_vehicle(car1)

# Cliente compra un vehiculo
customer1.buy_vehicle(car1)

# Vehiculos disponibles
retail.available_inventory()
