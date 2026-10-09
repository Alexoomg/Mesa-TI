# Matriz de pruebas – H4
| ID | Requisito | Caso | Tipo | Resultado | Evidencia |
|---|---|---|---|---|---|
| CP-01 | RF-01/02 | Registrar ticket válido | Auto | Aprobado | Captura de `unittest` |
| CP-02 | CAL-01 | Título vacío → 400 | Auto | Aprobado | idem |
| CP-03 | CAL-01 | Prioridad inválida → 400 | Auto | Aprobado | idem |
| CP-04 | RF-03 | Listado con estado, prioridad y responsable | Auto | Aprobado | idem |
| CP-05 | RF-04 / BD-01 | Cambiar estado/responsable e historial | Auto | Aprobado | idem |
| CP-06 | RF-05 | Filtros por prioridad y categoría | Auto | Aprobado | idem |
| CP-07 | RF-06 | Resumen total y por estado | Auto | Aprobado | idem |
| CP-08 | CAL-01 | Ticket inexistente → 404 | Auto | Aprobado | idem |
| CP-09 | BD-01 | Persistencia tras reiniciar | Script / Manual | Aprobado por script; repetir manual | Captura pendiente |
| CP-10 | Integración | Flujo Nuevo→Cerrado | Script / Manual | Aprobado por script; repetir manual | Captura pendiente |
| CP-11 | RF-05 | Filtros combinados | Script / Manual | Aprobado por script; repetir manual | Captura pendiente |
| CP-12 | CAL-01 | Entrada `<script>` escapada | Script / Manual | Aprobado por script; repetir manual | Captura pendiente |
| CP-13 | UI | Pantallas vs. wireframes | Manual | Pendiente | Captura pendiente |
| CP-14 | CAM-01 | Registrar prioridad Crítica | Auto | Aprobado | Captura de `unittest` |
| CP-15 | CAM-01/RF-05 | Filtrar por Crítica | Auto | Aprobado | idem |

**Resumen:** 10 pruebas automáticas aprobadas (10/10). Defectos abiertos: ninguno registrado (completar si aparecen). Retest: pendiente de defectos.
Comando: `python -m unittest tests.test_app -v`
