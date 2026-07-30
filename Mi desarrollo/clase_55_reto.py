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
    def descuento_global(cls, amount, nuevo_descuento):
        cls.descuento = nuevo_descuento
        return cls.descuento * amount


Pedido.pedido_min(110, 50)
print(Pedido.descuento_global(20000, 0.21))
