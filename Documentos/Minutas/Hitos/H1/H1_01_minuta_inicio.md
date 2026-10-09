# Minuta de hito H1 – Inicio y planificación
**Fecha de reunión:** __/__/____ (completar con la fecha real) · **Asistentes:** Iván Peña, Yanci Arizmendi, Michael Mejía
**Repositorio:** <URL> · **Tablero:** <URL> · **Captura del tablero:** adjuntar

## Problema y objetivo
La organización recibe requerimientos de TI por correo, mensajería y conversaciones informales, sin trazabilidad de responsable, prioridad, estado ni tiempos.
**Objetivo:** construir un MVP web que registre y controle solicitudes de soporte desde su creación hasta su cierre, con persistencia en base de datos relacional.

## Alcance v0.1
**Incluye:** registrar, listar, asignar responsable, cambiar estado, filtrar y resumir solicitudes; BD relacional; validaciones; pruebas.
**Queda fuera:** autenticación/roles de usuario, notificaciones por correo, SLA automáticos, adjuntos, reportes avanzados.

## Historias / requisitos (8)
1. Como solicitante, registro una solicitud con título, descripción, categoría y prioridad. (RF-01)
2. Como sistema, asigno ID único y fecha de creación. (RF-02)
3. Como técnico, listo solicitudes con estado, prioridad y responsable. (RF-03)
4. Como líder, asigno responsable y cambio el estado (Nuevo, En proceso, Resuelto, Cerrado). (RF-04)
5. Como técnico, filtro por estado, prioridad o categoría. (RF-05)
6. Como líder, veo el total y el conteo por estado. (RF-06)
7. Como equipo, conservo historial de cambios en BD. (BD-01)
8. Como usuario, recibo mensajes claros ante datos inválidos. (CAL-01)

## Modelo de datos conceptual
usuarios 1—N tickets · categorias 1—N tickets · tickets 1—N historial (ver `H2_02_modelo_ER.md`).
## Boceto de arquitectura
Navegador → Flask (rutas + validaciones) → SQLite. Pantallas: listado, nueva solicitud, detalle (ver `H2_03_wireframes.md`).

## Cronograma preliminar
H1 29-09 inicio · H2 30-09 línea base · H3 06-10 MVP v0.1 · H4 07-10 integración/QA · Final 13-10.

## Roles H1
| Rol | Responsable |
|---|---|
| Líder de Proyecto y Control | Iván Peña |
| Solución y Desarrollo | Yanci Arizmendi |
| Datos, Calidad y Pruebas | Michael Mejía |

## Decisiones
- Herramienta de control: GitHub Projects (Kanban) + repositorio Git.
- Stack: Python + Flask + SQLite (simple, un solo `pip install`, sin servidor de BD).
