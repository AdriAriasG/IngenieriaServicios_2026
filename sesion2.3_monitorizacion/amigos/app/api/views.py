from flask import request, abort, jsonify
from .. import db
from . import api
from ..models import Amigo

def a_dict(amigo):
    "paso un amigo a diccionario para devolverlo en json"
    return {'id': amigo.id, 'name': amigo.name,
            'lati': amigo.lati, 'longi': amigo.longi,
            'device': amigo.device}

@api.route("/amigo/<int:id>")
def get_amigo(id):
    "devuelvo en json el amigo con ese id, o 404 si no existe"
    amigo = Amigo.query.get_or_404(id)
    return jsonify(a_dict(amigo))

@api.route("/amigo/byName/<name>")
def get_amigo_by_name(name):
    "busco un amigo por su nombre; 404 si no existe"
    amigo = Amigo.query.filter_by(name=name).first()
    if not amigo:
        abort(404, "No se encuentra ningun amigo con ese nombre")
    return jsonify(a_dict(amigo))

@api.route("/amigos")
def list_amigos():
    "devuelvo en json la lista de todos los amigos"
    amigos = Amigo.query.all()
    return jsonify([a_dict(amigo) for amigo in amigos])

@api.route("/amigo/<int:id>", methods=["PUT"])
def edit_amigo(id):
    "modifico el amigo con ese id y devuelvo su json ya modificado"
    amigo = Amigo.query.get_or_404(id)
    # compruebo que he recibido json
    if not request.json:
        abort(422, "No se ha enviado JSON")
    # los campos que no vengan valdran None
    name = request.json.get("name")
    lati = request.json.get("lati")
    longi = request.json.get("longi")
    device = request.json.get("device")
    if name:
        amigo.name = name
    if lati:
        amigo.lati = lati
    if longi:
        amigo.longi = longi
    # el device puede ser una cadena vacia
    if device is not None:
        amigo.device = device
    # guardo solo si ha cambiado algo
    if name or lati or longi or device is not None:
        db.session.commit()
    return jsonify(a_dict(amigo))

@api.route("/amigo/<int:id>", methods=["DELETE"])
def delete_amigo(id):
    "borro el amigo con ese id"
    amigo = Amigo.query.get_or_404(id)
    db.session.delete(amigo)
    db.session.commit()
    # no hay nada que devolver: 204 "no content"
    return ('', 204)

@api.route("/amigos", methods=["POST"])
def new_amigo():
    "creo un amigo con los datos json recibidos y devuelvo su json (con el id)"
    if not request.json:
        abort(422, "No se ha enviado JSON")
    name = request.json.get("name")
    # sin nombre rechazo la peticion
    if not name:
        abort(422, "El JSON no incluye el campo 'name'")
    # si el nombre ya existe tambien la rechazo
    amigo = Amigo.query.filter_by(name=name).first()
    if amigo:
        abort(422, "Ya existe un amigo con ese nombre")
    # latitud y longitud por defecto "0"
    lati = request.json.get("lati", "0")
    longi = request.json.get("longi", "0")
    amigo = Amigo(name=name, lati=lati, longi=longi)
    db.session.add(amigo)
    db.session.commit()
    return jsonify(a_dict(amigo))

@api.route("/devices")
def list_devices():
    "devuelvo la lista de device no nulos ni vacios"
    devices = [a.device for a in Amigo.query.all() if a.device]
    return jsonify(devices)
