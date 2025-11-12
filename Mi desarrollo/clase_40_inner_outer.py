x = "global"  # variable global


# funcion externa
def outer_function():
    x = "enclosign"

    # funcion interna
    def innfer_function():
        x = "local"  # variable local
        print(x)

    innfer_function()
    print(x)


outer_function()
print(x)
