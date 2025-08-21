# Manejo de excepciones

# La idea es poder dar una solucion 

# Cada try va a tener un except
try:
    divisor = int(input("ingresa un numero divisor: "))
    result = 100/divisor
    print(result)
# ponerle el nombre de las excepciones
except ZeroDivisionError as e:
    print("Error: el divisor no puede ser 0")
    print("Ha ocurrido un error: ", e)
except ValueError as e:
    print("Error: debes poner un numero valido")
    print("Ha ocurrido un error: ", e)
# Puedo agregar un loop o un buckle para que el usuario me de la respuesta

# Las excepciones tienen jerarquia

print(20*"-")

def print_exception_hierarchy(exception_class, indent=0):
    print(' ' * indent+ exception_class.__name__)
    for subclass in exception_class.__subclasses__():
        print_exception_hierarchy(subclass, indent + 4)

print_exception_hierarchy(Exception)

# Se podria solo manejar Exception, pero es mejor manejarlo de forma específica

"""
Exception
    ArithmeticError
        FloatingPointError
        OverflowError
        ZeroDivisionError
    AssertionError
    AttributeError
    BufferError
    EOFError
    ImportError
        ModuleNotFoundError
        ZipImportError
    LookupError
        IndexError
        KeyError
        CodecRegistryError
    MemoryError
    NameError
        UnboundLocalError
    OSError
        BlockingIOError
        ChildProcessError
        ConnectionError
            BrokenPipeError
            ConnectionAbortedError
            ConnectionRefusedError
            ConnectionResetError
        FileExistsError
        FileNotFoundError
        InterruptedError
        IsADirectoryError
        NotADirectoryError
        PermissionError
        ProcessLookupError
        TimeoutError
        UnsupportedOperation
        itimer_error
    ReferenceError
    RuntimeError
        NotImplementedError
        PythonFinalizationError
        RecursionError
        _DeadlockError
    StopAsyncIteration
    StopIteration
    SyntaxError
        IndentationError
            TabError
        _IncompleteInputError
    SystemError
        CodecRegistryError
    TypeError
    ValueError
        UnicodeError
            UnicodeDecodeError
            UnicodeEncodeError
            UnicodeTranslateError
        NotShareableError
        UnsupportedOperation
    Warning
        BytesWarning
        DeprecationWarning
        EncodingWarning
        FutureWarning
        ImportWarning
        PendingDeprecationWarning
        ResourceWarning
        RuntimeWarning
        SyntaxWarning
        UnicodeWarning
        UserWarning
    InterpreterError
        InterpreterNotFoundError
    ExceptionGroup
"""