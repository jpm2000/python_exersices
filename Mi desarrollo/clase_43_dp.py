from enum import Enum
from typing import Counter
from collections import deque
from collections import defaultdict


class EstadoPedido(Enum):
    PENDIENTE = "Pendiente"
    APROBADO = "Aprobado"
    ENVIADO = "Enviado"
    EN_RUTA = "En ruta"
    ENTREGADO = "Entregado"


pedidos = [
    {
        "id": 1,
        "customer_name": "Juan",
        "product": "book",
        "status": EstadoPedido.APROBADO,
    },
    {
        "id": 2,
        "customer_name": "Juan",
        "product": "book",
        "status": EstadoPedido.PENDIENTE,
    },
    {
        "id": 3,
        "customer_name": "Juan",
        "product": "book",
        "status": EstadoPedido.EN_RUTA,
    },
    {
        "id": 4,
        "customer_name": "Juan",
        "product": "book",
        "status": EstadoPedido.ENTREGADO,
    },
    {
        "id": 5,
        "customer_name": "Juan",
        "product": "book",
        "status": EstadoPedido.ENVIADO,
    },
    {
        "id": 6,
        "customer_name": "Juan",
        "product": "book",
        "status": EstadoPedido.APROBADO,
    },
    {
        "id": 7,
        "customer_name": "Juan",
        "product": "book",
        "status": EstadoPedido.ENVIADO,
    },
]


def status(lista: list[dict]) -> list:
    return [pedido["status"] for pedido in lista]


estados = status(pedidos)
print("Lista de los estaddos de los pedidos actuales")
print(estados)


# Al principio estaba usandolo con la lista de pedidos, pero como esta tiene dicconarios no se puede iterar para crear llaves y valores.
# En cambio con la de estados, como me da una lista con los estados por pedido puedo contarlos
def count_pedidos(list_pedidos: list[dict]) -> Counter:
    return Counter(list_pedidos)


pedidos_count = count_pedidos(estados)
print("")
print("Counter")
print(pedidos_count)


def count_status(pedidos_list: list[dict]) -> defaultdict:
    status_count = defaultdict(int)
    for pedido in pedidos_list:
        status_count[pedido] += 1
    return status_count


statuses = count_status(estados)
print("")
print("defaultdict")
print(statuses)

print("")


def queue(lista_estados: list) -> deque:
    delivery_queue = deque(lista_estados)
    variable = lista_estados[1]
    print(f"segunda variable {variable}")
    print("")

    print("primera version")
    print(delivery_queue)

    delivery_queue.pop()
    print("")
    print("Eliminé el ultimo valor de la lista")
    print(delivery_queue)

    delivery_queue.append(variable)
    print("")
    print("Agregué de nuevo la variable pero al final")
    print(delivery_queue)

    delivery_queue.appendleft(EstadoPedido.APROBADO)
    print("")
    print("Agregué un nuevo valor de aprobado al inicio")
    print(delivery_queue)

    delivery_queue.popleft()
    print("")
    print("Eliminé el nuevo valor de aprobado al inicio")
    print(delivery_queue)

    return delivery_queue


queue_estados = queue(estados)

print(queue_estados)

print("")
print("Nuevo conteo")
print(count_pedidos(queue_estados))
print("Se elimina uno de enviados y se agrega uno de pendiente")
