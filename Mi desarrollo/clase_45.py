# Crear el decorador para determinar si el empleado tiene un empleado determinado
# Este es el decorador anidado
def check_access(required_role):
    def decorador(func):
        def wrapper(employee):
            # Si el rol del empleado coincide con el rol seleccionado
            if employee.get("role") == required_role:
                return func(employee)
            else:
                print(
                    f"Acseso denegado. Solo {required_role} puede realizar esta tarea"
                )

        return wrapper

    return decorador


# Este es el decorador comparable
def log_action(func):
    # Se puede hacer solo el wrapper, y no usar el decorador, por lo que ya le estamos pasando la función
    def wrapper(employee):
        print(f"Registrando acción para el empleado {employee['name']}")
        return func(employee)

    return wrapper


# Estamos llamando a dos decoradores como tal, uno ya tiene el decorador del otro
@check_access("admin")
@log_action
def delete_employee(employee):
    print(f"El empleado {employee['name']}, ha sido eliminado")


admin = {"name": "Juan Pablo", "role": "admin"}
employee = {"name": "Tomas", "role": "employee"}

delete_employee(admin)
delete_employee(employee)
