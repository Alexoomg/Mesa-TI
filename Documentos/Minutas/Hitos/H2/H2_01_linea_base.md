# H2 – Línea base del proyecto (v1.0)
**Fecha:** 30-09 · **Líder de Proyecto y Control:** Yanci Arizmendi · **Datos, Calidad y Pruebas:** Yanci Arizmendi · **Solución y Desarrollo:** Iván Peña

## 1. Alcance v1.0
**Incluye:** RF-01 a RF-06, BD-01, CAL-01; interfaz web de 3 pantallas; historial de cambios; pruebas automatizadas y manuales.
**Excluye:** login, correo, SLA, adjuntos, reportes avanzados. Todo cambio al alcance se registra como tarjeta en el tablero con su impacto.
**MVP (foco):** flujo completo registrar → listar → asignar → cambiar estado → cerrar, con persistencia.

## 2. Backlog priorizado
| # | Tarea | Prioridad | Hito | Est. (h) |
|---|---|---|---|---|
| 1 | Script BD (schema.sql) | Alta | H2 | 3 |
| 2 | RF-01/02 Registrar ticket | Alta | H3 | 4 |
| 3 | RF-03 Listar tickets | Alta | H3 | 3 |
| 4 | RF-04 Cambiar estado y responsable | Alta | H3 | 4 |
| 5 | Validaciones y errores (CAL-01) | Alta | H3 | 3 |
| 6 | RF-05 Filtros | Media | H4 | 3 |
| 7 | RF-06 Resumen | Media | H4 | 3 |
| 8 | Plan de pruebas y casos | Alta | H2 | 6 |
| 9 | Ejecutar QA y registrar defectos | Alta | H3-H4 | 6 |
| 10 | Reportes de avance 1 y 2 | Media | H3-H4 | 6 |
| 11 | Análisis del cambio/imprevisto | Media | H4 | 4 |
| 12 | Informe final y presentación | Alta | Final | 12 |

## 3. EDT (70 h)
| Código | Paquete de trabajo | Horas |
|---|---|---|
| **1** | **Gestión del proyecto** | **16** |
| 1.1 | Planificación y alcance | 4 |
| 1.2 | Tablero y seguimiento | 4 |
| 1.3 | Reportes de avance | 4 |
| 1.4 | Gestión de cambios y riesgos | 4 |
| **2** | **Diseño** | **10** |
| 2.1 | Arquitectura | 3 |
| 2.2 | Wireframes | 3 |
| 2.3 | Modelo ER | 4 |
| **3** | **Desarrollo** | **20** |
| 3.1 | Script de BD | 3 |
| 3.2 | RF-01/02 Registro | 4 |
| 3.3 | RF-03 Listado | 3 |
| 3.4 | RF-04 Estado y responsable | 4 |
| 3.5 | RF-05 Filtros | 3 |
| 3.6 | RF-06 Resumen | 3 |
| **4** | **Calidad y pruebas** | **12** |
| 4.1 | Plan de pruebas | 3 |
| 4.2 | Casos y datos de prueba | 3 |
| 4.3 | Ejecución QA | 4 |
| 4.4 | Retest | 2 |
| **5** | **Documentación y cierre** | **12** |
| 5.1 | Informe final | 8 |
| 5.2 | Presentación y demo | 4 |
| | **Total** | **70** |

## 4. Recursos
**Humanos:** 2 integrantes (Iván Peña y Yanci Arizmendi) con rotación de roles en cada hito (matriz abajo). **Técnicos:** Python 3, Flask, SQLite, Git/GitHub, GitHub Projects, Draw.io (Diagramas y recursos graficos); equipos personales.

## 5. Estimación financiera (supuesto: valor hora $8.000 CLP, editable)
| Ítem | Cálculo | Monto CLP |
|---|---|---|
| Mano de obra | 70 h × $8.000 | 560.000 |
| Herramientas (todas gratuitas) | | 0 |
| Contingencia 10% | | 56.000 |
| **Total** | | **616.000** |

## 6. Cronograma
| Fecha | Hito | Entregable |
|---|---|---|
| 29-09 | H1 | Tablero, repo, minuta, alcance v0.1 |
| 30-09 | H2 | Línea base, ER, wireframes, plan de pruebas |
| 06-10 | H3 | MVP v0.1 (RF-01 a RF-04), Reporte N.º 1 |
| 07-10 | H4 | RF-05/06, QA, cambio/imprevisto, Reporte N.º 2 |
| 13-10 | Final | MVP v1.0, informe, presentación |

## 7. Arquitectura preliminar
Presentación (Jinja2 en `templates/`) → Lógica (Flask, `app.py`: rutas, validaciones, errores) → Datos (SQLite, `schema.sql`). Revisión cruzada: propone Desarrollo, revisa Datos/Calidad, valida el Líder (alcance, recursos, plazo).

## 8. Plan de pruebas inicial
Ver `H2_04_plan_pruebas.md`.

## 9. Matriz de rotación
| Fecha | Líder y Control | Solución y Desarrollo | Datos, Calidad y Pruebas |
|---|---|---|---|
| 29-09 | Iván Peña | Yanci Arizmendi | Iván Peña |
| 30-09 | Yanci Arizmendi | Iván Peña | Yanci Arizmendi |
| 06-10 | Iván Peña | Yanci Arizmendi | Iván Peña |
| 07-10 | Conjunta | Conjunta | Conjunta |

### Distribución de horas planificadas por integrante (35 h cada uno)
| Paquete | Iván Peña | Yanci Arizmendi |
|---|---|---|
| 1 Gestión (16 h) | 8 | 8 |
| 2 Diseño (10 h): arquitectura, wireframes, ER | 5 (arquitectura 2, wireframes 3) | 5 (arquitectura 1, ER 4) |
| 3 Desarrollo (20 h) | 9 (RF-03, RF-05, RF-06) | 11 (script BD, RF-01/02, RF-04) |
| 4 Calidad y pruebas (12 h) | 7 (casos y datos 3, ejecución 2, retest 2) | 5 (plan 3, ejecución 2) |
| 5 Documentación y cierre (12 h) | 6 | 6 |
| **Total** | **35 h** | **35 h** |
Costo por integrante: 35 h × $8.000 = $280.000 CLP (sin contingencia).

## 10. Evidencias a adjuntar
Captura del tablero actualizado + PNG del diagrama ER + este documento (v1.0).
