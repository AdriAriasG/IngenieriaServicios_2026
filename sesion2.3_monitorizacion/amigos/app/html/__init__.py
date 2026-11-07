from flask import Blueprint

# blueprint con la vista html de la aplicacion
html = Blueprint('html', __name__)

from . import views
