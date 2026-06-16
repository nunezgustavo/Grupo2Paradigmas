#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Proyecto Final - Paradigmas de la Programación
# Grupo 02 - Dominio: Reserva Natural
# FP-UNA · 2026

# ==============================================================
# MÓDULO OO
# ==============================================================

class Especie:
    """EntidadBase: representa una especie registrada en la reserva natural."""

    categorias_validas = ["en peligro", "vulnerable", "extinta"]

    def __init__(self, nombre, nombre_cientifico, habitat, categoria, estudiada=False):
        self.nombre = nombre
        self.nombre_cientifico = nombre_cientifico
        self.habitat = habitat
        self.categoria = categoria.lower().strip()
        self.estudiada = estudiada

    def __str__(self):
        return (f"{self.nombre} ({self.nombre_cientifico}) | "
                f"Hábitat: {self.habitat} | Categoría: {self.categoria} | "
                f"Estudiada: {'Sí' if self.estudiada else 'No'}")

    def __repr__(self):
        return self.__str__()

    def __lt__(self, other):
        return self.nombre < other.nombre

    def __eq__(self, other):
        return self.nombre == other.nombre

    def es_activa(self):
        """Retorna True si la especie está en la categoría de mayor riesgo."""
        return self.categoria == "en peligro"

    def resumen(self):
        return f"{self.nombre} | Categoría: {self.categoria} | Estudiada: {'Sí' if self.estudiada else 'No'}"

    def marcar_estudiada(self):
        self.estudiada = True


class Coleccion:
    """Gestiona la colección general de especies de la reserva."""

    def __init__(self, nombre):
        self.nombre = nombre
        self.especies = []  # list[Especie]

    def agregar(self, especie):
        if not isinstance(especie, Especie):
            print("Error: solo se pueden agregar instancias de Especie.")
            return
        self.especies.append(especie)
        print(f"Especie '{especie.nombre}' agregada correctamente.")

    def buscar_por_nombre(self, nombre):
        """Búsqueda parcial, case-insensitive."""
        return [e for e in self.especies if nombre.lower() in e.nombre.lower()]

    def filtrar_por_categoria(self, categoria):
        return list(filter(lambda e: e.categoria == categoria.lower().strip(), self.especies))

    def estadisticas(self):
        total = len(self.especies)
        estudiadas = sum(1 for e in self.especies if e.estudiada)
        en_peligro = sum(1 for e in self.especies if e.categoria == "en peligro")
        vulnerables = sum(1 for e in self.especies if e.categoria == "vulnerable")
        extintas = sum(1 for e in self.especies if e.categoria == "extinta")
        print(f"\n--- ESTADÍSTICAS ---")
        print(f"Colección: {self.nombre}")
        print(f"Total de especies: {total}")
        print(f"Estudiadas: {estudiadas} | Sin estudiar: {total - estudiadas}")
        print(f"En peligro: {en_peligro} | Vulnerables: {vulnerables} | Extintas: {extintas}")


class EspecieEnPeligro(Coleccion):
    """Colección especializada con foco en especies en peligro crítico."""

    def __init__(self, nombre, poblacion_estimada):
        super().__init__(nombre)
        self.poblacion_estimada = poblacion_estimada  # int: población total estimada en la reserva

    def estadisticas(self):
        """Extiende las estadísticas base con datos propios de la reserva especializada."""
        super().estadisticas()
        criticas = [e for e in self.especies if e.es_activa()]
        print(f"--- Estadísticas de especialización ---")
        print(f"Población estimada en reserva: {self.poblacion_estimada}")
        print(f"Especies en estado crítico: {len(criticas)}")

    def plan_conservacion(self):
        """Genera un plan de conservación para las especies en peligro crítico."""
        criticas = [e for e in self.especies if e.es_activa()]
        if not criticas:
            print("No hay especies en peligro crítico registradas.")
            return
        print("\n--- PLAN DE CONSERVACIÓN ---")
        for e in criticas:
            estado = "Estudiada" if e.estudiada else "Pendiente de estudio"
            print(f"  - {e.nombre} ({e.nombre_cientifico})")
            print(f"    Hábitat: {e.habitat} | Estado: {estado}")


# ==============================================================
# MÓDULO FUNCIONAL
# ==============================================================

def items_activos(coleccion):
    """Retorna nombres de especies 'en peligro' usando filter() y map()."""
    en_peligro = filter(lambda e: e.es_activa(), coleccion.especies)
    return list(map(lambda e: e.nombre, en_peligro))

def resumen_coleccion(coleccion):
    """Genera un string de resumen por especie usando map() y lambda."""
    return list(map(lambda e: e.resumen(), coleccion.especies))

def items_ordenados(coleccion, criterio):
    """Retorna la lista de especies ordenada por el criterio dado usando sorted() con key=lambda."""
    return sorted(coleccion.especies, key=lambda e: getattr(e, criterio))


# ==============================================================
# MENÚ PRINCIPAL
# ==============================================================

def _pedir_especie():
    """Solicita datos al usuario y retorna una instancia de Especie validada."""
    print("\n--- AGREGAR ESPECIE ---")
    nombre = input("Nombre común: ")
    nombre_cientifico = input("Nombre científico: ")
    habitat = input("Hábitat: ")
    categoria = input("Categoría (en peligro / vulnerable / extinta): ").lower().strip()
    while categoria not in Especie.categorias_validas:
        print(f"Categoría no válida. Opciones: {', '.join(Especie.categorias_validas)}")
        categoria = input("Categoría: ").lower().strip()
    return Especie(nombre, nombre_cientifico, habitat, categoria)


def _menu_funcional(coleccion):
    print("\n--- MÓDULO FUNCIONAL ---")
    print("a. Mostrar especies activas (en peligro)")
    print("b. Resumen de colección")
    print("c. Ordenar por criterio")
    sub = input("Seleccione: ").lower().strip()

    if sub == "a":
        activos = items_activos(coleccion)
        if activos:
            print("Especies en peligro (filter + map):")
            for nombre in activos:
                print(f"  → {nombre}")
        else:
            print("No hay especies en peligro registradas.")
    elif sub == "b":
        resumenes = resumen_coleccion(coleccion)
        if resumenes:
            print("Resumen de colección (map + lambda):")
            for r in resumenes:
                print(f"  → {r}")
        else:
            print("La colección está vacía.")
    elif sub == "c":
        print("Criterios: nombre, nombre_cientifico, habitat, categoria")
        criterio = input("Ordenar por: ").strip()
        if criterio not in ("nombre", "nombre_cientifico", "habitat", "categoria"):
            print("Criterio no válido.")
            return
        ordenadas = items_ordenados(coleccion, criterio)
        print(f"Especies ordenadas por '{criterio}' (sorted + lambda):")
        for e in ordenadas:
            print(f"  → {e.resumen()}")
    else:
        print("Opción no válida.")


def iterar_opcion(coleccion, opcion):
    try:
        opcion = int(opcion)
    except ValueError:
        print("Opción no válida. Ingrese un número del 1 al 9.")
        return True

    match opcion:
        case 1:
            especie = _pedir_especie()
            coleccion.agregar(especie)
        case 2:
            if not coleccion.especies:
                print("La colección está vacía.")
            else:
                for e in coleccion.especies:
                    print(e)
        case 3:
            nombre = input("Nombre a buscar: ")
            resultados = coleccion.buscar_por_nombre(nombre)
            if resultados:
                for e in resultados:
                    print(e)
            else:
                print("No se encontraron especies.")
        case 4:
            categoria = input("Categoría (en peligro / vulnerable / extinta): ").lower().strip()
            resultados = coleccion.filtrar_por_categoria(categoria)
            if resultados:
                for e in resultados:
                    print(e)
            else:
                print("No se encontraron especies en esa categoría.")
        case 5:
            nombre = input("Nombre de la especie a marcar como estudiada: ")
            encontradas = coleccion.buscar_por_nombre(nombre)
            if encontradas:
                encontradas[0].marcar_estudiada()
                print(f"'{encontradas[0].nombre}' marcada como estudiada.")
            else:
                print("Especie no encontrada.")
        case 6:
            coleccion.estadisticas()
        case 7:
            coleccion.plan_conservacion()
        case 8:
            _menu_funcional(coleccion)
        case 9:
            return False
        case _:
            print("Opción no válida. Ingrese un número del 1 al 9.")
    return True


def menu_principal():
    print("=" * 46)
    print("  SISTEMA DE GESTIÓN — PROYECTO FINAL")
    print("  Paradigmas de la Programación · FP-UNA")
    print("=" * 46)
    nombre = input("Nombre de la colección: ")
    while True:
        try:
            poblacion = int(input("Población estimada de la reserva: "))
            break
        except ValueError:
            print("Por favor ingrese un número entero.")
    coleccion = EspecieEnPeligro(nombre, poblacion)
    print(f"\nColección '{nombre}' iniciada.")
    print(f"Población estimada: {poblacion}")
    print("=" * 46)
    while True:
        print("\n--- MENÚ PRINCIPAL ---")
        print("1. Agregar especie")
        print("2. Mostrar todas las especies")
        print("3. Buscar por nombre")
        print("4. Filtrar por categoría")
        print("5. Marcar como estudiada")
        print("6. Ver estadísticas")
        print("7. Plan de conservación")
        print("8. Módulo funcional")
        print("9. Salir")
        opcion = input("Seleccione una opción: ")
        if not iterar_opcion(coleccion, opcion):
            print("¡Hasta pronto!")
            break


menu_principal()


# ==============================================================
# REFLEXIÓN COMPARATIVA
# ==============================================================
#
# 1. agregar() de EspecieEnPeligro vs. agregar_libro() del TPI 1:
#    En TPI 1, agregar_libro() operaba sobre una lista global externa a la función.
#    En el Proyecto Final, agregar() (línea ~55) es un método de Coleccion que
#    opera sobre self.especies, una lista interna del objeto. La validación de tipo
#    con isinstance() queda encapsulada dentro del método, eliminando la posibilidad
#    de insertar datos incorrectos desde afuera. El estado ya no es global: pertenece
#    al objeto y solo él lo gestiona.
#
# 2. Decisión de diseño más difícil:
#    Separar Coleccion (genérica) de EspecieEnPeligro (especializada).
#    La alternativa inicial era poner toda la lógica en una sola clase, que fue
#    lo que hicimos en la primera versión del código. Elegimos herencia porque
#    EspecieEnPeligro ES UNA Coleccion más específica: reutiliza agregar(),
#    buscar_por_nombre() y filtrar_por_categoria() sin cambios, y solo extiende
#    estadisticas() con super() (línea ~83) y agrega plan_conservacion() (línea ~90).
#    Así la clase base queda genérica y reutilizable.
#
# 3. Módulo funcional sobre objetos vs. diccionarios:
#    La función items_activos() (línea ~105) usa e.es_activa() para filtrar.
#    En TPI 1 hubiéramos accedido a especie["categoria"], con riesgo de KeyError
#    si la clave no existía. Con objetos, es_activa() encapsula la condición y
#    el código es más expresivo y seguro. Lo mismo aplica a resumen_coleccion()
#    (línea ~110): e.resumen() es más claro que concatenar manualmente campos
#    de un diccionario.
