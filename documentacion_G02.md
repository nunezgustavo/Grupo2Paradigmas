# Documentación Técnica — Proyecto Final
## Paradigmas de la Programación · FP-UNA · 2026

---

## Carátula

| Campo           | Valor                                                   |
|-----------------|---------------------------------------------------------|
| **Dominio**     | Reserva Natural                                         |
| **Grupo**       | G02                                                     |
| **Integrantes** | Ñunez Gustavo · Maidana Josias · Portillo Elias         |
| **Fecha**       | Junio 2026                                              |
| **Docente**     | Prof. Lic. Gustavo Galeano                              |
| **Materia**     | Paradigmas de la Programación (Código 4.2)              |

---

## 1. Descripción del sistema

### ¿Qué hace el sistema?

El sistema permite administrar una colección de especies de una reserva natural
desde la consola. El usuario puede:

- Registrar nuevas especies con sus datos de conservación.
- Consultar qué especies están en estado crítico.
- Filtrar por categoría de conservación.
- Marcar especies como estudiadas.
- Obtener estadísticas de la reserva.
- Generar un plan de conservación para las especies en peligro.
- Ejecutar el módulo funcional para obtener resúmenes y listados ordenados.

### ¿Qué problema resuelve?

Las reservas naturales gestionan colecciones de especies sin herramientas
centralizadas. Este sistema permite registrar y consultar el estado de
conservación de cada especie, identificar rápidamente cuáles están en peligro
crítico y cuáles aún no fueron estudiadas, y generar planes de acción concretos.

---

## 2. Decisiones de diseño

### ¿Por qué esta jerarquía de clases?

Se eligió una jerarquía de tres clases porque el dominio tiene dos niveles
naturales de abstracción:

1. **Especie** encapsula los datos y comportamiento de una especie individual.
   Es natural que cada especie conozca su propia categoría y pueda indicar si
   está activa (en peligro crítico).

2. **Coleccion** centraliza la gestión del conjunto de especies. Se separó del
   concepto de "especie individual" porque las operaciones de búsqueda, filtrado
   y estadísticas son responsabilidad del contenedor, no de cada elemento.

3. **EspecieEnPeligro** extiende la colección con el concepto de
   *población estimada* de la reserva. Se eligió herencia en lugar de
   composición porque `EspecieEnPeligro` *es una* `Coleccion` más específica —
   reutiliza todas sus operaciones base y solo amplía `estadisticas()` con datos
   de la reserva y agrega `plan_conservacion()`.

### ¿Se consideraron alternativas?

Sí. La primera versión del código ponía toda la lógica directamente en
`EspecieEnPeligro` sin una clase `Coleccion` intermedia. Eso mezclaba
responsabilidades: la clase especializada conocía conceptos que debería
delegar. Con la jerarquía final, la clase base permanece genérica y
reutilizable para cualquier tipo de reserva.

---

## 3. Diagrama UML de clases

```
┌─────────────────────────────────────┐
│             <<clase>>               │
│              Especie                │
├─────────────────────────────────────┤
│ + nombre : str                      │
│ + nombre_cientifico : str           │
│ + habitat : str                     │
│ + categoria : str                   │
│ + estudiada : bool                  │
├─────────────────────────────────────┤
│ + es_activa() : bool                │
│ + resumen() : str                   │
│ + marcar_estudiada() : None         │
│ + __str__() : str                   │
│ + __repr__() : str                  │
│ + __lt__() : bool                   │
│ + __eq__() : bool                   │
└─────────────────────────────────────┘
              ▲  1..*
              │  (composición)
┌─────────────┴───────────────────────┐
│             <<clase>>               │
│             Coleccion               │
├─────────────────────────────────────┤
│ + nombre : str                      │
│ + especies : list[Especie]          │
├─────────────────────────────────────┤
│ + agregar(especie) : None           │
│ + buscar_por_nombre(n) : list       │
│ + filtrar_por_categoria(c) : list   │
│ + estadisticas() : None             │
└─────────────────────────────────────┘
              △
              │  (herencia)
┌─────────────┴───────────────────────┐
│             <<clase>>               │
│         EspecieEnPeligro            │
├─────────────────────────────────────┤
│ + poblacion_estimada : int          │
├─────────────────────────────────────┤
│ + estadisticas() [override]         │
│ + plan_conservacion() : None        │
└─────────────────────────────────────┘
```

**Cómo leer el diagrama:**
- `▲ 1..*` indica que `Coleccion` *contiene* una o más instancias de `Especie` (composición).
- `△` indica herencia: `EspecieEnPeligro` *es una* `Coleccion`.
- `[override]` señala que `estadisticas()` sobreescribe el método del padre llamando a `super()`.

---

## 4. Descripción de clases y funciones públicas

### Clase `Especie`

Representa una especie individual dentro de la reserva natural.

| Elemento                | Tipo / Retorno | Descripción                                                    |
|-------------------------|---------------|----------------------------------------------------------------|
| `nombre`                | `str`         | Nombre común de la especie (ej: "Jaguar")                      |
| `nombre_cientifico`     | `str`         | Nombre científico (ej: "Panthera onca")                        |
| `habitat`               | `str`         | Hábitat donde vive la especie                                  |
| `categoria`             | `str`         | Estado de conservación: `en peligro`, `vulnerable`, `extinta`  |
| `estudiada`             | `bool`        | Indica si la especie ya fue relevada por investigadores        |
| `es_activa()`           | `bool`        | Retorna `True` si la categoría es `"en peligro"`               |
| `resumen()`             | `str`         | Línea resumida con nombre, categoría y estado de estudio       |
| `marcar_estudiada()`    | `None`        | Cambia `estudiada` a `True`                                    |

### Clase `Coleccion`

Gestiona la colección general de especies de la reserva.

| Elemento                        | Tipo / Retorno   | Descripción                                        |
|---------------------------------|------------------|----------------------------------------------------|
| `nombre`                        | `str`            | Nombre descriptivo de la colección                 |
| `especies`                      | `list[Especie]`  | Lista de todas las especies registradas            |
| `agregar(especie)`              | `None`           | Agrega una especie; valida el tipo antes de insertar |
| `buscar_por_nombre(nombre)`     | `list[Especie]`  | Búsqueda parcial, case-insensitive                 |
| `filtrar_por_categoria(cat)`    | `list[Especie]`  | Filtra por categoría exacta usando `filter()`      |
| `estadisticas()`                | `None`           | Imprime totales, estudiadas, distribución por categoría |

### Clase `EspecieEnPeligro` *(hereda de `Coleccion`)*

| Elemento                  | Tipo / Retorno | Descripción                                                          |
|---------------------------|---------------|----------------------------------------------------------------------|
| `poblacion_estimada`      | `int`         | Población total estimada en la reserva                               |
| `estadisticas()`          | `None`        | Llama a `super().estadisticas()` y agrega datos de la especialización |
| `plan_conservacion()`     | `None`        | Lista las especies en peligro crítico con su estado de estudio       |

### Módulo funcional

| Función                              | Retorno         | Herramienta      | Descripción                                      |
|--------------------------------------|-----------------|------------------|--------------------------------------------------|
| `items_activos(coleccion)`           | `list[str]`     | filter + map     | Nombres de especies en categoría `"en peligro"`  |
| `resumen_coleccion(coleccion)`       | `list[str]`     | map + lambda     | Una línea de resumen por especie                 |
| `items_ordenados(coleccion, criterio)` | `list[Especie]` | sorted + lambda | Lista ordenada por el atributo indicado          |

---

## 5. Instrucciones de ejecución

### Requisitos

- Python 3.10 o superior (por el uso de `match`)
- No requiere librerías externas

### Ejecución

```bash
python proyecto_G02.py
```

### Secuencia mínima para probar el sistema

```
Nombre de la colección: Reserva Pantanal
Población estimada de la reserva: 1500

[Opción 1] Agregar especie:
  Nombre común: Jaguar
  Nombre científico: Panthera onca
  Hábitat: Selva tropical
  Categoría: en peligro

[Opción 1] Agregar especie:
  Nombre común: Tapir
  Nombre científico: Tapirus terrestris
  Hábitat: Bosque húmedo
  Categoría: vulnerable

[Opción 5] Marcar como estudiada: Jaguar
[Opción 6] Ver estadísticas
[Opción 7] Plan de conservación
[Opción 8] Módulo funcional → a → b → c → nombre
[Opción 9] Salir
```

---

## 6. Reflexión comparativa

*(La reflexión completa con referencias a líneas exactas se encuentra en los comentarios al final de `proyecto_G02.py`)*

**TPI 1 vs Proyecto Final — `agregar()`:**
En TPI 1 el estado vivía en listas globales externas a las funciones. En el
Proyecto Final, `self.especies` pertenece al objeto `Coleccion`, y la
validación de tipo está encapsulada en el método `agregar()`. Esto eliminó una
clase entera de errores posibles: ya no es posible insertar un dato incorrecto
desde afuera.

**Decisión de diseño más difícil:**
Separar `Coleccion` de `EspecieEnPeligro`. La versión inicial ponía todo en
una sola clase. La solución con herencia resultó más limpia: la clase base
quedó genérica y la subclase solo agrega lo propio de su especialización
(`poblacion_estimada` y `plan_conservacion()`).

**Módulo funcional sobre objetos:**
Operar con `e.es_activa()` en lugar de `especie["categoria"] == "en peligro"`
eliminó los posibles `KeyError` y hizo el código más expresivo. Ver
`items_activos()` vs el filtrado manual de TPI 1.

---

*Fin del documento — Proyecto Final · Paradigmas de la Programación · FP-UNA 2026*
