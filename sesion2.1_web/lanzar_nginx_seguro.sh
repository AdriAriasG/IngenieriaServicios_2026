#!/bin/bash
# me coloco en la carpeta del script para que $(pwd) apunte a ella
cd "$(dirname "$0")"

# paro el contenedor anterior si existia (con --rm se borra solo)
docker stop nginx 2>/dev/null

# igual que lanzar_nginx.sh, pero ademas monto mi nginx.conf con las opciones
# de seguridad encima del global del contenedor
docker run --rm -d --network pruebas \
    --name nginx -p 80:80 -p 81:81 \
    -v $(pwd)/html:/usr/share/nginx/html \
    -v $(pwd)/html2:/usr/share/nginx/html2 \
    -v $(pwd)/sitios_nginx:/etc/nginx/conf.d \
    -v $(pwd)/configuracion_nginx/nginx.conf:/etc/nginx/nginx.conf nginx
