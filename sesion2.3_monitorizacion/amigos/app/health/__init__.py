from flask import Blueprint

# blueprint con la comprobacion de salud del servicio
health = Blueprint('health', __name__)

from . import views
