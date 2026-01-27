# Ejercicio: implementar un decorador llamado log_employee_action, que registra cualquier acción ralizada por un empleado en un archivo plano.
def log_employee_action(func):
    def wrapper(employee):
        file_path = "Mi desarrollo/hr.txt"
        if employee.get("status") == "nuevon":
            write = func(employee)
            with open(file_path, "w") as file:
                file.write("\n\n")
        elif employee.get("status") == "despedido":
            write = func(employee)
            # return func(employee)
            with open(file_path, "w") as file:
                file.write(func(employee))
        else:
            write = func(employee)
            # print("no han habido cambios recienemente")
            with open(file_path, "w") as file:
                file.write("\n\nno han habido cambios recienemente")

    return wrapper


@log_employee_action
def new_hire(employee):
    print(f"Hay un nuevo empleado llamado {employee['name']}")


@log_employee_action
def layoff(employee):
    print(f"{employee['name']} tuvo que irse")


employee1 = {"name": "Carlos", "status": "nuevon"}
employee2 = {"name": "Ana", "status": "despedida"}
new_hire(employee1)
new_hire(employee2)
layoff(employee2)
layoff(employee1)
