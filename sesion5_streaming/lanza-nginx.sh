#!/bin/bash
# me coloco en la carpeta del script para que $(pwd) apunte a ella
cd "$(dirname "$0")"

# paro el contenedor anterior si existia (con --rm se borra solo)
docker stop nginx 2>/dev/null

# nginx con la configuracion por defecto, sirviendo mi carpeta html en el puerto 80
docker run --rm -d --name nginx -p 80:80 \
    -v $(pwd)/html:/usr/share/nginx/html nginx
