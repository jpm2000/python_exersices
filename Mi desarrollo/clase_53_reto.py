"""
Un buen ejercicio para practicar estos conceptos es implementar una clase CuentaBancaria que contenga un método protegido para actualizar el saldo,
permitiendo consultarlo de manera externa, y un método privado para registrar transacciones,
ya que esa lógica solo le pertenece a la clase de manera interna [08:10].
Comprender cuándo usar cada nivel de acceso es lo que permite escribir código más seguro y profesional.
¿Ya has probado a refactorizar alguna de tus clases aplicando estos niveles de encapsulamiento?
"""


class Account:
    def __init__(self, holder: str, number: int, balance: int):
        if balance < 0:
            raise ValueError("El saldo no puede ser negativo")
        self.holder = holder
        self.number = number
        self.__balance = balance

    @property
    def balance(self) -> int:
        return self.__balance

    def _notificar_saldo(self, transaccion: int):
        print(
            f"Se realizó un movimiento en su cuenta {transaccion}. Este es el saldo actualizado {self.balance}, para la cuenta numero {self.number} de {self.holder}"
        )

    def __registro_transaccion(self, transaccion: int, tipo: str):
        if tipo == "retiro":
            if transaccion > self.__balance or transaccion <= 0:
                raise ValueError(
                    "La transacción no puede exeder el balance de la cuenta, ser 0 o un valor negativo"
                )
            elif transaccion <= self.__balance and transaccion > 0:
                self.__balance -= transaccion
                print(
                    f"Usted acaba de enviar una transaccion de {transaccion}, desde su cuenta."
                )
            return self._notificar_saldo(transaccion)
        elif tipo == "recibir":
            if transaccion <= 0:
                raise ValueError("La transacción no puede ser un valor negativo o 0")
            else:
                self.__balance += transaccion
                print(f"Usted acaba de recibir {transaccion}, en su cuenta.")
            return self._notificar_saldo(transaccion)
        else:
            raise ValueError(
                "Seleccione un tipo de transaccion correcto entre retiro o recibir"
            )

    def public_method(self, transaccion: int, tipo: str) -> None:
        self.__registro_transaccion(transaccion, tipo)


class CuentasAhorros(Account):
    def _notificar_saldo(self, transaccion: int):
        print(
            f"[Cuenta de Ahorros] movimiento {transaccion} nuevo saldo {self.balance} generando intereses"
        )

    def __registro_transaccion(self, transaccion: int, tipo: str):
        print("Intento de override")


"""

cuenta = Account("JP", 1, 0)
# cuenta.public_method(0, "recibir")
cuenta.public_method(100000, "recibir")
print(cuenta.balance)
# cuenta.public_method(400, "retiro")
# print(cuenta.balance)
cuenta.public_method(100000, "retiro")
print(cuenta.balance)
cuenta.public_method(50, "deposito")

"""


ahorros = CuentasAhorros("Juan Pablo", 2, 1000)
ahorros.public_method(5000000, "recibir")
ahorros.public_method(100, "recibir")
