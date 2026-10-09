# Mesa de Soporte TI (MVP)
Sistema web liviano para registrar y controlar solicitudes de soporte TI. Python + Flask + SQLite.

## Ejecución
```
pip install -r requirements.txt
python app.py            # http://127.0.0.1:5000  (crea mesa.db desde schema.sql)
python -m unittest tests.test_app -v
```
## Estructura
`app.py` (rutas y validaciones) · `schema.sql` (BD + datos base) · `templates/` (interfaz) · `tests/` (pruebas) · `datos_prueba.sql` (datos de ejemplo) · `Documentos/Minutas/Hitos/` (H1, H2, H3, H4, Final)

## Requisitos cubiertos
Prioridades: Crítica, Alta, Media, Baja. Si ya existe una `mesa.db` anterior, bórrela y vuelva a ejecutar.

Datos de ejemplo: `sqlite3 mesa.db < datos_prueba.sql` (una sola vez).

RF-01/02 `/tickets/nuevo` · RF-03 `/` · RF-04 `/tickets/<id>` · RF-05 filtros en `/` · RF-06 tarjetas de resumen · BD-01 `schema.sql` · CAL-01 validaciones, errores 400/404/500 y pruebas.
