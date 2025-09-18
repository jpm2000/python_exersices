# Crear la gestión de una biblioteca con clases


class Book:
    def __init__(self, author, title):
        self.title = title
        self.author = author
        self.available = True

    def borrowed(self):
        if self.available:
            self.available = False
            print(f"The book {self.title} was borrowed already")
        else:
            print(f"The book {self.title} is not available")

    def returned(self):
        self.available = True
        print(f"The book {self.title} was returned")


class User:
    def __init__(self, name, user_id):
        self.name = name
        self.user_id = user_id
        self.book_borrowed = []

    def borrow_book(self, book):
        if book.available:
            book.borrowed()
            self.book_borrowed.append(book)
        else:
            print(f"The book {book.title} is not available")

    def return_book(self, book):
        if book in self.book_borrowed:
            book.returned()
            self.book_borrowed.remove(book)
        else:
            print(f"The book {book.title} is not in the borrowed list")


class Library:
    def __init__(self):
        # Aca tengo una colección de usuarios y libros, para agregarles
        self.users = []
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print(f"The book {book.title} has been added")

    def add_user(self, user):
        self.users.append(user)
        print(f"The user {user.name} has been added")

    def show_available_books(self):
        print("Available books:")
        for book in self.books:
            if book.available:
                print(f"{book.title} by {book.author}")


# Crear los objetos de la biblioteca

# Crear el objeto de libros
book1 = Book("J. K. Rowling", "Harry Potter")
book2 = Book("George Lucas", "Star Wars")

# Crear el objeto de usuarios
user1 = User("Juan", "001")

# Crear el objeto de la biblioteca para agregar usuarios y libros

library = Library()
library.add_book(book1)
library.add_book(book2)
library.add_user(user1)

# Mostrar libros
library.show_available_books()

# Prestamos

user1.borrow_book(book1)
library.show_available_books()

user1.borrow_book(book2)
user1.return_book(book1)
library.show_available_books()

book3 = Book("Frank Herbert", "Dune")
library.add_book(book3)
library.show_available_books()

print("")
print(20 * "--")


"""
Desarrolla una concesionaria de vehículos en la cual se puedan gestionar las compras y ventas de vehículos. 
Un usuario podrá ver los vehículos disponibles, su precio y realizar la compra de uno. 
Aplica los conceptos de programación orientada a objetos vistos en este ejercicio.

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
