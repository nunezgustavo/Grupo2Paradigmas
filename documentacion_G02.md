# Grupo 2 ¡¡Falta modificar el .md con respecto al archivo python!!

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

El sistema permite administrar una colección personal de plantas de interior
desde la consola. El usuario puede:

- Registrar nuevas plantas con sus datos de cuidado.
- Consultar qué plantas requieren atención.
- Filtrar por nivel de luz requerida.
- Obtener estadísticas adaptadas al ambiente de la colección.
- Ejecutar el módulo funcional para obtener resúmenes y listados ordenados.

### ¿Qué problema resuelve?

Los aficionados a las plantas de interior suelen gestionar colecciones grandes
sin ninguna herramienta. Este sistema centraliza el registro y facilita el
mantenimiento al identificar rápidamente qué plantas están enfermas y cuáles
son adecuadas para un ambiente particular (baño, oficina, dormitorio).

---

## 2. Decisiones de diseño

### ¿Por qué esta jerarquía de clases?

Se eligió una jerarquía de tres clases porque el dominio tiene dos niveles
naturales de abstracción:

1. **PlantaInterior** encapsula los datos y comportamiento de una planta
   individual. Era natural que cada planta conociera su propio estado y
   pudiera auto-diagnosticarse.

2. **ColeccionPlantas** centraliza la gestión de la colección. Se separó del
   concepto de "planta individual" porque las operaciones de búsqueda y
   estadística son responsabilidad del contenedor, no del elemento.

3. **ColeccionEspecializada** extiende la colección con el concepto de
   *ambiente*. Se eligió herencia en lugar de composición porque
   ColeccionEspecializada *es una* ColeccionPlantas más específica, no
   *tiene una* — reutiliza todas sus operaciones base y solo amplía
   `estadisticas()` con información del ambiente.

### ¿Se consideraron alternativas?

Sí. Una alternativa era modelar el ambiente como un atributo de
`ColeccionPlantas` directamente, sin herencia. Eso hubiera funcionado para
este tamaño de sistema, pero habría mezclado responsabilidades: la clase base
conocería conceptos propios de una versión especializada. Con herencia, la
clase base permanece genérica y reutilizable.

---

## 3. Diagrama UML de clases

> **Instrucción:** Reemplazar este bloque con una imagen del diagrama generado
> en draw.io u otra herramienta. El texto ASCII a continuación es solo para
> ilustrar la estructura antes de que el diagrama esté terminado.

```
┌────────────────────────────────┐
│          <<clase>>             │
│       PlantaInterior           │
├────────────────────────────────┤
│ + nombre_comun : str           │
│ + nombre_cientifico : str      │
│ + luz_requerida : str          │
│ + frecuencia_riego_dias : int  │
│ + tiene_flor : bool            │
│ + esta_sana : bool             │
├────────────────────────────────┤
│ + diagnostico() : str          │
│ + marcar_enferma() : None      │
│ + recuperar() : None           │
│ + __str__() : str              │
│ + __repr__() : str             │
└────────────────────────────────┘
              ▲  1..*
              │  (composición)
┌─────────────┴──────────────────┐
│          <<clase>>             │
│       ColeccionPlantas         │
├────────────────────────────────┤
│ + nombre : str                 │
│ + plantas : list[PlantaInterior│
├────────────────────────────────┤
│ + agregar(planta) : None       │
│ + buscar_por_nombre(s) : list  │
│ + filtrar_por_luz(n) : list    │
│ + estadisticas() : None        │
└────────────────────────────────┘
              △
              │  (herencia)
┌─────────────┴────────────────────┐
│           <<clase>>              │
│     ColeccionEspecializada       │
├──────────────────────────────────┤
│ + ambiente : str                 │
├──────────────────────────────────┤
│ + estadisticas() [override]      │
│ + plantas_para_ambiente() : list │
└──────────────────────────────────┘
```

**Cómo leer el diagrama:**
- `▲ 1..*` indica que `ColeccionPlantas` *contiene* una o más instancias de
  `PlantaInterior` (composición).
- `△` indica herencia: `ColeccionEspecializada` *es una* `ColeccionPlantas`.
- `[override]` señala que `estadisticas()` sobreescribe el método del padre.

---

## 4. Descripción de clases y funciones públicas

### Clase `PlantaInterior`

Representa una planta de interior individual.

| Elemento                          | Tipo / Retorno | Descripción                                               |
|-----------------------------------|---------------|-----------------------------------------------------------|
| `nombre_comun`                    | `str`         | Nombre coloquial (ej: "Potus", "Suculenta")               |
| `nombre_cientifico`               | `str`         | Nombre científico (ej: "Epipremnum aureum")               |
| `luz_requerida`                   | `str`         | `'alta'`, `'media'` o `'baja'`                            |
| `frecuencia_riego_dias`           | `int`         | Días entre riegos                                         |
| `tiene_flor`                      | `bool`        | Si produce flores                                         |
| `esta_sana`                       | `bool`        | Estado actual de la planta                                |
| `diagnostico()`                   | `str`         | Resumen del estado con datos de cuidado                   |
| `marcar_enferma()`                | `None`        | Cambia `esta_sana` a `False`                              |
| `recuperar()`                     | `None`        | Cambia `esta_sana` a `True`                               |

### Clase `ColeccionPlantas`

Gestiona la colección completa.

| Elemento                          | Tipo / Retorno         | Descripción                                       |
|-----------------------------------|------------------------|---------------------------------------------------|
| `nombre`                          | `str`                  | Nombre descriptivo de la colección                |
| `plantas`                         | `list[PlantaInterior]` | Todas las plantas registradas                     |
| `agregar(planta)`                 | `None`                 | Agrega una planta; valida tipo antes de insertar  |
| `buscar_por_nombre(nombre)`       | `list[PlantaInterior]` | Búsqueda parcial, case-insensitive                |
| `filtrar_por_luz(nivel_luz)`      | `list[PlantaInterior]` | Filtra por nivel de luz exacto                    |
| `estadisticas()`                  | `None`                 | Imprime totales, sanas, flores, riego promedio    |

### Clase `ColeccionEspecializada` *(hereda de `ColeccionPlantas`)*

| Elemento                          | Tipo / Retorno         | Descripción                                                 |
|-----------------------------------|------------------------|-------------------------------------------------------------|
| `ambiente`                        | `str`                  | Ambiente de la colección (Baño, Oficina, etc.)              |
| `estadisticas()`                  | `None`                 | Llama a `super().estadisticas()` y agrega estadísticas del ambiente |
| `plantas_para_ambiente()`         | `list[PlantaInterior]` | Filtra plantas adecuadas según el ambiente configurado      |

### Módulo funcional

| Función                                    | Retorno         | Herramienta   | Descripción                                      |
|--------------------------------------------|-----------------|---------------|--------------------------------------------------|
| `plantas_sanas(coleccion)`                 | `list[str]`     | filter + map  | Nombres de plantas en estado sano                |
| `resumen_coleccion(coleccion)`             | `list[str]`     | map + lambda  | Una línea de resumen por planta                  |
| `plantas_ordenadas(coleccion, criterio)`   | `list[PlantaInterior]` | sorted + lambda | Lista ordenada por el atributo indicado   |

---

## 5. Instrucciones de ejecución

### Requisitos

- Python 3.8 o superior
- No requiere librerías externas

### Ejecución

```bash
python proyecto_G00_ejemplo.py
```

### Secuencia mínima para probar el sistema

```
Nombre de la colección: Mi Jardín Interior
Ambiente: Oficina

[Opción 1] Agregar planta:
  Nombre común: Potus
  Nombre científico: Epipremnum aureum
  Luz requerida: baja
  Frecuencia de riego (días): 7
  ¿Produce flores? (s/n): n

[Opción 1] Agregar planta:
  Nombre común: Orquídea
  Nombre científico: Phalaenopsis amabilis
  Luz requerida: media
  Frecuencia de riego (días): 5
  ¿Produce flores? (s/n): s

[Opción 6] Ver estadísticas
[Opción 7] Módulo funcional → c → frecuencia_riego_dias
[Opción 9] Salir
```

---

## 6. Reflexión comparativa

*(Esta sección puede referenciar los comentarios al final del archivo .py)*

La reflexión completa se encuentra en el bloque de comentarios al final de
`proyecto_G00_ejemplo.py` (líneas ~220 en adelante). A continuación un
resumen:

**TPI 1 vs Proyecto Final — `agregar`:**
La diferencia central es que en TPI 1 el estado vivía fuera de las funciones
(lista global). En el Proyecto Final, `self.plantas` pertenece al objeto, y
la validación del tipo está encapsulada en el método. Esto eliminó una clase
entera de errores posibles.

**Decisión de diseño más difícil:**
Modelar `plantas_para_ambiente()` sin crear una subclase por cada ambiente.
La solución (dict de lambdas) resultó más extensible y menos verbosa.

**Módulo funcional sobre objetos:**
Operar con `p.esta_sana` en lugar de `planta["leido"]` eliminó los KeyError
posibles y hizo el código más expresivo. Ver `plantas_sanas()` vs
`filtrar_por_genero()` del TPI 1.

---

*Fin del documento — Proyecto Final · Paradigmas de la Programación · FP-UNA 2026*
