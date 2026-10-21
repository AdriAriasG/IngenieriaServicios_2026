# secretos de la app: los leo de variables de entorno para no escribirlos en el codigo
import os

# si no existe la variable uso sqlite en memoria (vacia, no sirve para nada real)
SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URI", "sqlite://")
