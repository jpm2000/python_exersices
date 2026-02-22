class Counter:
    count = 0

    # Afecta algo de nuestra clase, y se pasa un cls po clase
    @classmethod
    def increment(cls):
        cls.count += 1


Counter.increment()
Counter.increment()
print(Counter.count)
