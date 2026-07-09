"""
Como reto, intenta crear una función que reciba una cantidad variable de precios con `*args` y un descuento opcional con `**kwargs`,
aplicando ese descuento a los productos indicados.
La práctica te ayudará a identificar rápidamente cuál técnica usar en cada situación.
¿Qué combinación te resultó más útil?
Comparte tu solución en los comentarios.
"""


class Products:
    def __init__(self, product_line, *args, **kwargs):
        self.product_line = product_line
        self.prices = args
        self.disc = kwargs

    def show_prices(self):
        print(f"Product line: {self.product_line}")
        print(f"Prices with no discount: {self.prices}")
        for key, value in self.disc.items():
            print(f"{key}: {value}")

    def prices_with_discount(self):
        precios_finales = []
        print(f"Product line: {self.product_line}")
        print(f"Prices with no discount: {self.prices}")
        for prices, disc in zip(self.prices, self.disc.values()):
            precio_final = prices * (1 - disc)
            precios_finales.append(precio_final)
            print(
                f"Precio original: {prices} | Descueto: {disc} | Precio final: {precio_final}"
            )
        return precios_finales


precios = Products(
    "Celulares",
    5000000,
    1000000,
    300500,
    6000001,
    80000,
    discount_1=0.5,
    discount_2=0,
    discount_3=0.1,
    discount_4=0,
    discount_5=0.7,
)
print("V1")
precios.show_prices()
print("")
print("V2")
precios.prices_with_discount()

print("")
print("V3")
precios_finales = precios.prices_with_discount()
print(precios_finales)
