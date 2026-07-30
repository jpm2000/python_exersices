class Order:
    # No voy a tener un constructor

    # Calculo de impuesto
    @staticmethod
    def calculate_tax(amount, tax_rate):
        # No le estoy mandando self, porque se puede llamar sin tener una instancia
        return amount * (tax_rate / 100)


# Para llamar al metodo estatico
print(Order.calculate_tax(1000, 18))
