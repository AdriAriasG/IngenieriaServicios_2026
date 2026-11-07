#!/bin/bash
# paro el contenedor anterior si existia
docker stop amigos 2>/dev/null

# aplicacion flask con la imagen 3.0 (health check y metricas); le paso por
# variables de entorno el modo y la url de la base de datos
docker run --name amigos \
    -e DEPLOYMENT_MODE=production \
    -e DATABASE_URI=mysql+pymysql://amigosuser:amigospass@basedatos/amigosdb \
    --rm -d --network pruebas amigos:3.0
