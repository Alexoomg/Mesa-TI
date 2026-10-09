# Reporte de Avance N.º 1 – Hito H3 (MVP funcional v0.1)
**Período:** 29-09 al 06-10 · **Líder de Proyecto y Control (H3):** Michael Mejía · **Desarrollo:** Iván Peña · **Datos/Calidad/Pruebas:** Yanci Arizmendi
**Repositorio:** <URL> · **Tablero:** <URL> · **Fecha de emisión:** __/__/____ (fecha real)

## 1. Resumen
El MVP v0.1 está operativo: registra, guarda en SQLite, lista y actualiza estado/responsable (RF-01 a RF-04). Además ya se adelantaron RF-05 y RF-06, y las validaciones básicas (CAL-01).

## 2. Planificado vs. real
| Entregable | Planificado | Real | Horas plan | Horas reales | Desvío |
|---|---|---|---|---|---|
| Línea base (H2) | 30-09 | Completar | 20 | completar | completar |
| RF-01/02 Registro | 06-10 | Completo (código + prueba) | 4 | completar | completar |
| RF-03 Listado | 06-10 | Completo | 3 | completar | completar |
| RF-04 Estado y responsable | 06-10 | Completo | 4 | completar | completar |
| Validaciones y errores | 06-10 | Completo | 3 | completar | completar |
| Pruebas funcionales iniciales | 06-10 | 8 casos automáticos aprobados | 4 | completar | completar |
| RF-05 / RF-06 | 07-10 (H4) | Adelantados en código; falta validarlos en QA integrado | 6 | completar | Adelanto |

Las horas reales y fechas de cierre deben salir del historial del tablero: no estimarlas ahora.

## 3. Aporte por integrante (commits)
| Integrante | Rol en H3 | Commits / archivos aportados |
|---|---|---|
| Iván Peña | Solución y Desarrollo | completar (p. ej. app.py, templates/) |
| Yanci Arizmendi | Datos, Calidad y Pruebas | completar (p. ej. tests/, plan de pruebas) |
| Michael Mejía | Líder y Control | completar (p. ej. docs/, README) |

Requisito H3: los tres deben tener commits propios en GitHub.

## 4. Defectos, riesgos y bloqueos
| ID | Tipo | Descripción | Causa | Acción | Estado |
|---|---|---|---|---|---|
| R-01 | Riesgo | Poco tiempo para QA integrado antes del 13-10 | Calendario corto | Priorizar casos de prioridad Alta | Abierto |
| R-02 | Riesgo | Commits desbalanceados entre integrantes | Código generado en bloque | Repartir commits por archivo/tarea | Abierto |
| D-01 | Defecto | Registrar aquí cualquier fallo real encontrado en la demo | | | |

Debe existir al menos una tarjeta Bloqueado/Riesgo en el tablero con causa y acción.

## 5. Decisiones
- Mantener Flask + SQLite sin autenticación (fuera de alcance).
- Adelantar RF-05/06 porque el costo era bajo; se valida en H4.

## 6. Próximos pasos (H4 07-10)
Validar RF-05/06, pruebas de integración, análisis del cambio/imprevisto, Reporte N.º 2, cerrar pendientes.
