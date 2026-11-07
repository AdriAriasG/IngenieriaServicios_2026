from flask import Blueprint

# blueprint con las metricas de la aplicacion para prometheus
metrics = Blueprint("metrics", __name__)

from app.metrics import views
