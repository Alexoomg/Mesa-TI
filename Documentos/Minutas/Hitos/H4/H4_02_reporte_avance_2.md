# Reporte de Avance N.º 2 – Hito H4 (Integración, QA y control)
**Período:** 06-10 al 07-10 · **Trabajo conjunto de los dos integrantes (Iván Peña y Yanci Arizmendi)** · **Fecha de emisión:** 12/10/2026

## 1. Resumen
Se integró el producto completo (RF-01 a RF-06), se ejecutó la regresión (10/10 pruebas automáticas aprobadas) y se gestionó el cambio CAM-01 (prioridad Crítica). El producto queda en **versión v0.9** para cerrar pendientes antes del 13-10.

## 2. Planificado vs. real
| Entregable | Planificado | Real | Horas plan | Horas reales | Desvío |
|---|---|---|---|---|---|
| RF-05 Filtros | H4 | Completo y probado (CP-06, CP-11) | 3 | completar | completar |
| RF-06 Resumen | H4 | Completo y probado (CP-07) | 3 | completar | completar |
| Integración y QA | H4 | Regresión 10/10; manuales por repetir con captura | 6 | completar | completar |
| Cambio CAM-01 | No planificado | Implementado y probado | 0 | 3 (est.) | +3 h, cubierto por contingencia |
| Reporte N.º 2 y matriz de pruebas | H4 | Este documento + `H4_03_matriz_pruebas.md` | 3 | completar | completar |
Las horas reales deben salir del tablero.

## 3. Riesgos, defectos y bloqueos
| ID | Tipo | Descripción | Acción | Estado |
|---|---|---|---|---|
| R-01 | Riesgo | Poco tiempo para QA integrado | Priorizar casos Alta y repetir los manuales hoy | En seguimiento |
| R-02 | Riesgo | Commits desbalanceados | Cada integrante sube sus archivos con su cuenta | En seguimiento |
| R-03 | Riesgo | `mesa.db` antigua rechaza 'Crítica' | Borrar `mesa.db` y regenerar | Mitigado (documentado) |
| R-04 | Riesgo | Equipo reducido a 2 integrantes | Horas redistribuidas (35 h c/u), roles rotados con revisión cruzada | En seguimiento |
| D-xx | Defecto | Registrar aquí cualquier defecto real hallado | | |

## 4. Decisiones del período
- Aprobar CAM-01 y pasar el alcance a v1.1 sin mover la fecha final.
- Mantener sin autenticación ni notificaciones (fuera de alcance).
