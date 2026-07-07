class MultiplierFactory:
    # Creación de cada objeto

    # Cada metodo tiene un orden lógico. Como ahi creo la instancia debe ir de primero
    def __new__(cls, factor: int):
        """
        Metodo especial, que es new. Controlo la creacion de los objetos. Voy a crear un nuevo objeto o instancia.
        Llamo al mismo metodo de new
        """
        print(f"Creando instancia con factor {factor}")
        return super(MultiplierFactory, cls).__new__(cls)

    # Constructor, que le doy como información un factor
    def __init__(self, factor: int):
        """
        La variable factor me ayuda a generar la multiplicación
        """
        print(f"Inicializando con factor {factor}")
        self.factor = factor

    def __call__(self, number: int) -> int:
        """ """
        return number * self.factor


# El numero 5 va a ir directamente al constructor. Va a ser el factor
multipier = MultiplierFactory(5)

# Luego llamo al generador de multiplicadores. Quiero que este numero se multiplique con el factor
result = multipier(10)

print(result)
