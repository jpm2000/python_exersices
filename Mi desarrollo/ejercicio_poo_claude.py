"""
Perfecto, ahora que veo que también quieres practicar la función `super()`, te he creado un ejercicio más completo que integra todos los conceptos: clases, herencia, polimorfismo y el uso de `super()`.Este ejercicio te permitirá practicar todos los conceptos que mencionas en tus notas:

Conceptos que vas a repasar:

1. Clases y Constructores
- Definir clases con atributos (características) y métodos (acciones)
- Usar `__init__()` como constructor para inicializar objetos

2. Herencia
- `Empleado` hereda de `Persona`
- `Desarrollador`, `Gerente` y `Vendedor` heredan de `Empleado`
- Jerarquía de 3 niveles como en tus notas

3. Función super()
- Llamar métodos de la superclase desde la subclase
- Evitar repetir código en los constructores
- Mantener la cadena de herencia limpia

4. Polimorfismo
- Los métodos `trabajar()`, `calcular_salario()` y `presentarse()` se comportan diferente según el tipo de empleado
- Mismo método, diferentes implementaciones

5. Encapsulamiento
- Uso de métodos públicos para acceder y modificar datos
- Control de acceso a la información

Progresión sugerida:
1. **Completa la clase `Persona`** (ya está hecha como ejemplo)
2. **Implementa `Empleado`** usando `super()`
3. **Crea las subclases especializadas** (`Desarrollador`, `Gerente`, `Vendedor`)
4. **Desarrolla la clase `Empresa`** para gestionar empleados
5. **Ejecuta las pruebas** para verificar el polimorfismo

¿Te gustaría que te ayude con alguna parte específica del ejercicio o tienes alguna duda sobre cómo implementar algún concepto?
"""

# EJERCICIO: Sistema de Gestión de Empleados
# Practicar: Clases, Herencia, Polimorfismo y super()

# PARTE 1: Implementa las clases base
# =================================


class Persona:
    """Clase base que representa a una persona"""

    def __init__(self, nombre, edad, documento):
        self.nombre = nombre
        self.edad = edad
        self.documento = documento

    def presentarse(self):
        print(f"Hola, soy {self.nombre}, tengo {self.edad} años")

    def obtener_info_basica(self):
        return f"Nombre: {self.nombre}, Edad: {self.edad}, Documento: {self.documento}"


class Empleado(Persona):
    """Clase que hereda de Persona y representa a un empleado"""

    def __init__(self, nombre, edad, documento, salario_base, departamento):
        # TODO: Usar super() para inicializar los atributos de Persona
        # TODO: Añadir atributos específicos: salario_base, departamento
        pass

    def trabajar(self):
        # TODO: Método genérico (será sobrescrito por las subclases)
        pass

    def calcular_salario(self):
        # TODO: Método genérico que retorna el salario base
        pass

    def presentarse(self):
        # TODO: Usar super() para llamar al método de Persona
        # TODO: Añadir información específica del empleado
        pass


# PARTE 2: Implementa las subclases especializadas
# ===============================================


class Desarrollador(Empleado):
    """Subclase de Empleado especializada en desarrollo"""

    def __init__(self, nombre, edad, documento, salario_base, lenguajes):
        # TODO: Usar super() para inicializar Empleado (departamento = "Desarrollo")
        # TODO: Añadir atributo: lenguajes (lista de lenguajes de programación)
        pass

    def trabajar(self):
        # TODO: Implementar método específico
        print(f"{self.nombre} está escribiendo código...")

    def calcular_salario(self):
        # TODO: Usar super() para obtener salario base
        # TODO: Añadir bonificación del 20% por lenguajes conocidos
        pass

    def programar(self, proyecto):
        # TODO: Método específico de desarrollador
        pass


class Gerente(Empleado):
    """Subclase de Empleado especializada en gestión"""

    def __init__(self, nombre, edad, documento, salario_base, equipo_a_cargo):
        # TODO: Usar super() para inicializar Empleado (departamento = "Gerencia")
        # TODO: Añadir atributo: equipo_a_cargo (número de personas)
        pass

    def trabajar(self):
        # TODO: Implementar método específico
        print(f"{self.nombre} está gestionando el equipo...")

    def calcular_salario(self):
        # TODO: Usar super() para obtener salario base
        # TODO: Añadir bonificación de $500 por cada persona en el equipo
        pass

    def dirigir_reunion(self, tema):
        # TODO: Método específico de gerente
        pass


class Vendedor(Empleado):
    """Subclase de Empleado especializada en ventas"""

    def __init__(self, nombre, edad, documento, salario_base, meta_ventas):
        # TODO: Usar super() para inicializar Empleado (departamento = "Ventas")
        # TODO: Añadir atributos: meta_ventas, ventas_realizadas (iniciar en 0)
        pass

    def trabajar(self):
        # TODO: Implementar método específico
        print(f"{self.nombre} está contactando clientes...")

    def calcular_salario(self):
        # TODO: Usar super() para obtener salario base
        # TODO: Añadir comisión del 10% sobre ventas realizadas
        pass

    def realizar_venta(self, monto):
        # TODO: Método para registrar una venta
        pass


# PARTE 3: Implementa la clase Empresa
# ===================================


class Empresa:
    """Clase que gestiona una colección de empleados"""

    def __init__(self, nombre):
        # TODO: Inicializar nombre de empresa y lista vacía de empleados
        pass

    def contratar_empleado(self, empleado):
        # TODO: Añadir empleado a la lista
        pass

    def mostrar_empleados(self):
        # TODO: Mostrar información de todos los empleados
        pass

    def calcular_nomina_total(self):
        # TODO: Calcular la suma de todos los salarios (POLIMORFISMO)
        pass

    def hacer_trabajar_a_todos(self):
        # TODO: Llamar al método trabajar() de cada empleado (POLIMORFISMO)
        pass

    def empleados_por_departamento(self, departamento):
        # TODO: Filtrar empleados por departamento
        pass


# PARTE 4: Código de prueba
# ========================


def main():
    """Función principal para probar el sistema"""
    # Crear empresa
    empresa = Empresa("TechCorp")

    # Crear empleados de diferentes tipos
    dev1 = Desarrollador(
        "Ana García", 28, "12345678", 80000, ["Python", "JavaScript", "Java"]
    )
    dev2 = Desarrollador("Carlos López", 32, "87654321", 85000, ["C++", "Python"])

    gerente1 = Gerente("María Rodríguez", 40, "11223344", 120000, 8)

    vendedor1 = Vendedor("Pedro Martín", 35, "44332211", 50000, 100000)
    vendedor2 = Vendedor("Laura Sánchez", 29, "55667788", 48000, 80000)

    # Simular algunas ventas
    vendedor1.realizar_venta(25000)
    vendedor1.realizar_venta(15000)
    vendedor2.realizar_venta(30000)

    # Contratar empleados
    for empleado in [dev1, dev2, gerente1, vendedor1, vendedor2]:
        empresa.contratar_empleado(empleado)

    # Probar funcionalidades
    print("=== INFORMACIÓN DE LA EMPRESA ===")
    empresa.mostrar_empleados()

    print("\n=== TODOS TRABAJANDO (POLIMORFISMO) ===")
    empresa.hacer_trabajar_a_todos()

    print(f"\n=== NÓMINA TOTAL ===")
    print(f"Total a pagar: ${empresa.calcular_nomina_total():,.2f}")

    print("\n=== EMPLEADOS POR DEPARTAMENTO ===")
    for dept in ["Desarrollo", "Gerencia", "Ventas"]:
        empleados_dept = empresa.empleados_por_departamento(dept)
        print(f"{dept}: {len(empleados_dept)} empleados")

    print("\n=== MÉTODOS ESPECÍFICOS ===")
    dev1.programar("Sistema de inventario")
    gerente1.dirigir_reunion("Planificación Q4")

    print("\n=== PRESENTACIONES (POLIMORFISMO) ===")
    for empleado in empresa.empleados[:3]:  # Solo los primeros 3
        empleado.presentarse()


# Descomenta para probar tu implementación:
# if __name__ == "__main__":
#     main()

# INSTRUCCIONES:
# ==============
# 1. Completa todos los métodos marcados con TODO
# 2. Asegúrate de usar super() donde sea apropiado
# 3. Implementa correctamente el polimorfismo en los métodos trabajar(), calcular_salario() y presentarse()
# 4. Ejecuta el código de prueba para verificar tu implementación
# 5. Experimenta creando nuevos tipos de empleados

# CONCEPTOS A REPASAR:
# ===================
# - Herencia: Empleado hereda de Persona, y las especializaciones heredan de Empleado
# - super(): Usado para llamar métodos de la clase padre
# - Polimorfismo: Mismo método (trabajar, calcular_salario) con comportamientos diferentes
# - Encapsulamiento: Atributos privados y métodos públicos para acceder a ellos
# - Abstracción: Clases que representan conceptos del mundo real
