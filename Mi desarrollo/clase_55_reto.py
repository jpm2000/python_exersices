class Pedido:
    descuento = 0.20

    def __init__(self, amount):
        self.amount = amount

    @staticmethod
    def pedido_min(cantidad_pedido, cantidad_min):
        if cantidad_pedido >= cantidad_min:
            print(
                f"El pedido fue de {cantidad_pedido} lo cual es mayor o igual a {cantidad_min}"
            )
        else:
            print("Vuelva a hacer el pedido")

    @classmethod
    def descuento_global(cls, nuevo_descuento):
        cls.descuento = nuevo_descuento
        return cls.descuento

    @classmethod
    def crear_pedido_con_descuento(cls, amount):
        monto_final = amount - (1 * (amount * cls.descuento))
        return cls(monto_final)


print("Pedido con el descuento original")
pedido_1 = Pedido.crear_pedido_con_descuento(50000)
print(pedido_1.amount)
print(f"El valor final con el descuento aplicado global es de {pedido_1.amount}")

print(" ")
print("Pedido con el descuento del 25%")
descuento_2 = Pedido.descuento_global(0.25)
pedido_2 = Pedido.crear_pedido_con_descuento(50000)
print(pedido_2.amount)
print(f"El valor final con el descuento aplicado global es de {pedido_2.amount}")
print(
    pedido_1.amount
)  # ¿sigue en 40000.0, o cambió a 37500 después de actualizar el descuento?
