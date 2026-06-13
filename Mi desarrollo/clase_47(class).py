class Counter:
    # Atributo que va a iniciar desde 0
    count = 0

    # Llamar al decorador class method
    @classmethod
    def increment(cls):
        cls.count += 1


Counter.increment()
Counter.increment()
print(Counter.count)
