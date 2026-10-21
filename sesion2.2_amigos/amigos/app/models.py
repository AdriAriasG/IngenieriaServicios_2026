from app import db

class Amigo(db.Model):
    "definicion de la tabla 'amigos' de la base de datos"
    __tablename__ = "amigos"

    # columnas de la tabla y sus tipos
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32), unique=True)
    longi = db.Column(db.String(32))
    lati = db.Column(db.String(32))
    # dispositivo del amigo (ejercicio 7.1), vacio por defecto
    device = db.Column(db.Text())

    # como se muestra un amigo si lo imprimo desde python
    def __repr__(self):
        return "<Amigo[{}]: {}>".format(self.id, self.name)
