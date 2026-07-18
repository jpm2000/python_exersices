"""
Reto: Clase Producto con @property

Implementa una clase Producto que use el decorador @property para gestionar
el atributo precio de forma controlada, evitando el acceso o modificación
directa sin validación.

1. Crea la clase Producto con un atributo protegido para el precio (y el
   stock), exponiendo el precio a través de una property con su getter
   correspondiente.

2. Implementa validación para asegurarse de que el precio y el stock no
   puedan ser negativos (setter).

3. Define un método para eliminar la información del inventario (deleter).

Aplica el mismo criterio que usaste en la clase Account: decide qué debe
ser público, protegido o privado, y qué relación debe existir entre el
setter de precio y el atributo stock..

"""


class Producto:
    def __init__(self, referencia: str, precio: int, num_stock: int):
        self.referencia = referencia
        self._precio = precio
        self._num_stock = num_stock

    @property
    def precio(self):
        if self._precio <= 0:
            raise ValueError(
                "Con un precio de 0 o menor no vas a generar nada de ingresos, estas regalando el producto. Esto no es caridad"
            )
        else:
            return self._precio

    @property
    def num_stock(self):
        if self._num_stock < 0:
            raise ValueError(
                "El stock del inventario no puede ser negativo. No podemos ponernos a vender aire"
            )
        else:
            return self._num_stock

    @precio.setter
    def precio(self, nuevo_precio: int):
        if nuevo_precio <= 0:
            raise ValueError(
                "Pilas no puedes cambiar el precio por un valor negativo o 0."
            )
        else:
            self._precio = nuevo_precio
            print(
                f"Acabas de actualizar el precio de tu referencia {self.referencia}, quedo con un precio de {self._precio} y un inventario de {self._num_stock}"
            )

    @num_stock.setter
    def num_stock(self, nuevo_stock: int):
        if nuevo_stock < 0:
            raise ValueError("Pilas no puedes regalar stock que no tienes.")
        else:
            self._num_stock = nuevo_stock
            print(
                f"Acabas de actualizar la cantidad de inventario que tienes de la referencia {self.referencia}, quedo con un precio de {self._precio} y un inventario de {self._num_stock}"
            )

    @num_stock.deleter
    def num_stock(self):
        print("El stock de la empresa se ha dado de bajo")
        del self._num_stock


producto1 = Producto("Gafas", 150, 10)
producto2 = Producto("Gorra", 250, 11)
producto3 = Producto("Chaqueta", 500, 3)
producto4 = Producto("Camisa", 50, 50)

print("Info del producto #1")
print(producto1._precio)
print(producto1._num_stock)
producto1.precio = 500
producto1.num_stock = 100
print(producto1.precio)
print(producto1.num_stock)
del producto1.num_stock
try:
    print(producto1.num_stock)
except AttributeError as e:
    print(f"Como se esperaba, ya no existe: {e}")

producto1.num_stock = 50
print(producto1.num_stock)

"""
print("")
print("Info del producto #2")
print(producto2._precio)
print(producto2._num_stock)
producto2.precio = 10
producto2.num_stock = 0
print(producto2.precio)
print(producto2.num_stock)
del producto2.num_stock

print("")
print("Info del producto #3")
print(producto3._precio)
print(producto3._num_stock)
producto3.precio = 0
producto3.num_stock = 1000
print(producto3.precio)
print(producto3.num_stock)
del producto3.num_stock

print("")
print("Info del producto #4")
print(producto4._precio)
print(producto4._num_stock)
producto4.precio = 120
producto4.num_stock = 1200
print(producto4.precio)
print(producto4.num_stock)
del producto4.num_stock
"""
