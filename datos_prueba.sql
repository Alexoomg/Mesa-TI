-- Datos de prueba (ejecutar DESPUÉS de crear la BD con schema.sql; no ejecutar dos veces)
-- Uso:  python app.py  (crea mesa.db)  y luego:  sqlite3 mesa.db < datos_prueba.sql
INSERT INTO tickets (solicitante,titulo,descripcion,categoria_id,prioridad,estado,responsable_id) VALUES
 ('Ana Pérez','No enciende el PC','El equipo no enciende desde ayer',1,'Alta','Nuevo',NULL),
 ('Luis Soto','Sin acceso a correo','No puedo iniciar sesión en el correo',4,'Media','En proceso',2),
 ('Marta Díaz','Internet lento en oficina 3','La red se cae cada hora',3,'Alta','En proceso',1),
 ('Pedro Ruiz','Instalar antivirus','Se requiere instalar antivirus en notebook',2,'Baja','Resuelto',3),
 ('Carla Núñez','Cambiar mouse','El mouse dejó de funcionar',1,'Baja','Cerrado',3),
 ('Jorge Vera','Servidor de archivos caído','Nadie accede a la carpeta compartida',3,'Crítica','Nuevo',NULL);
INSERT INTO historial (ticket_id,campo,valor_anterior,valor_nuevo) VALUES
 (2,'estado','Nuevo','En proceso'),(2,'responsable','Sin asignar','Yanci Arizmendi'),
 (3,'estado','Nuevo','En proceso'),(3,'responsable','Sin asignar','Iván Peña'),
 (4,'estado','Nuevo','Resuelto'),(5,'estado','Nuevo','Cerrado');
