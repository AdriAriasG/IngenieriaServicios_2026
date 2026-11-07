# importo la funcion create_app desde la carpeta app
from app import create_app
import os

# el modo de despliegue viene de una variable de entorno (por defecto production)
modo = os.getenv("DEPLOYMENT_MODE", "production")
app = create_app(modo)
