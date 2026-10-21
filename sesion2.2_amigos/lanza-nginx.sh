#!/bin/bash
# me coloco en la carpeta del script para que $(pwd) apunte a ella
cd "$(dirname "$0")"

# paro el contenedor anterior si existia
docker stop nginx 2>/dev/null

# nginx como proxy inverso hacia la aplicacion; solo monto la configuracion
docker run --rm -d --network pruebas --name nginx \
    -v $(pwd)/sitios_nginx:/etc/nginx/conf.d \
    -p 80:80 nginx
