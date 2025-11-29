"""
Enunciado del ejercicio

Tienes una lista de productos en una tienda:

```python
productos = [
    {"name": "Laptop", "price": 3500, "category": "tech"},
    {"name": "Mouse", "price": 50, "category": "tech"},
    {"name": "Silla ergonómica", "price": 900, "category": "office"},
    {"name": "Escritorio", "price": 1200, "category": "office"},
]
```

1. Crea una función `filtrar_productos_caros` que:
   - Reciba la lista de productos y un `precio_minimo` (int).
   - Devuelva un `str` con una línea por cada producto cuyo `price` sea mayor a `precio_minimo`, usando un f-string, por ejemplo:
     `El producto Laptop cuesta 3500, está por encima de 1000`.
2. Si ningún producto cumple la condición, debe devolver un mensaje tipo:
   `No se encontraron productos por encima de 1000`.

Pistas técnicas a usar (igual que en tu ejercicio de empleados):
- List comprehension para filtrar.[1][2][3]
- f-strings para armar las frases.[4][5]
- `"\n".join(...)` para unir todas las líneas en un solo string.
"""

from typing import TypeAlias

productos = [
    {"name": "Laptop", "price": 3500, "category": "tech"},
    {"name": "Mouse", "price": 50, "category": "tech"},
    {"name": "Silla ergonómica", "price": 900, "category": "office"},
    {"name": "Escritorio", "price": 1200, "category": "office"},
]

Precio: TypeAlias = dict[str, int | str]


def filtrar_productos_caros(lista: list[Precio], precio_min: int, category: str) -> str:
    precio_category = [
        producto
        for producto in lista
        if "price" in producto
        and producto["price"] >= precio_min
        and "category" in producto
        and producto["category"] == category
    ]

    if not precio_category:
        return f"No se encontraron productos con el precio mayor a {precio_min} y que sean de la categoria {category}"

    lineas = [
        f"El producto se llama {producto['name']}, es de la categoria {producto['category']} y cuesta {producto['price']}. El cual esta por encima del minimo {precio_min} y que es de la categoria {category}"
        for producto in precio_category
    ]

    return ".\n".join(lineas)


print(filtrar_productos_caros(productos, 900, "tech"))
