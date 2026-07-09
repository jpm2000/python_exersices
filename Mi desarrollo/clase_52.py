# Aca voy a recibir los args y se pone con *
def sum_numbers(*args):
    return sum(args)


print("Args:")
print(sum_numbers(1, 2, 3, 4, 5, 6))
print(sum_numbers(1, 2, 3))
print(sum_numbers(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))

print("")
print("Kargs:")


# No se cuantos van a ser
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}; {value}")


print_info(name="Carlos", edad="30", city="Bogota")
print_info(name="Carlos", edad="30", city="Bogota", country="Colombia")

print("")
print("Con una clase:")


class Employee:
    def __init__(self, name, *args, **kwargs):
        self.name = name
        # No todos tienen los mismos skills
        self.skills = args
        self.detail = kwargs

    def show_employee(self):
        print(f"Employee: {self.name}")
        print("Skills", self.skills)
        print("Details", self.detail)


# Los lenguages van a pasar de una a args y los que mando de manera directa como age y city  van a kwargs
employee = Employee("Carlos", "Python", "Java", "C++", age=30, city="Bogota")
employee.show_employee()
