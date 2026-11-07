#!/bin/bash
# me coloco en la carpeta del script para que $(pwd) apunte a ella
cd "$(dirname "$0")"

# paro el contenedor anterior si existia (con --rm se borra solo)
docker stop basedatos 2>/dev/null

# mariadb con la base de datos amigosdb, su usuario y los datos en ./basedatos
docker run --name basedatos \
    -e MYSQL_ROOT_PASSWORD=claveroot \
    -e MYSQL_USER=amigosuser \
    -e MYSQL_DATABASE=amigosdb \
    -e MYSQL_PASSWORD=amigospass \
    -v $(pwd)/basedatos:/var/lib/mysql \
    --rm --network pruebas -d mariadb
