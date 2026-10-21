from flask import Flask

# creo la aplicacion flask
app = Flask(__name__)

# asocio la ruta raiz con esta funcion; lo que devuelve es la respuesta http
@app.route('/')
def hola_flask():
    return '¡Hola Flask!'
