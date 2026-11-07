from . import health
from .. import db

@health.route("/health")
def health_check():
    "compruebo que la app responde y que puede hablar con la base de datos"
    try:
        # una consulta minima basta para saber si mariadb contesta
        db.session.execute(db.text("SELECT 1"))
        return {"status": "ok", "database": "ok"}, 200
    except Exception:
        # sin base de datos el servicio no se considera sano: 503
        return {"status": "error", "database": "error"}, 503
