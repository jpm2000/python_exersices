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
        super().__init__(nombre, edad, documento)
        self.salario_base = salario_base
        self.departamento = departamento

    def trabajar(self):
        # TODO: Método genérico (será sobrescrito por las subclases)
        raise NotImplementedError(
            "Esta clase debe ser ejecutada por una subclase que especifica el trabajo de la persona"
        )

    def calcular_salario(self):
        # TODO: Método genérico que retorna el salario base
        print(f"El salario base de {self.nombre} es: {self.salario_base}")

    def presentarse(self):
        # TODO: Usar super() para llamar al método de Persona.
        # ¿Cuando se refiere al metodo de persona se refiere a traer la información básica de la persona?
        # TODO: Añadir información específica del empleado
        super().presentarse()
        super().obtener_info_basica()
        print(f"Salario: {self.salario_base}, Departamento: {self.departamento}")


# PARTE 2: Implementa las subclases especializadas
# ===============================================


class Desarrollador(Empleado):
    """Subclase de Empleado especializada en desarrollo"""

    def __init__(
        self, nombre, edad, documento, salario_base, departamento, lenguajes: list
    ):
        # TODO: Usar super() para inicializar Empleado (departamento = "Desarrollo")
        # TODO: Añadir atributo: lenguajes (lista de lenguajes de programación)
        super().__init__(nombre, edad, documento, salario_base, departamento)
        self.lenguajes = list(lenguajes)
        # ¿Aca no deberia dejar el constructur sin lenguajes y luego agregar un atributo llamado self.lenguajes = [] para crear la lista?

    def trabajar(self):
        # TODO: Implementar método específico
        print(f"{self.nombre} está escribiendo código en {self.lenguajes}")

    def calcular_salario(self):
        # TODO: Usar super() para obtener salario base
        # TODO: Añadir bonificación del 20% por lenguajes conocidos
        super().calcular_salario()
        deseadas = ["Python", "JavaScript", "Node", "Type Script", "Java", "C++"]
        coincide = any(code in self.lenguajes for code in deseadas)
        # Toca entender porque aparece así con una raya amarilla
        if coincide == True:
            self.salario_base = self.salario_base * 1.20
            print(
                f"El salario actual de {self.nombre} es {self.salario_base}, tiene un aumento por sus habilidades"
            )
        else:
            print("No posee las habilidades necesarias")

    def programar(self, proyecto):
        # TODO: Método específico de desarrollador
        print(
            f"El desarrollador sabe programar en {self.lenguajes} lo cual sirve para el proyecto {proyecto}"
        )


class Gerente(Empleado):
    """Subclase de Empleado especializada en gestión"""

    def __init__(
        self, nombre, edad, documento, salario_base, departamento, equipo_a_cargo
    ):
        # TODO: Usar super() para inicializar Empleado (departamento = "Gerencia")
        # TODO: Añadir atributo: equipo_a_cargo (número de personas)
        super().__init__(nombre, edad, documento, salario_base, departamento)
        self.equipo_a_cargo = equipo_a_cargo

    def trabajar(self):
        # TODO: Implementar método específico
        print(
            f"{self.nombre} está gestionando el equipo de {self.equipo_a_cargo} personas"
        )

    def calcular_salario(self):
        # TODO: Usar super() para obtener salario base
        # TODO: Añadir bonificación de $500 por cada persona en el equipo
        super().calcular_salario()
        if self.equipo_a_cargo > 0:
            self.salario_base = self.salario_base + (self.equipo_a_cargo * 500)
            print(f"El salario final de {self.nombre} es de {self.salario_base}")
        else:
            print(f"El salario de {self.nombre} sigue siendo {self.salario_base}")

    def dirigir_reunion(self, tema):
        # TODO: Método específico de gerente
        print(
            f"{self.nombre} tiene a cargo a {self.equipo_a_cargo} personas para el proyecto {tema}"
        )


class Vendedor(Empleado):
    """Subclase de Empleado especializada en ventas"""

    def __init__(
        self, nombre, edad, documento, salario_base, departamento, meta_ventas
    ):
        # TODO: Usar super() para inicializar Empleado (departamento = "Ventas")
        # TODO: Añadir atributos: meta_ventas, ventas_realizadas (iniciar en 0)
        super().__init__(nombre, edad, documento, salario_base, departamento)
        self.meta_ventas = meta_ventas
        self.ventas_realizadas = 0

    def trabajar(self):
        # TODO: Implementar método específico
        print(
            f"{self.nombre} está contactando clientes para llegar a {self.meta_ventas} y va {self.ventas_realizadas}"
        )

    def calcular_salario(self):
        # TODO: Usar super() para obtener salario base
        # TODO: Añadir comisión del 10% sobre ventas realizadas
        super().calcular_salario()
        if self.ventas_realizadas > 0:
            self.salario_base = self.salario_base + (self.ventas_realizadas * 0.10)
            print(f"El salario actualizado de {self.nombre} es de {self.salario_base}")
        else:
            print(
                f"El salario actual de {self.nombre} es de {self.salario_base}, ya que no ha aumentados sus ventas"
            )

    def realizar_venta(self, monto):
        # TODO: Método para registrar una venta
        if monto > 0:
            self.ventas_realizadas = self.ventas_realizadas + monto
            print(
                f"{self.nombre} ha realizado una nueva venta y ahora va: {self.ventas_realizadas}"
            )
        else:
            print(f"{self.nombre} no ha vendido nada, puro humo")


# PARTE 3: Implementa la clase Empresa
# ===================================


class Empresa:
    """Clase que gestiona una colección de empleados"""

    def __init__(self, nombre):
        # TODO: Inicializar nombre de empresa y lista vacía de empleados
        self.nombre = nombre
        self.empleados = []

    def contratar_empleado(self, empleado: Empleado):
        # TODO: Añadir empleado a la lista
        self.empleados.append(empleado)
        print(
            f"Tenemos un nuevo empleado en la empresa, su nombre es {empleado.nombre} y está en el departamento de {empleado.departamento}"
        )

    def mostrar_empleados(self):
        # TODO: Mostrar información de todos los empleados
        print(f"Los empleados de la empresa: {self.empleados}")

    def calcular_nomina_total(self):
        # TODO: Calcular la suma de todos los salarios (POLIMORFISMO)
        for salario in self.empleados:
            if salario.calcular_salario() == 0:
                print(f"En {self.nombre} no han contratado a nadie")
            else:
                suma = sum(salario)
                print(
                    f"La empresa {self.nombre} está gastando en salarios mensuales: {suma}"
                )

    def hacer_trabajar_a_todos(self):
        # TODO: Llamar al método trabajar() de cada empleado (POLIMORFISMO)
        print(
            f"La información de todos los trabajadores en {self.nombre} es la siguiente:"
        )
        if self.empleados == 0:
            print(
                "No se puede mostrar la información de los trabajadores porque no han contratado"
            )
        else:
            for trabajo in self.empleados:
                print(f"- {trabajo}")

    def empleados_por_departamento(self, departamento: Empleado):
        # TODO: Filtrar empleados por departamento
        print(
            f"La información de todos los trabajadores por departamento en {self.nombre} es la siguiente:"
        )
        if self.empleados == 0:
            print(
                "No se puede mostrar la información de los trabajadores por departamento que no han contratado"
            )
        else:
            for dept in empleado.departamento:
                print(f"- {dept}")


# PARTE 4: Código de prueba
# ========================


def main():
    """Función principal para probar el sistema"""
    # Crear empresa
    empresa = Empresa("TechCorp")

    # Crear empleados de diferentes tipos
    dev1 = Desarrollador(
        "Ana García",
        28,
        "12345678",
        80000,
        "Desarrollo",
        ["Python", "JavaScript", "Java"],
    )
    dev2 = Desarrollador(
        "Carlos López", 32, "87654321", 85000, "Desarrollo", ["C++", "Python"]
    )

    gerente1 = Gerente("María Rodríguez", 40, "11223344", 120000, "C-Level", 8)

    vendedor1 = Vendedor("Pedro Martín", 35, "44332211", 50000, "Ventas", 100000)
    vendedor2 = Vendedor("Laura Sánchez", 29, "55667788", 48000, "Ventas", 80000)

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
if __name__ == "__main__":
    main()

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

print("")
print(20 * "-")
print("Prueba clase Persona")
persona = Persona("JP", 24, 1000611715)
persona.presentarse()
persona.obtener_info_basica()

print("")
print("Prueba clase Empleado")
empleado = Empleado("JP", 25, 1000611715, 4000000, "Desarrollo")
# empleado.trabajar()
empleado.calcular_salario()
empleado.presentarse()

print("")
print("Prueba clase Desarrollador")
desarrollador = Desarrollador(
    "JP", 25, 1000611715, 4000000, "Desarrollo", ["Python", "C++"]
)
desarrollador.trabajar()
desarrollador.calcular_salario()
desarrollador.programar("Platzi")

print("")
print("Prueba clase Gerente")
gerente = Gerente("JP", 25, 1000611715, 4000000, ["Gerencia"], 10)
gerente.trabajar()
gerente.calcular_salario()
gerente.dirigir_reunion("Platzi")

print("")
print("Prueba clase Ventas")
vendedor = Vendedor("JP", 25, 1000611715, 4000000, "Ventas", 1000000)
vendedor.trabajar()
vendedor.calcular_salario()
vendedor.realizar_venta(1)
vendedor.calcular_salario()

print("")
print("Prueba clase Empresa")
empresa = Empresa("Mythbusters")
empresa.contratar_empleado(desarrollador)
empresa.mostrar_empleados()
# empresa.calcular_nomina_total()
empresa.hacer_trabajar_a_todos()
empresa.empleados_por_departamento("Desarrollo")
