# Registro de cambio / imprevisto – CAM-01 (H4)
**Fecha de registro:** __/__/____ (fecha real) · **Registrado por:** Líder de Proyecto y Control · **Origen:** [indicar si fue una solicitud real o un escenario simulado por el equipo para el hito]

## 1. Descripción
Se solicita agregar el nivel de prioridad **Crítica** (incidentes que detienen la operación) además de Alta, Media y Baja.

## 2. Análisis de impacto
| Dimensión | Impacto |
|---|---|
| Alcance | Se agrega un valor al campo prioridad: base de datos (CHECK), validación, formularios y filtro. No cambia ningún RF. |
| Cronograma | Sin desplazamiento de fechas; se absorbe dentro de H4 (07-10). La entrega final del 13-10 se mantiene. |
| Horas | +3 h (BD y validación 1 h, pruebas 1 h, documentación 1 h) |
| Costo | +3 h × $8.000 = **$24.000 CLP**, cubierto por la contingencia ($56.000 → quedan $32.000) |
| Calidad | 2 casos de prueba nuevos (CP-14, CP-15) y regresión completa |
| Riesgo | Una `mesa.db` creada antes del cambio conserva la restricción antigua: hay que borrarla y regenerarla (en el MVP los datos son de prueba, recreables con `datos_prueba.sql`). |

## 3. Decisión (revisión cruzada)
Propone: Solución y Desarrollo · Revisa: Datos, Calidad y Pruebas · Valida (alcance, recursos, plazo): Líder de Proyecto y Control.
**Resultado: aprobado y replanificado dentro de H4.** Alcance v1.0 actualizado a **v1.1** (4 niveles de prioridad).

## 4. Acciones realizadas
1. `schema.sql`: restricción de prioridad incluye 'Crítica'.
2. `app.py`: lista de prioridades actualizada (formulario, filtro y validación).
3. `tests/test_app.py`: `test_09` y `test_10`. Resultado: 10/10 pruebas aprobadas.
4. Tablero: tarjeta CAM-01 con etiqueta `cambio` movida a Hecho; tareas afectadas marcadas `Replanificada` si corresponde.

## 5. Estado
Cerrado tras retest. Commit asociado: <enlace al commit>.
