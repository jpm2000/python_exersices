"""
Un buen ejercicio para practicar estos conceptos es implementar una clase CuentaBancaria que contenga un método protegido para actualizar el saldo,
permitiendo consultarlo de manera externa, y un método privado para registrar transacciones,
ya que esa lógica solo le pertenece a la clase de manera interna [08:10].
Comprender cuándo usar cada nivel de acceso es lo que permite escribir código más seguro y profesional.
¿Ya has probado a refactorizar alguna de tus clases aplicando estos niveles de encapsulamiento?
"""


class Account:
    def __init__(self, holder, number, balance):
        self.holder = holder
        self.number = number
        self.balance = balance

    def _actualizar_saldo(self):
        print(
            f"Este es el saldo actualizado {self.balance} para la cuenta numero {self.number} de {self.holder}"
        )

    def __registar_transaccion(self, transaction):
        if transaction > 0:
            self.balance += transaction
        print(
            f"Se ha generado una transacción de {transaction} en la cuenta {self.number}, el saldo actual es {self.balance}"
        )

    def public_method(self):
        self.__registar_transaccion()


cuenta = Account("JP", "1", "0")
cuenta._actualizar_saldo()
# cuenta.__registar_transaccion(10000)
# cuenta._actualizar_saldo()
