from flask import Blueprint

# blueprint con la api rest de la aplicacion
api = Blueprint('api', __name__)

from . import views
