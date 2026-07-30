class Order:
    global_discount = 10

    def __init__(self, amount):
        self.amount = amount

    # Quiero modificarlo pero no instanciarlo. Class method necesita cls, para que se refiera a la clase
    @classmethod
    def update_global_discount(cls, new_discount):
        cls.global_discount = new_discount


Order.update_global_discount(15)
print(Order.global_discount)
