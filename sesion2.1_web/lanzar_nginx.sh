#!/bin/bash
# me coloco en la carpeta del script para que $(pwd) apunte a ella
cd "$(dirname "$0")"

# paro el contenedor anterior si existia (con --rm se borra solo)
docker stop nginx 2>/dev/null

# lanzo nginx en la red pruebas, mapeando los puertos 80 y 81 al anfitrion
# y montando los html de los dos sitios y la carpeta de configuracion
docker run --rm -d --network pruebas \
    --name nginx -p 80:80 -p 81:81 \
    -v $(pwd)/html:/usr/share/nginx/html \
    -v $(pwd)/html2:/usr/share/nginx/html2 \
    -v $(pwd)/sitios_nginx:/etc/nginx/conf.d nginx
