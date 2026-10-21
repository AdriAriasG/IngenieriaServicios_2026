from flask import render_template, redirect, url_for, request, abort
from . import html
from .. import db
from ..models import Amigo

@html.route("/amigos")
def tabla_amigos():
    "obtengo la lista de amigos de la base de datos y la devuelvo en una tabla html"
    amigos = Amigo.query.all()
    return render_template("tabla_amigos.html", amigos=amigos)

@html.route("/delete_amigo/<int:id>")
def delete_amigo(id):
    "borro un amigo de la base de datos"
    # get_or_404 genera un 404 si el id no existe
    amigo = Amigo.query.get_or_404(id)
    db.session.delete(amigo)
    db.session.commit()
    # redirijo a la tabla de amigos (codigo 302)
    return redirect(url_for('html.tabla_amigos'))

@html.route("/edit_amigo/<int:id>")
def edit_amigo(id):
    "presento un formulario con los datos del amigo a modificar"
    amigo = Amigo.query.get_or_404(id)
    return render_template("edit_amigo.html", amigo=amigo)

@html.route("/new_amigo/")
def new_amigo():
    "presento el mismo formulario pero vacio, para un amigo nuevo"
    return render_template("edit_amigo.html", amigo=None)

@html.route("/save_amigo", methods=["POST"])
def save_amigo():
    "recibo el formulario y creo un amigo nuevo o modifico uno existente"
    id = request.form.get("id")
    if id is None or id == "":
        # amigo nuevo: el nombre es obligatorio
        name = request.form.get("name")
        if not name:
            abort(422)
        # latitud y longitud son opcionales, por defecto "0"
        lati = request.form.get("lati", "0")
        longi = request.form.get("longi", "0")
        device = request.form.get("device")
        amigo = Amigo(name=name, lati=lati, longi=longi, device=device)
        db.session.add(amigo)
        db.session.commit()
    else:
        # amigo existente: modifico los campos que lleguen
        amigo = Amigo.query.get_or_404(int(id))
        name = request.form.get("name")
        if name:
            amigo.name = name
        lati = request.form.get("lati")
        if lati:
            amigo.lati = lati
        longi = request.form.get("longi")
        if longi:
            amigo.longi = longi
        # el device puede venir vacio y se guarda tal cual
        device = request.form.get("device")
        if device is not None:
            amigo.device = device
        db.session.commit()
    return redirect(url_for("html.tabla_amigos"))
