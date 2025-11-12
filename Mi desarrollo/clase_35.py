import statistics
import csv
from statistics import median
from statistics import mean

monthly_sales = {}
with open(
    "/Users/juanpablomanrique/Documents/Repositories/python_exersices/Mi desarrollo/monthly_sales.csv",
    mode="r",
) as file:
    read_csv = csv.DictReader(file)
    for row in read_csv:
        month = row["month"]
        sales = int(row["sales"])
        monthly_sales[month] = sales

sales = list(monthly_sales.values())

print(sales)

# Hallar la media
median = median(sales)
print(f"la mediana de las ventas es de: {median}")

mean = mean(sales)
print(f"la media de las ventas es de: {mean}")

moda = statistics.mode(sales)
print(f"la moda de las ventas es de: {moda}")

desv_std = statistics.stdev(sales)
print(f"la desviación de las ventas es de: {desv_std}")

variance = statistics.variance(sales)
print(f"la media de las ventas es de: {variance}")

max_sales = max(sales)
min_sales = min(sales)

range = max_sales - min_sales
print(f"rango de ventas: {range}")
