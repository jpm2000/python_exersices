from collections import defaultdict


def count_products(orders: list[str]) -> defaultdict:
    product_count = defaultdict(int)  # crea un diccionario con valor por defecto 0
    for product in orders:
        product_count[product] += 1
    return product_count


orders = ["laptop", "smartphone", "laptop", "tablet"]
count = count_products(orders)
print(count)


# Contar las ventas

print("")
print("Contar las ventas")

from collections import Counter


def count_sales(products: list[str]) -> Counter:
    # Usa counter para contar cuantos productos se han vendido
    return Counter(products)


sales = ["laptop", "smartphone", "smartphone", "laptop", "tablet"]
result = count_sales(sales)
print(result)

print("")
print("Envio de una cola")

from collections import deque


def manage_delivery_queue() -> deque:
    # Crea una cola para gestionar la entrega de productos
    delivery_queue = deque(["order_1", "order_2", "order_3"])
    delivery_queue.append("order_4")  # agrega al final de la lista
    delivery_queue.appendleft("order_0")  # agregar al inicio
    delivery_queue.pop()  # ya no existe la orden 4
    delivery_queue.popleft()  # elimina el 0

    return delivery_queue


print(manage_delivery_queue())

print("")
print("Enumeraciones")

from enum import Enum


class OrderStatus(Enum):  # Ereda las propiedades de la libreria
    PENDING = 1
    SHIPPED = 2
    DELIVERED = 3


def check_order_status(status: OrderStatus):  # comprobar el estado del pedido
    # Comprueba el estado del pedido
    if status == OrderStatus.PENDING:
        return "Order is still pending"
    elif status == OrderStatus.SHIPPED:
        return "Order has being shipped"
    elif status == OrderStatus.DELIVERED:
        return "Order delivered"


print(check_order_status(OrderStatus.SHIPPED))
print(check_order_status(OrderStatus.PENDING))
print(check_order_status(OrderStatus.DELIVERED))
