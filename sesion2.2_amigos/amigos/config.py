# configuraciones para distintas formas de lanzar la aplicacion

class Config:
    "clase base de la que derivan las demas"
    # valores comunes a todos los entornos
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevelopmentConfig(Config):
    "configuracion de desarrollo"
    DEBUG = True
    # muestro por consola el sql que se envia a la base de datos
    SQLALCHEMY_ECHO = True

class ProductionConfig(Config):
    "configuracion de produccion"
    DEBUG = False

# diccionario que asocia un nombre con una configuracion
app_config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig
}
