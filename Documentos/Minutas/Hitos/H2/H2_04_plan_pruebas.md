# Plan de pruebas (inicial H2, ejecutado en H3/H4)
**Alcance:** RF-01 a RF-06, BD-01, CAL-01. **Tipos:** funcional (automatizada con `unittest`) e integración (manual). **Criterio de aceptación:** todos los casos Alta en estado Aprobado, sin defectos críticos abiertos.

| ID | Requisito | Caso | Resultado esperado | Tipo | Estado |
|---|---|---|---|---|---|
| CP-01 | RF-01/02 | Registrar ticket válido | Se guarda, ID TCK-0001 y fecha automática | Auto | Aprobado |
| CP-02 | CAL-01 | Título vacío | Error 400 con mensaje | Auto | Aprobado |
| CP-03 | CAL-01 | Prioridad inválida | Error 400 | Auto | Aprobado |
| CP-04 | RF-03 | Listar tickets | Muestra estado, prioridad y responsable | Auto | Aprobado |
| CP-05 | RF-04/BD-01 | Cambiar estado y responsable | Se actualiza y queda en historial | Auto | Aprobado |
| CP-06 | RF-05 | Filtrar por prioridad y categoría | Solo coincidencias | Auto | Aprobado |
| CP-07 | RF-06 | Resumen total y por estado | Conteos correctos | Auto | Aprobado |
| CP-08 | CAL-01 | Ticket inexistente | Error 404 | Auto | Aprobado |
| CP-09 | BD-01 | Reiniciar app y revisar datos | Los tickets persisten | Manual | Pendiente |
| CP-10 | Integración | Flujo completo Nuevo→En proceso→Resuelto→Cerrado | Cada paso visible en detalle e historial | Manual | Pendiente |
| CP-11 | RF-05 | Combinar filtros estado+prioridad+categoría | Resultado de la intersección | Manual | Pendiente |
| CP-12 | CAL-01 | Intentar `<script>` en el título | Se muestra como texto, sin ejecutarse | Manual | Pendiente |
| CP-13 | UI | Revisión visual en navegador (3 pantallas) | Pantallas coinciden con wireframes | Manual | Pendiente |

Los 8 casos automáticos se ejecutaron el día de la preparación (8/8 OK). Los manuales se registran en `H3_02_evidencia_pruebas.md`. Defectos: tarjeta en el tablero con etiqueta `defecto`, luego retest.
