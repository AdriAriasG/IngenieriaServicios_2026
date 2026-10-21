from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import app_config

# creo el objeto db que conecta con la base de datos
db = SQLAlchemy()

# factoria de aplicaciones: recibe que configuracion quiero usar
def create_app(config_name):
    # la configuracion de instance se lee de la carpeta ./instance
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')

    # conecto la app con la base de datos y activo las migraciones
    db.init_app(app)
    migrate = Migrate(app, db)
    from app import models

    # no defino rutas aqui: monto los blueprints en sus rutas
    from .html import html as html_blueprint
    app.register_blueprint(html_blueprint, url_prefix='/html')
    from .api import api as api_blueprint
    app.register_blueprint(api_blueprint, url_prefix='/api')

    return app
