# Crear el decorador para expandir a funcion
def check_access(func):
    def wrapper(employee):
        # Comprobar si el empleado tiene rol "admin" que son los que eliminian los roles
        if employee.get("role") == "admin":
            return func(employee)
        else:
            print("acceso denegado, solo admin puede acceder")

    return wrapper


@check_access
def delete_employees(employee):
    print(f"El empleado {employee['name']} ha sido eliminado")


admin = {"name": "Carlos", "role": "admin"}
employee = {"name": "Ana", "role": "sales"}
# delete_employees(admin)
delete_employees(employee)
