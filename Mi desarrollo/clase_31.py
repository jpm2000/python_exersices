"""
Manipular CSVs
"""

import csv
import json

# leer un archivo
"""
with open(
    "/Users/juanpablomanrique/Documents/Repositories/python_exersices/6.Lectura y escritura de archivos/products.csv",
    mode="r",
) as file:
    csv_reader = csv.DictReader(file)
    for row in csv_reader:
        print(row)
"""

# puedo ir iteranto en cada columna. Me hacce la duda de que diferencia hay entre esto con pandas

"""
with open(
    "/Users/juanpablomanrique/Documents/Repositories/python_exersices/6.Lectura y escritura de archivos/products.csv",
    mode="r",
) as file:
    csv_reader = csv.DictReader(file)
    for row in csv_reader:
        print(f"Producto: {row['name']}, Precio: {row['price']}")

"""

# new data exercise
"""
new_product = {
    "name": "Wireless charger",
    "price": 75,
    "quantity": 100,
    "brand": "Super cargadores",
    "category": "Accesories",
    "entry_date": "2025-10-30",
}

# abrir el archivo para cambiarle el formato. A de append "a"

with open(
    "/Users/juanpablomanrique/Documents/Repositories/python_exersices/6.Lectura y escritura de archivos/products.csv",
    mode="a",
    newline="",
) as file:
    # Agrgearle un salto de linea file.write("\n")
    file.write("\n")
    csv_writer = csv.DictWriter(file, fieldnames=new_product.keys())
    # Solo se le hace un cambio directamente al CSV
    csv_writer.writerow(new_product)
"""

# new column

# Modo lectura para agregarla solo al nuevo path
file_path = "/Users/juanpablomanrique/Documents/Repositories/python_exersices/6.Lectura y escritura de archivos/products.csv"
updated_file_path = "/Users/juanpablomanrique/Documents/Repositories/python_exersices/6.Lectura y escritura de archivos/products_updated_3.csv"

new_data = {
    "name": "Ketones",
    "price": 110,
    "quantity": 50,
    "brand": "JPM",
    "category": "nutrition",
    "entry_date": 2025 - 10 - 30,
    "total_value": 100 * 50,
}

json_file_path = "/Users/juanpablomanrique/Documents/Repositories/python_exersices/6.Lectura y escritura de archivos/products_json.json"

with open(file_path, mode="r") as file:
    csv_reader = csv.DictReader(file)
    # obtener los nombres de las columnas existentes
    fieldnames = csv_reader.fieldnames + ["total_value"]
    with open(updated_file_path, mode="w", newline="") as updated_file:
        csv_writer = csv.DictWriter(updated_file, fieldnames=fieldnames)
        csv_writer.writeheader()  # Escribir encabezado

        for row in csv_reader:
            # Lo busca en la columna que se creó
            row["total_value"] = float(row["price"]) * int(row["quantity"])
            csv_writer.writerow(row)

        csv_escribe = csv.DictWriter(updated_file, fieldnames=new_data.keys())
        csv_escribe.writerow(new_data)

json_file_path = "/Users/juanpablomanrique/Documents/Repositories/python_exersices/6.Lectura y escritura de archivos/products_json.json"


with open(file_path, mode="r") as file:
    csv_read = csv.DictReader(file)
    data = list(csv_read)

with open(json_file_path, mode="w") as json_file:
    json.dump(data, json_file, indent=4)

print("archivo en json")
