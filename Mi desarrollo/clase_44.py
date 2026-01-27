def log_transaction(func):
    def wrapper():
        print("1 Log de la transacción...")
        # Acá se ejecuta la funcion process paymnet
        func()
        print("3 Log terminado...")

    return wrapper


@log_transaction
def process_payment():
    print("2 Procesando pago...")


process_payment()
