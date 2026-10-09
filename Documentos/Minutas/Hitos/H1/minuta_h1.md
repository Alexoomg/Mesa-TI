# Minuta de Hito H1 · Inicio y planificación
**Proyecto:** Mesa de Soporte TI · **Fecha de la reunión:** 29/09/2026  · **Herramientas:** GitHub Projects + repositorio Git

## 1. Asistentes y roles del hito
| Integrante | Rol en H1 |
|---|---|
| Iván Peña | Líder de Proyecto y Control |
| Yanci Arizmendi | Solución y Desarrollo |
| Michael Mejía | Datos, Calidad y Pruebas |

## 2. Problema y objetivo
**Problema:** la organización recibe solicitudes de soporte TI por correo, mensajería y conversaciones informales, sin trazabilidad de responsable, prioridad, estado ni tiempos.

**Objetivo:** construir un MVP web que permita registrar y controlar una solicitud desde su creación hasta su cierre, con persistencia en base de datos relacional y evidencia de planificación y control.

## 3. Alcance v0.1
**Incluye:** registro de tickets; ID y fecha automáticos; listado; asignación de responsable; cambio de estado (Nuevo, En proceso, Resuelto, Cerrado); filtros; resumen; BD relacional; validaciones; pruebas funcionales.

**Excluye:** login y roles de seguridad, notificaciones por correo, SLA automáticos, adjuntos, reportes exportables, despliegue en la nube, diseño responsive avanzado.

## 4. Historias / requisitos (9)
| ID | Historia | Prioridad |
|---|---|---|
| HU-01 (RF-01) | Como solicitante, registro una solicitud con título, descripción, categoría y prioridad | Alta |
| HU-02 (RF-02) | Como sistema, genero ID único y fecha de creación | Alta |
| HU-03 (RF-03) | Como técnico, listo solicitudes viendo estado, prioridad y responsable | Alta |
| HU-04 (RF-04) | Como líder de soporte, asigno responsable y cambio el estado | Alta |
| HU-05 (RF-05) | Como técnico, filtro por estado, prioridad o categoría | Media |
| HU-06 (RF-06) | Como jefatura, veo el total y la cantidad por estado | Media |
| HU-07 (BD-01) | Como organización, quiero datos permanentes (usuarios, tickets, categorías, cambios) | Alta |
| HU-08 (CAL-01) | Como usuario, recibo mensajes claros ante datos inválidos o errores | Alta |
| HU-09 (CAL-01) | Como equipo, dejo evidencia de pruebas funcionales | Alta |

## 5. Decisiones tomadas
- Stack: Python + Flask + SQLite (simple, sin servidor de BD, ejecutable en cualquier PC del equipo).
- Control: GitHub Projects (Kanban) + repositorio Git en la misma organización/cuenta.
- Rotación de roles según matriz del documento.

## 6. Cronograma preliminar
| Fecha | Hito | Entregable principal |
|---|---|---|
| 29-09 | H1 | Tablero, repo, minuta, alcance v0.1 |
| 30-09 | H2 | Línea base: EDT, costos, ER, wireframes, plan de pruebas |
| 06-10 | H3 | MVP v0.1 (RF-01 a RF-04) + Reporte de Avance 1 |
| 07-10 | H4 | MVP v0.9 (RF-05/06) + cambio + Reporte de Avance 2 |
| 13-10 | Final | MVP v1.0, informe, demo |

## 7. Modelo de datos conceptual
<img width="331" height="762" alt="Captura de pantalla 2026-09-30 120515" src="https://github.com/user-attachments/assets/2cb7e9f2-85fd-4d66-b6c7-32b428c9c4ca" />
(Diagrama Modelo de datos)




## 8. Boceto inicial de arquitectura e interfaz
Navegador → Flask (rutas + validaciones) → SQLite. Pantallas: Listado con filtros y resumen, Nuevo ticket, Detalle/actualización. 
# Wireframes
## W1 · Listado (`/`)
```
[Mesa de Soporte TI]                 [Tickets] [+ Nuevo ticket]
 Total | Nuevo | En proceso | Resuelto | Cerrado   (tarjetas)
 Estado [v]  Prioridad [v]  Categoría [v]  [Filtrar] [Limpiar]
 ID       | Título | Categoría | Prioridad | Estado | Responsable | Creado
 TCK-0001 | ...    | Redes     | Alta      | Nuevo  | —           | ...
```
## W2 · Nuevo ticket (`/tickets/nuevo`)
```
 Solicitante [____]   Título [____]   Descripción [________]
 Categoría [v]   Prioridad [v]   [Registrar]      (errores en rojo arriba)
```
## W3 · Detalle (`/tickets/<id>`)
```
 TCK-0001 · Título        Solicitante · Categoría · Prioridad · Fecha
 Descripción
 Estado [v]  Responsable [v]  [Guardar cambios]
 Historial: fecha — Ticket creado / Estado: Nuevo → En proceso ...
```

## 9. Evidencia adjunta

<img width="1599" height="899" alt="Captura de pantalla 2026-09-30 113545" src="https://github.com/user-attachments/assets/64b29ef8-fb2c-486b-8ca5-9c58268a329a" />
(Captura inicial del tablero)



## 10. Riesgos iniciales
| Riesgo | Acción |
|---|---|
| Poco tiempo de desarrollo | Alcance mínimo y stack simple |
| Commits desiguales entre integrantes | Repartir tareas y commits por rol y hito |
| Tablero desactualizado | Actualizar estados el mismo día de cada avance |

## 11. Traspaso a H2 (plantilla)
Terminado: ______ · En curso: ______ · Bloqueado: ______ · Evidencia: ______ · Decisión que continúa: ______
