import json
import csv

json_file_path = "/Users/juanpablomanrique/Documents/Repositories/python_exersices/6.Lectura y escritura de archivos/products.json"
csv_file_path = "/Users/juanpablomanrique/Documents/Repositories/python_exersices/6.Lectura y escritura de archivos/products_csv.csv"

# Lectura del archivo

with open(json_file_path, mode="r") as file:
    products = json.load(file)

# Mostrar el contenido
for product in products:
    print(product)
    print("")
    print(f"Product: {product['name']}, Price: {product['price']}")

# New data json

print("")

new_data = {
    "name": "Ketones",
    "price": 110,
    "quantity": 50,
    "brand": "JPM",
    "category": "nutrition",
    "entry_date": 2025 - 10 - 30,
}

products.append(new_data)

with open(json_file_path, mode="w") as file:
    json.dump(products, file, indent=4)

print("added new data")

print("")

fieldnames = products[0].keys()

with open(csv_file_path, mode="w", newline="") as csv_file:
    csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    csv_writer.writeheader()
    csv_writer.writerows(products)

print("csv creado")
