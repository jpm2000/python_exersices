# 3 propiedades


class Employee:
    # Como estoy usando el guion bajo digo que el salario es un atributo protegido
    def __init__(self, name, salary):
        self.name = name
        # Usar la información desde dentro de la clase. El salario es un atributro protegido
        self._salary = salary

    # Aca se usa property porque es de tipo getter.
    @property
    def salary(self):
        return self._salary

    # En este caso va a ser setter o sea que puedo agregar nueva informacion en un atributo
    @salary.setter
    def salary(self, new_salary):
        if new_salary < 0:
            raise ValueError("Salary cannot be negative")
        self._salary = new_salary

    # Eliminar los atributos
    @salary.deleter
    def salary(self):
        print(f"The salary of {self.name} has been deleted")
        del self._salary


# Crear instancia de Employee
employee = Employee("Ana", 5000)

# Llamo directo al salario. COn getter puedo traerlo diretamente
print(employee.salary)

# Cambiar el salario
employee.salary = 6000
print(employee.salary)

# Asignar un valor negativo
# employee.salary = -6000
# print(employee.salary)

# Para eliminar
del employee.salary
print(employee.salary)
