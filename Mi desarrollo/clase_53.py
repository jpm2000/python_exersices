class BaseClass:
    def __init__(self):
        # Hay que usar la convención "_" en la variables protegidas. Vamos a poder acceder por fuera de la clase para que tengan más informacion sobre cómo usarla
        self._protected_variable = "Protected"
        # Acá también dejo el double guión bajo
        self.__private_varible = "Private"

    def _protected_method(self):
        print("Este es un metodo protegido")

    # Un double guion bajo siginifica que es un metodo privado. En los casos de arriba ha sido un guión solo
    def __private_method(self):
        print("Esto es un metodo privado")

    # Función publica. Va a llamar al método privado en este caso
    def public_method(self):
        self.__private_method()


base = BaseClass()

# Puedo acceder al metdodo como a la variable
# print(base._protected_variable)
# base._protected_method()

# Si puedo acceder al metodo privado porque está en el nivel de identación del publico. No es recomendable, solo debe usarse de manera interna lo privado
# base.public_method()

# Cuando quiero llamar al metodo privado, que pasa?
base.__private_method()
