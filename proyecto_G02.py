# Dominio - Reserva Natural
"""
Vamos a comentar primero lo que hacemos para poder descricir bien en el readme lo que hicimos
"""

# Modulo OO
# Entidad Base
class Especie: 
    def __init__(self): 
        pass
    
    # Minimo de 5 métodos
    def __str__(self): 
        return "Especie: " + self.nombre

    def __repr__(self): 
        return self.__str__()

# SubClase Especializada
class EspecieEnPeligro(Especie): 
    def __init__(self): 
        super().__init__()

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

def menu_principal(): 
    # El menú opera sobre una instancia de "EspecieEnPeligro. Al iniciarse el programa solicita al usuario el nombre y la especialización de la colección". Debe ofrecer al menos 7 opciones
    pass


# Reflexion Comparativa
"""
1. Comparen el método agregar() de la ColeccionEspecializada con agregar_libro() del TPI 
2. ¿Qué ganaron con la encapsulación en objeto? 
3. ¿Qué decisión de diseño fue la más difícil en su dominio? ¿Por qué la tomaron así? 
4. ¿Qué parte del módulo funcional resultó más natural trabajar sobre objetos en lugar de 
diccionarios? 
"""