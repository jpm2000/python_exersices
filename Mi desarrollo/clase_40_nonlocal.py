def outer_function():
    x = "enclosing"

    def inner_function():
        nonlocal x  # La voy a modificar en esta altura
        x = "modified"
        print(f"El valor en inner es: {x}")

    inner_function()
    print(f"el valor de outer es: {x}")


outer_function()
