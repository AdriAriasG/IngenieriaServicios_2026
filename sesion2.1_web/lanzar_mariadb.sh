#!/bin/bash
# me coloco en la carpeta del script para que $(pwd) apunte a ella
cd "$(dirname "$0")"

# paro el contenedor anterior si existia (con --rm se borra solo)
docker stop mariadb 2>/dev/null

# lanzo mariadb en la red pruebas, con la clave de root por variable de entorno
# y guardando los datos en la carpeta basedatos del anfitrion (persistente)
docker run --name mariadb -e MYSQL_ROOT_PASSWORD=claveroot \
    -v $(pwd)/basedatos:/var/lib/mysql \
    --rm --network pruebas -d mariadb
