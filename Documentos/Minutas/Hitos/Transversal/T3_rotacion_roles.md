# Rotación de roles del equipo de 2 integrantes (desglose por hito)
**Base (enunciado):** cada integrante debe ejercer, al menos una vez antes del cierre, los tres roles. El rol define quién responde por el resultado del hito, pero el otro integrante puede colaborar. Las decisiones de arquitectura las propone Solución y Desarrollo, las revisa Datos/Calidad/Pruebas y las valida el Líder.

**Adaptación a 2 personas:** un integrante ejerce dos roles por hito (Líder + Datos). Quien tiene Desarrollo no tiene Datos, así nadie se revisa a sí mismo.

| Hito | Fecha | Líder y Control + Datos, Calidad y Pruebas | Solución y Desarrollo |
|---|---|---|---|
| H1 | 29-09 | Iván Peña | Yanci Arizmendi |
| H2 | 30-09 | Yanci Arizmendi | Iván Peña |
| H3 | 06-10 | Iván Peña | Yanci Arizmendi |
| H4 | 07-10 | Conjunta | Conjunta |
| Final | 13-10 | Conjunta | Conjunta |

## H1 · 29-09 – Inicio y planificación
- **Iván (Líder):** tablero creado y con backlog inicial, roles asignados, minuta de hito, cronograma preliminar, alcance v0.1 y 6–10 historias.
- **Iván (Datos):** modelo de datos conceptual.
- **Yanci (Desarrollo):** repositorio creado con la estructura inicial, boceto de interfaz y de arquitectura, elección y justificación del stack.
- **Revisión cruzada:** Iván revisa el boceto de arquitectura de Yanci y valida alcance, recursos y plazo.
- **Evidencia:** captura del tablero + enlace al repo + minuta.

## H2 · 30-09 – Línea base
- **Yanci (Líder):** alcance v1.0, backlog priorizado, EDT, recursos, horas, estimación financiera, cronograma y fechas; tablero actualizado.
- **Yanci (Datos):** modelo ER, script inicial (`schema.sql`) y plan de pruebas inicial.
- **Iván (Desarrollo):** wireframes y arquitectura preliminar; revisión del esqueleto del repositorio.
- **Revisión cruzada:** Yanci revisa wireframes y arquitectura de Iván.
- **Evidencia:** tablero actualizado + diagrama ER + planificación v1.0 (no se entrega ese día; alimenta los capítulos 5, 6 y 8).
- **Traspaso H1→H2** al inicio.

## H3 · 06-10 – MVP funcional v0.1
- **Yanci (Desarrollo):** MVP con persistencia y RF-01 a RF-04, interfaces integradas, commits propios.
- **Iván (Datos):** pruebas funcionales iniciales, datos de prueba, registro de defectos.
- **Iván (Líder):** avance planificado vs. real, riesgos y bloqueos, Reporte de Avance N.º 1, captura del tablero.
- **Colaboración obligatoria:** Iván también hace commits (p. ej. RF-03 y las pruebas) para que ambos tengan participación visible en GitHub.
- **Evidencia:** demo parcial + Reporte N.º 1 + captura del tablero + evidencia de pruebas y defectos (capítulos 9, 10 y 12).
- **Traspaso H2→H3** al inicio.

## H4 · 07-10 – Integración, QA y control (conjunta)
- **Ambos:** RF-05 y RF-06, integración completa, pruebas funcionales y de integración, correcciones, análisis de un cambio/imprevisto, cierre de pendientes.
- **Reparto sugerido:** Iván RF-05 y retest; Yanci RF-06 y ejecución de pruebas del código de Iván (QA cruzada).
- **Evidencia:** MVP v0.9 + registro del cambio + Reporte N.º 2 + matriz de pruebas (capítulos 10, 11 y 12).
- **Traspaso H3→H4** al inicio.

## Final · 13-10 – Entrega completa (conjunta)
- **Ambos:** MVP v1.0, tablero final, repositorio, informe, anexos, matriz de rotación validada, presentación y demo. Cada uno presenta la mitad de la presentación y explica los roles que ejerció.

## Cumplimiento de la regla de los tres roles
| Integrante | Líder y Control | Solución y Desarrollo | Datos, Calidad y Pruebas |
|---|---|---|---|
| Iván Peña | H1, H3 | H2 | H1, H3 |
| Yanci Arizmendi | H2 | H1, H3 | H2 |
