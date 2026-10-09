"""Mesa de Soporte TI - MVP (Flask + SQLite)."""
import os
import sqlite3

from flask import (Flask, abort, flash, g, redirect, render_template,
                   request, url_for)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ESTADOS = ["Nuevo", "En proceso", "Resuelto", "Cerrado"]
PRIORIDADES = ["Crítica", "Alta", "Media", "Baja"]


def create_app(database=None):
    app = Flask(__name__)
    app.config["DATABASE"] = database or os.path.join(BASE_DIR, "mesa.db")
    app.config["SECRET_KEY"] = "dev-mesa-soporte"

    def get_db():
        if "db" not in g:
            g.db = sqlite3.connect(app.config["DATABASE"])
            g.db.row_factory = sqlite3.Row
            g.db.execute("PRAGMA foreign_keys = ON")
        return g.db

    @app.teardown_appcontext
    def close_db(_exc):
        db = g.pop("db", None)
        if db is not None:
            db.close()

    def init_db():
        db = sqlite3.connect(app.config["DATABASE"])
        with open(os.path.join(BASE_DIR, "schema.sql"), encoding="utf-8") as f:
            db.executescript(f.read())
        db.commit()
        db.close()

    init_db()
    app.jinja_env.filters["codigo"] = lambda i: f"TCK-{int(i):04d}"

    # ---------- Listado + filtros + resumen (RF-03, RF-05, RF-06) ----------
    @app.route("/")
    def index():
        db = get_db()
        estado = request.args.get("estado", "")
        prioridad = request.args.get("prioridad", "")
        categoria = request.args.get("categoria", "")
        sql = """SELECT t.*, c.nombre AS categoria, u.nombre AS responsable
                 FROM tickets t JOIN categorias c ON c.id = t.categoria_id
                 LEFT JOIN usuarios u ON u.id = t.responsable_id WHERE 1=1"""
        params = []
        if estado in ESTADOS:
            sql += " AND t.estado = ?"; params.append(estado)
        if prioridad in PRIORIDADES:
            sql += " AND t.prioridad = ?"; params.append(prioridad)
        if categoria.isdigit():
            sql += " AND t.categoria_id = ?"; params.append(int(categoria))
        tickets = db.execute(sql + " ORDER BY t.id DESC", params).fetchall()
        conteo = {e: 0 for e in ESTADOS}
        for r in db.execute("SELECT estado, COUNT(*) n FROM tickets GROUP BY estado"):
            conteo[r["estado"]] = r["n"]
        categorias = db.execute("SELECT * FROM categorias ORDER BY nombre").fetchall()
        return render_template("index.html", tickets=tickets, conteo=conteo,
                               total=sum(conteo.values()), categorias=categorias,
                               estados=ESTADOS, prioridades=PRIORIDADES,
                               f_estado=estado, f_prioridad=prioridad,
                               f_categoria=categoria)

    # ---------- Registro (RF-01, RF-02) ----------
    @app.route("/tickets/nuevo", methods=["GET", "POST"])
    def nuevo():
        db = get_db()
        categorias = db.execute("SELECT * FROM categorias ORDER BY nombre").fetchall()
        if request.method == "POST":
            f = {k: request.form.get(k, "").strip() for k in
                 ("solicitante", "titulo", "descripcion", "categoria", "prioridad")}
            errores = []
            if len(f["solicitante"]) < 2: errores.append("Indique el solicitante.")
            if len(f["titulo"]) < 5: errores.append("El título debe tener al menos 5 caracteres.")
            if len(f["descripcion"]) < 10: errores.append("La descripción debe tener al menos 10 caracteres.")
            if f["prioridad"] not in PRIORIDADES: errores.append("Prioridad no válida.")
            cat_ok = f["categoria"].isdigit() and db.execute(
                "SELECT 1 FROM categorias WHERE id=?", (int(f["categoria"]),)).fetchone()
            if not cat_ok: errores.append("Categoría no válida.")
            if errores:
                return render_template("nuevo.html", categorias=categorias, errores=errores,
                                       f=f, prioridades=PRIORIDADES), 400
            cur = db.execute(
                "INSERT INTO tickets (solicitante,titulo,descripcion,categoria_id,prioridad)"
                " VALUES (?,?,?,?,?)",
                (f["solicitante"], f["titulo"], f["descripcion"], int(f["categoria"]), f["prioridad"]))
            db.commit()
            flash(f"Solicitud TCK-{cur.lastrowid:04d} registrada.")
            return redirect(url_for("detalle", ticket_id=cur.lastrowid))
        return render_template("nuevo.html", categorias=categorias, errores=[], f={},
                               prioridades=PRIORIDADES)

    def cargar_ticket(ticket_id):
        t = get_db().execute(
            """SELECT t.*, c.nombre AS categoria, u.nombre AS responsable
               FROM tickets t JOIN categorias c ON c.id=t.categoria_id
               LEFT JOIN usuarios u ON u.id=t.responsable_id WHERE t.id=?""",
            (ticket_id,)).fetchone()
        if t is None:
            abort(404)
        return t

    # ---------- Detalle (RF-04) ----------
    @app.route("/tickets/<int:ticket_id>")
    def detalle(ticket_id):
        t = cargar_ticket(ticket_id)
        db = get_db()
        usuarios = db.execute("SELECT * FROM usuarios ORDER BY nombre").fetchall()
        historial = db.execute("SELECT * FROM historial WHERE ticket_id=? ORDER BY id DESC",
                               (ticket_id,)).fetchall()
        return render_template("detalle.html", t=t, usuarios=usuarios,
                               historial=historial, estados=ESTADOS)

    @app.route("/tickets/<int:ticket_id>/actualizar", methods=["POST"])
    def actualizar(ticket_id):
        t = cargar_ticket(ticket_id)
        db = get_db()
        estado = request.form.get("estado", "")
        resp = request.form.get("responsable", "")
        if estado not in ESTADOS:
            abort(400, "Estado no válido.")
        resp_id = None
        if resp:
            if not resp.isdigit() or not db.execute(
                    "SELECT 1 FROM usuarios WHERE id=?", (int(resp),)).fetchone():
                abort(400, "Responsable no válido.")
            resp_id = int(resp)
        if estado != t["estado"]:
            db.execute("INSERT INTO historial (ticket_id,campo,valor_anterior,valor_nuevo)"
                       " VALUES (?,?,?,?)", (ticket_id, "estado", t["estado"], estado))
        if resp_id != t["responsable_id"]:
            nombre = lambda i: (db.execute("SELECT nombre FROM usuarios WHERE id=?", (i,)).fetchone() or [None])[0] if i else "Sin asignar"
            db.execute("INSERT INTO historial (ticket_id,campo,valor_anterior,valor_nuevo)"
                       " VALUES (?,?,?,?)",
                       (ticket_id, "responsable", nombre(t["responsable_id"]), nombre(resp_id)))
        db.execute("UPDATE tickets SET estado=?, responsable_id=? WHERE id=?",
                   (estado, resp_id, ticket_id))
        db.commit()
        flash("Solicitud actualizada.")
        return redirect(url_for("detalle", ticket_id=ticket_id))

    # ---------- Manejo de errores (CAL-01) ----------
    @app.errorhandler(400)
    @app.errorhandler(404)
    @app.errorhandler(500)
    def error(e):
        code = getattr(e, "code", 500)
        msg = {404: "No encontramos lo que busca.", 400: getattr(e, "description", "Solicitud inválida."),
               500: "Error interno. Intente nuevamente."}.get(code, "Error.")
        return render_template("error.html", code=code, msg=msg), code

    return app


if __name__ == "__main__":
    create_app().run(debug=True)
