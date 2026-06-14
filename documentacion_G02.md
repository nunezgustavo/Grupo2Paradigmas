# Grupo 2 — Documentación Técnica

> Estado del documento: se actualizó con base en el archivo Python actual. Las partes ya implementadas en `proyecto_G02.py` se indican como completadas; las que aún no están terminadas se marcan como "falta completar".

# Documentación Técnica — Proyecto Final
## Paradigmas de la Programación · FP-UNA · 2026

---

## Carátula

| Campo            | Valor                                                  |
|------------------|--------------------------------------------------------|
| **Dominio**      | Reserva Natural    |
| **Grupo**        | G02     |
| **Integrantes**  | Ñunez Gustavo · Maidana Jose · Portillo Elias |
| **Fecha**        | Mayo 2026                                              |
| **Docente**      | Prof. Lic. Gustavo Galeano                             |
| **Materia**      | Paradigmas de la Programación (Código 4.2)             |

---

## 1. Descripción del sistema

### ¿Qué hace el sistema?

El sistema permite administrar una colección de especies en peligro desde la
consola. El usuario puede:

- Registrar especies con categoría válida. ✅ completado
- Mostrar todas las especies registradas. ✅ completado
- Buscar una especie por nombre. ✅ completado
- Filtrar especies por categoría. ✅ completado
- Marcar una especie como estudiada. ✅ completado
- Ver estadísticas básicas de la colección. ✅ completado
- Ejecutar el módulo funcional. falta completar ❌

### ¿Qué problema resuelve?

La reserva natural necesita registrar y consultar especies con una categoría
válida, sin perder información sobre qué especies ya fueron estudiadas.
Este sistema centraliza el registro y facilita la revisión rápida de la
colección. falta completar ❌

---

## 2. Decisiones de diseño

### ¿Por qué esta jerarquía de clases?

La jerarquía implementada en `proyecto_G02.py` usa:

1. `Especie` para representar cada especie individual. ✅ completado
2. `EspecieEnPeligro` para gestionar la colección especializada. ✅ completado
3. Validación de categoría mediante `categoria_valida()`. ✅ completado

La idea de diseño fue separar la entidad individual (`Especie`) de la
colección (`EspecieEnPeligro`), porque las operaciones de búsqueda, filtrado
estadísticas pertenecen a la colección, no a cada especie por separado.

Esta estructura permitió que la categoría se valide al momento de registrar
cada especie, y que la colección mantenga el estado de todas las especies
registradas. Las funciones auxiliares del módulo funcional aún están pendientes. falta completar ❌

### ¿Se consideraron alternativas?

Sí. Otra opción era guardar todo en listas o diccionarios sueltos, pero eso
hubiera dificultado la validación y el mantenimiento. Con clases, cada especie
conoce su propia categoría y estado de estudio, y la colección centraliza las
operaciones sobre ese conjunto.

---

## 3. Diagrama UML de clases

> **Instrucción:** Reemplazar este bloque con una imagen del diagrama generado
> en draw.io u otra herramienta. El texto ASCII a continuación es solo para
> ilustrar la estructura antes de que el diagrama esté terminado.

```
┌──────────────────────────────────────┐
│             <<clase>>                  │
│               Especie                  │
├──────────────────────────────────────┤
│ + nombre : str                         │
│ + categoria : str                      │
│ + estudiada : bool                     │
├──────────────────────────────────────┤
│ + categoria_valida() : bool            │
│ + es_activa() : bool      falta completar ❌ │
│ + resumen() : str         falta completar ❌ │
│ + __str__() : str                      │
│ + __repr__() : str                     │
└──────────────────────────────────────┘
              ▲  1..*
              │  (composición)
┌─────────────┴──────────────────────────┐
│             <<clase>>                  │
│        EspecieEnPeligro                │
├──────────────────────────────────────┤
│ + nombre : str                         │
│ + especializacion : str                │
│ + especies : dict                      │
├──────────────────────────────────────┤
│ + agregar_especie() : bool             │
│ + mostrar_especies() : bool            │
│ + buscar_especie(nombre) : bool        │
│ + filtrar_por_categoria(cat) : bool   │
│ + marcar_estudiada(nombre) : bool      │
│ + estadisticas() : bool                │
│ + ejecutar_modulo_funcional() : falta completar ❌ │
└──────────────────────────────────────┘
```

**Cómo leer el diagrama:**
- `▲ 1..*` indica que `EspecieEnPeligro` contiene varias instancias de
  `Especie`.
- La validación de categoría ocurre dentro de `Especie` y se usa al registrar
  cada nueva especie.

---

## 4. Descripción de clases y funciones públicas

### Clase `Especie` ✅ completado

Representa una especie individual dentro de la colección.

| Elemento                          | Tipo / Retorno | Descripción                                               |
|-----------------------------------|---------------|-----------------------------------------------------------|
| `nombre`                          | `str`         | Nombre de la especie                                      |
| `categoria`                       | `str`         | Categoría de conservación (`en peligro`, `vulnerable`, `extinta`) |
| `estudiada`                       | `bool`        | Indica si ya fue marcada como estudiada                   |
| `categoria_valida()`              | `bool`        | Valida que la categoría ingresada sea correcta             |
| `es_activa()`                     | `bool`        | falta completar ❌                                        |
| `resumen()`                       | `str`         | falta completar ❌                                        |
| `__lt__()` / `__eq__()`            | `bool`        | Comparación por nombre de especie                         |

### Clase `EspecieEnPeligro` ✅ completado

Gestiona la colección completa de especies en peligro.

| Elemento                          | Tipo / Retorno         | Descripción                                       |
|-----------------------------------|------------------------|---------------------------------------------------|
| `nombre`                          | `str`                  | Nombre descriptivo de la colección                |
| `especializacion`                 | `str`                  | Especialización o contexto de la colección        |
| `especies`                        | `dict`                 | Diccionario con las especies registradas          |
| `agregar_especie()`               | `bool`                 | Agrega una especie validando la categoría         |
| `mostrar_especies()`              | `bool`                 | Muestra todas las especies registradas             |
| `buscar_especie(nombre)`          | `bool`                 | Busca una especie por nombre                      |
| `filtrar_por_categoria(cat)`      | `bool`                 | Filtra por categoría usando `filter()`             |
| `marcar_estudiada(nombre)`        | `bool`                 | Marca una especie como estudiada                   |
| `estadisticas()`                  | `bool`                 | Muestra total y especies estudiadas                |
| `ejecutar_modulo_funcional()`     | `None`                 | falta completar ❌                                  |

### Funciones del módulo funcional

- `item_activos(coleccion)`: falta completar ❌
- `resumen_coleccion(coleccion)`: falta completar ❌
- `items_ordenados(coleccion)`: falta completar ❌

### Métodos pendientes en la clase `Especie`

- `es_activa()`: falta completar ❌
- `resumen()`: falta completar ❌

### Métodos pendientes en la clase `EspecieEnPeligro`

- `ejecutar_modulo_funcional()`: falta completar ❌

| Elemento                          | Tipo / Retorno         | Descripción                                                 |
|-----------------------------------|------------------------|-------------------------------------------------------------|
| `ambiente`                        | `str`                  | Ambiente de la colección (Baño, Oficina, etc.)              |
| `estadisticas()`                  | `None`                 | Llama a `super().estadisticas()` y agrega estadísticas del ambiente |
| `plantas_para_ambiente()`         | `list[PlantaInterior]` | Filtra plantas adecuadas según el ambiente configurado      |

### Módulo funcional

| Función                           | Retorno         | Herramienta   | Descripción                                      |
|-----------------------------------|-----------------|---------------|--------------------------------------------------|
| `item_activos(coleccion)`         | `list`          | filter + map  | falta completar ❌                                |
| `resumen_coleccion(coleccion)`    | `list[str]`     | map + lambda  | falta completar ❌                                |
| `items_ordenados(coleccion)`      | `list`          | sorted + lambda | falta completar ❌                              |

---

## 5. Instrucciones de ejecución

### Requisitos

- Python 3.8 o superior
- No requiere librerías externas

### Ejecución

```bash
python proyecto_G02.py
```

### Secuencia mínima para probar el sistema

Opciones actualmente disponibles en `proyecto_G02.py`:

1. Agregar especie ✅ completado
2. Mostrar especies ✅ completado
3. Buscar especie ✅ completado
4. Filtrar por categoría ✅ completado
5. Marcar especie como estudiada ✅ completado
6. Ver estadísticas ✅ completado
7. Salir ✅ completado

La parte del módulo funcional aún está pendiente. falta completar ❌

```
Nombre de la colección: Colección de Especies en Peligro
Especialización: Especies en Peligro

[Opción 1] Agregar especie:
  Nombre: Lobo
  Categoría: en peligro

[Opción 4] Filtrar por categoría:
  Categoría: en peligro

[Opción 6] Ver estadísticas
[Opción 7] Salir
```

---

## 6. Reflexión comparativa

*(Esta sección puede referenciar los comentarios al final del archivo .py)*

La reflexión completa se encuentra en los comentarios del archivo actual
`proyecto_G02.py`. A continuación un resumen adaptado al dominio real del
proyecto:

**Comparación con el enfoque anterior:**
La diferencia central es que ahora el estado de la colección vive dentro de
`self.especies`, y la validación de categoría se realiza dentro de la clase.
Eso hace que el programa sea más ordenado y evita errores de ingreso.

**Decisión de diseño más difícil:**
Validar la categoría hasta recibir una opción correcta, sin permitir avanzar
con una entrada inválida. Esa decisión mantiene la lógica consistente.

**Módulo funcional sobre objetos:**
Trabajar con `especie.categoria` y `especie.estudiada` hace que el código
sea legible y fácil de mantener, en lugar de depender de estructuras sueltas.

---

*Fin del documento — Proyecto Final · Paradigmas de la Programación · FP-UNA 2026*
