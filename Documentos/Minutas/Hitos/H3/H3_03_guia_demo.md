# Guía de demo parcial (≈5 min)
1. Abrir terminal: `pip install -r requirements.txt` y `python app.py`; abrir http://127.0.0.1:5000 (aplicación abierta).
2. **Registrar ticket:** "Nueva solicitud" → Solicitante "Ana Pérez", Título "No tengo internet", Descripción "Sin red en oficina 3", Categoría Red, Prioridad Alta → Registrar. Se ve el ID TCK-0001.
3. **Guardado en BD:** mostrar el archivo `mesa.db` (o `sqlite3 mesa.db "select * from tickets;"`).
4. **Listar:** volver a "Solicitudes"; se ve el ticket con "Sin asignar".
5. **Asignar responsable y cambiar estado:** abrir TCK-0001 → Estado "En proceso", Responsable "Yanci Arizmendi" → Guardar. Mostrar el historial.
6. **Validación:** intentar registrar con título vacío y mostrar el error.
7. (Bonus) Filtros y tarjetas de resumen.
8. Mostrar el tablero, los commits de los 3 integrantes y las pruebas (`python -m unittest tests.test_app -v`).
**Quién habla:** Líder (H3) presenta avance planificado vs. real; Desarrollo hace la demo; Datos/Calidad muestra pruebas y defectos.
