#!/bin/bash
# version de la imagen a lanzar (por defecto 2.0); uso: ./lanza-flask.sh 1.0
VERSION=${1:-2.0}

# paro el contenedor anterior si existia
docker stop amigos 2>/dev/null

# aplicacion flask con gunicorn; le paso por variables de entorno el modo y la
# url de la base de datos (por nombre de contenedor gracias al dns de docker)
docker run --name amigos \
    -e DEPLOYMENT_MODE=production \
    -e DATABASE_URI=mysql+pymysql://amigosuser:amigospass@basedatos/amigosdb \
    --rm -d --network pruebas amigos:$VERSION
