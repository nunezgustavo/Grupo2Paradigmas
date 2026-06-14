# Dominio - Reserva Natural
"""
Vamos a comentar primero lo que hacemos para poder descricir bien en el readme lo que hicimos
"""

# Modulo OO
# Entidad Base
class Especie: 
    categorias_validas = ["en peligro", "vulnerable", "extinta"]

    def __init__(self, nombre, categoria): 
        self.nombre = nombre
        self.categoria = categoria # En Peligro - Vulnerable - Extinta
        self.estudiada = False
    
    # Minimo de 5 métodos
    def __str__(self): 
        return f"Especie: {self.nombre} - Categoría: {self.categoria}"

    def __repr__(self): 
        return self.__str__()

    def categoria_valida(self):
        while True:
            if self.categoria.lower() in self.categorias_validas:
                return True
            print("Categoría no válida.")
            self.categoria = input("Ingrese la categoría de la especie válida (En Peligro - Vulnerable - Extinta): ")
    
    def es_activa(self):
        # Retorna True si la especie cumple la condición principal del dominio (por ejemplo, si está en peligro), False en caso contrario
        pass

    def resumen(self):
        # Retorna un string que resume la información de la especie
        pass

    def __lt__(self, other):
        # Define el criterio de ordenamiento por nombre de la especie
        return self.nombre < other.nombre
    
    def __eq__(self, other):
        # Define la igualdad entre especies por su nombre
        return self.nombre == other.nombre
    

# SubClase Especializada
class EspecieEnPeligro(Especie):
    def __init__(self, nombre, especializacion): 
        # super().__init__(nombre, categoria)
        self.nombre = nombre
        self.especializacion = especializacion
        self.especies = {}

    def __str__(self): 
        return "Colección: " + self.nombre + " - Especialización: " + self.especializacion

    def __repr__(self): 
        return self.__str__()
    
    # Agregar item
    def agregar_especie(self): 
        # Agrega una especie de la clase Especie a la colección especializada
        nombre = input("Ingrese el nombre de la especie: ")
        categoria = input("Ingrese la categoría de la especie (En Peligro - Vulnerable - Extinta): ")
        especie = Especie(nombre, categoria)
        especie.categoria_valida()
        self.especies[nombre] = especie
        print("Especie agregada correctamente.")
        return True
    
    # Mostrar todos los ítems
    def mostrar_especies(self): 
        # Muestra todas las especies en la colección especializada
        for especie in self.especies.values():
            print(especie)
        return True

    # Buscar por atributo principal
    def buscar_especie(self, nombre): 
        # Busca una especie por su nombre y retorna la instancia o None si no se encuentra
        especie = self.especies.get(nombre)
        if especie:
            print(especie)
            return True
        else:
            print("Especie no encontrada.")
            return True

    # Filtar por categoría
    def filtar_por_categoria(self, categoria): 
        # Retorna una lista de especies que pertenecen a una categoría específica usando filter() y lambda
        categoria = categoria.lower().strip()
        while categoria not in Especie.categorias_validas:
            print("Categoría no válida. Opciones válidas: " + ", ".join(Especie.categorias_validas))
            categoria = input("Ingrese la categoría a filtrar (En Peligro - Vulnerable - Extinta): ").lower().strip()

        especies_filtadas = list(filter(lambda especie: especie.categoria.lower() == categoria, self.especies.values()))
        if especies_filtadas:
            print("Especies encontradas en la categoría '" + categoria + "':")
            for especie in especies_filtadas:
                print(f"- {especie.nombre} | Categoría: {especie.categoria} | Estudiada: {'Sí' if especie.estudiada else 'No'}")
        else:
            print("No se encontraron especies en la categoría especificada.")
        return True

    # Marcar ítem como procesado / activo / visitado (según dominio)
    def marcar_estudiada(self, nombre): 
        # Marca una especie como estudiada por su nombre, actualizando el atributo correspondiente
        especie = self.especies.get(nombre)
        if especie is None:
            print("No se encontró la especie para marcar.")
        else:
            especie.estudiada = True
            print(f"La especie '{nombre}' fue marcada como estudiada.")
        return True

    # Ver estadísticas
    def estadisticas(self): 
        # Retorna un resumen estadístico de la colección especializada, como el número total de especies, cuántas están estudiadas, etc.
        total = len(self.especies)
        estudiadas = sum(1 for especie in self.especies.values() if especie.estudiada)
        print(f"Total de especies: {total}")
        print(f"Especies estudiadas: {estudiadas}")
        return True

    def ejecutar_modulo_funcional(self): 
        # Permite ejecutar el módulo funcional desde la instancia de la clase, mostrando un menú con las opciones disponibles
        pass

# Módulo funcional
def item_activos(coleccion): 
    # Retorna lista de ítems que cumplen la condición principal del dominio usando filter() y map()
    pass

def resumen_coleccion(coleccion): 
    # Genera un string que resumen por ítem usando map() y una función lambda o auxiliar
    pass

def items_ordenados(coleccion): 
    # Retorna la lista ordenada por el criterio dado usando sorted() con key=lambda
    pass

def iterar_opcion(coleccion, opcion): 
    try:
        opcion = int(opcion)
    except ValueError:
        print("Opción no válida. Por favor, seleccione una opción del 1 al 7.")
        return True

    match opcion:
        case 1:
            # Agregar ítem
            return coleccion.agregar_especie()
        case 2:
            # Mostrar ítems
            return coleccion.mostrar_especies()
        case 3:
            # Buscar por atributo principal
            return coleccion.buscar_especie(input("Ingrese el nombre de la especie a buscar: "))
        case 4:
            # Filtrar por categoría
            return coleccion.filtar_por_categoria(input("Ingrese la categoría a filtrar: "))
        case 5:
            # Marcar ítem como procesado / activo / visitado (según dominio)
            return coleccion.marcar_estudiada(input("Ingrese el nombre de la especie a marcar como estudiada: "))
        case 6:
            # Ver estadísticas
            return coleccion.estadisticas()
        case 7:
            # Salir
            return False
        case _:
            print("Opción no válida. Por favor, seleccione una opción del 1 al 7.")
            return True

def menu_principal(): 
    # El menú opera sobre una instancia de "EspecieEnPeligro. Al iniciarse el programa solicita al usuario el nombre y la especialización de la colección". Debe ofrecer al menos 7 opciones
    print("Bienvenido al sistema de gestión de especies en peligro")
    print("Por favor, ingrese el nombre de la colección especializada:")
    # nombre_coleccion = input()
    nombre_coleccion = "Colección de Especies en Peligro"
    print("Por favor, ingrese la especialización de la colección:")
    # especializacion = input()
    especializacion = "Especies en Peligro"
    EP = EspecieEnPeligro(nombre_coleccion, especializacion)
    print("Colección especializada creada: " + str(EP))
    while True: 
        print("\nMenú de opciones:")
        print("1. Agregar especie\n2. Mostrar especies\n3. Buscar especie\n4. Filtrar por categoría\n5. Marcar especie como estudiada\n6. Ver estadísticas\n7. Salir")
        opcion = input("Seleccione una opción: ")   
        resultado = iterar_opcion(EP, opcion)
        if not resultado: 
            break

menu_principal()

# Reflexion Comparativa
"""
1. Comparen el método agregar() de la ColeccionEspecializada con agregar_libro() del TPI 
2. ¿Qué ganaron con la encapsulación en objeto? 
3. ¿Qué decisión de diseño fue la más difícil en su dominio? ¿Por qué la tomaron así? 
4. ¿Qué parte del módulo funcional resultó más natural trabajar sobre objetos en lugar de 
diccionarios? 
"""