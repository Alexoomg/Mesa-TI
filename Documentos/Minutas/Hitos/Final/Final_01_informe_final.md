# Mesa de Soporte TI – Informe Final (borrador completo)
> Reemplazar los textos entre [corchetes] con datos reales. Para entregar: exportar a PDF o DOCX (sugerido 12–18 páginas sin portada, índice ni anexos).

## 1. Portada e identificación del equipo
Evaluación 3 – Mesa de Soporte TI · Integrantes: Iván Peña, Yanci Arizmendi, Michael Mejía · Curso/Docente: [completar] · Fecha de entrega: 13-10 · Repositorio: [URL] · Tablero: [URL]

## 2. Resumen ejecutivo
Se desarrolló un sistema web liviano (Python + Flask + SQLite) para registrar y controlar solicitudes de soporte TI, reemplazando correo y mensajería informal. El MVP cubre RF-01 a RF-06, persistencia relacional (BD-01) y validaciones y pruebas (CAL-01). El proyecto se gestionó en GitHub Projects con 4 hitos, rotación de roles y un cambio controlado (prioridad Crítica). Resultado: MVP v1.0 con 10 pruebas automáticas aprobadas, [N] tareas cerradas y [N] horas reales sobre 70 estimadas.

## 3. Problema, objetivo y alcance
**Problema:** requerimientos de TI llegan por correo, mensajería y conversaciones, sin trazabilidad de responsable, prioridad, estado ni tiempos.
**Objetivo:** MVP que demuestre el flujo completo de una solicitud, desde su registro hasta su cierre, con evidencia de planificación y control.
**Alcance incluido:** registrar, listar, filtrar, asignar responsable, cambiar estado, resumen y historial. **Excluido:** autenticación, notificaciones, SLA, adjuntos, reportes avanzados.

## 4. Requisitos y criterios de aceptación
| ID | Requisito | Criterio de aceptación | Caso |
|---|---|---|---|
| RF-01 | Registrar solicitud | Se guarda con solicitante, título, descripción, categoría y prioridad válidos | CP-01 |
| RF-02 | ID y fecha | ID TCK-0001 incremental y fecha automática | CP-01 |
| RF-03 | Listar | Muestra estado, prioridad y responsable | CP-04 |
| RF-04 | Actualizar | Cambia estado (4 valores) y responsable; queda historial | CP-05, CP-10 |
| RF-05 | Filtrar | Por estado, prioridad o categoría | CP-06, CP-11 |
| RF-06 | Resumen | Total y conteo por estado | CP-07 |
| BD-01 | Persistencia | 4 tablas relacionales; datos persisten | CP-09 |
| CAL-01 | Calidad | Validaciones, errores 400/404/500, pruebas | CP-02, CP-03, CP-08 |

## 5. Planificación: actividades, hitos y cronograma
EDT de 5 paquetes y 70 h (gestión 16, diseño 10, desarrollo 20, calidad 12, documentación 12). Hitos: H1 29-09, H2 30-09, H3 06-10, H4 07-10, Final 13-10. Detalle en `H2_01_linea_base.md`. Replanificación: CAM-01 absorbido en H4 sin mover la fecha final. [Agregar tabla cronograma plan vs. real.]

## 6. Recursos humanos, técnicos y económicos
Humanos: 3 integrantes con rotación. Técnicos: Python, Flask, SQLite, Git/GitHub, GitHub Projects, mermaid.live. Económicos (supuesto $8.000/h): mano de obra $560.000 + contingencia $56.000 = **$616.000 CLP**; herramientas $0. CAM-01 consumió $24.000 de la contingencia. [Agregar costo real según horas reales.]

## 7. Organización del equipo y rotación de roles
| Fecha | Líder y Control | Solución y Desarrollo | Datos, Calidad y Pruebas |
|---|---|---|---|
| 29-09 | Iván Peña | Yanci Arizmendi | Michael Mejía |
| 30-09 | Yanci Arizmendi | Michael Mejía | Iván Peña |
| 06-10 | Michael Mejía | Iván Peña | Yanci Arizmendi |
| 07-10 | Conjunta | Conjunta | Conjunta |
Cada integrante ejerció los tres roles. Traspasos en `T1_traspasos.md`. Matriz validada en `Final_03_matriz_rotacion.md`.

## 8. Diseño de solución
**Arquitectura en 3 capas:** plantillas Jinja2 (presentación) → Flask en `app.py` (rutas, validaciones, errores) → SQLite con `schema.sql` (datos). Decisión: stack simple, sin servidor de BD, instalación con un `pip install`, adecuado al plazo. Revisión cruzada: propone Desarrollo, revisa Datos/Calidad, valida el Líder.
**Interfaces:** listado con filtros y resumen, nueva solicitud, detalle con historial (wireframes en `H2_03_wireframes.md`; [insertar capturas reales]).
**Modelo de datos:** usuarios, categorias, tickets, historial (ER en `H2_02_modelo_ER.md`; [insertar PNG]).

## 9. Herramienta de control y evolución del tablero
GitHub Projects (Kanban) con columnas Backlog, Por hacer, En curso, En revisión/pruebas, Hecho, Bloqueado y campos Prioridad, Fecha objetivo, Estimación, Hito y Evidencia. [Insertar capturas H1, H2, H3, H4 y vista final con terminadas, pendientes y descartadas/replanificadas; describir cómo evolucionó.]

## 10. Reportes de avance
Reporte N.º 1 (H3) y N.º 2 (H4): `H3_01_reporte_avance_1.md`, `H4_02_reporte_avance_2.md`. [Resumir planificado vs. real, bloqueos (R-01, R-02, R-03) y decisiones.]

## 11. Cambio/imprevisto del H4 y tratamiento
CAM-01: nueva prioridad Crítica. Impacto: +3 h, +$24.000, sin cambio de fecha final; alcance v1.0 → v1.1. Aprobado con revisión cruzada y verificado con CP-14 y CP-15. Detalle en `H4_01_registro_cambio.md`.

## 12. Calidad y pruebas
15 casos: 10 automáticos aprobados (10/10), 4 verificados por script y por repetir a mano, 1 visual pendiente. Matriz en `H4_03_matriz_pruebas.md`. Defectos: [listar con ID, causa, corrección y retest; si no hubo, indicarlo]. Pendientes: [completar al 13-10].

## 13. Conclusiones y lecciones aprendidas
[Redactar con experiencia real. Ideas: valor de actualizar el tablero a diario; un stack simple permitió llegar al MVP; la rotación de roles mostró la importancia de los traspasos; el cambio CAM-01 evidenció el valor de la contingencia.]

## 14. Referencias
Flask Documentation (flask.palletsprojects.com) · SQLite Documentation (sqlite.org) · GitHub Docs: Projects · Enunciado de la Evaluación 3.

## 15. Anexos
A. Capturas del tablero por hito · B. Enlaces al repositorio y tablero · C. `schema.sql` y `datos_prueba.sql` · D. Registro de commits por integrante · E. Capturas de pruebas · F. Wireframes e interfaz final · G. Contribución por rol.
