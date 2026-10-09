import os, sys, tempfile, unittest
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from app import create_app

VALIDO = dict(solicitante="Ana Pérez", titulo="No enciende el PC",
              descripcion="El equipo no enciende desde ayer", categoria="1", prioridad="Alta")


class MesaTest(unittest.TestCase):
    def setUp(self):
        fd, self.path = tempfile.mkstemp(suffix=".db"); os.close(fd)
        self.app = create_app(self.path); self.c = self.app.test_client()

    def tearDown(self):
        os.remove(self.path)

    def crear(self, **kw):
        d = dict(VALIDO); d.update(kw)
        return self.c.post("/tickets/nuevo", data=d)

    def test_01_crear_ticket_valido(self):          # CP-01 RF-01/02
        r = self.crear()
        self.assertEqual(r.status_code, 302)
        self.assertIn("/tickets/1", r.headers["Location"])
        self.assertIn("TCK-0001", self.c.get("/tickets/1").get_data(as_text=True))

    def test_02_titulo_vacio_rechazado(self):       # CP-02 CAL-01
        self.assertEqual(self.crear(titulo="").status_code, 400)

    def test_03_prioridad_invalida(self):           # CP-03 CAL-01
        self.assertEqual(self.crear(prioridad="Urgente").status_code, 400)

    def test_04_listado_muestra_ticket(self):       # CP-04 RF-03
        self.crear()
        html = self.c.get("/").get_data(as_text=True)
        self.assertIn("No enciende el PC", html); self.assertIn("Sin asignar", html)

    def test_05_actualizar_y_historial(self):       # CP-05 RF-04 / BD-01
        self.crear()
        r = self.c.post("/tickets/1/actualizar", data=dict(estado="En proceso", responsable="1"))
        self.assertEqual(r.status_code, 302)
        html = self.c.get("/tickets/1").get_data(as_text=True)
        self.assertIn("En proceso", html); self.assertIn("Iván Peña", html)
        self.assertIn("Sin asignar", html)  # valor anterior en el historial

    def test_06_filtros(self):                      # CP-06 RF-05
        self.crear(titulo="Ticket alta uno", prioridad="Alta")
        self.crear(titulo="Ticket baja dos", prioridad="Baja", categoria="3")
        html = self.c.get("/?prioridad=Baja").get_data(as_text=True)
        self.assertIn("Ticket baja dos", html); self.assertNotIn("Ticket alta uno", html)
        html = self.c.get("/?categoria=1").get_data(as_text=True)
        self.assertIn("Ticket alta uno", html); self.assertNotIn("Ticket baja dos", html)

    def test_07_resumen_por_estado(self):           # CP-07 RF-06
        self.crear(); self.crear(titulo="Segundo ticket")
        self.c.post("/tickets/2/actualizar", data=dict(estado="Cerrado", responsable=""))
        html = self.c.get("/").get_data(as_text=True)
        self.assertIn("Total<b>2</b>", html); self.assertIn("Cerrado<b>1</b>", html)

    def test_08_ticket_inexistente_404(self):       # CP-08 CAL-01
        self.assertEqual(self.c.get("/tickets/999").status_code, 404)


    def test_09_prioridad_critica(self):            # CP-14 CAM-01
        r = self.crear(prioridad="Crítica", titulo="Servidor caído total")
        self.assertEqual(r.status_code, 302)
        self.assertIn("Crítica", self.c.get("/tickets/1").get_data(as_text=True))

    def test_10_filtro_critica(self):               # CP-15 CAM-01 + RF-05
        self.crear(prioridad="Crítica", titulo="Servidor caído total")
        self.crear(prioridad="Baja", titulo="Cambiar mouse viejo")
        html = self.c.get("/?prioridad=Crítica").get_data(as_text=True)
        self.assertIn("Servidor caído total", html); self.assertNotIn("Cambiar mouse viejo", html)


if __name__ == "__main__":
    unittest.main()
