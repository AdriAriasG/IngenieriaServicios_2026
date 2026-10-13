#!/bin/bash
# me coloco en la carpeta del script para que $(pwd) apunte a ella
cd "$(dirname "$0")"

# creo la subred pruebas si no existe
docker network create pruebas 2>/dev/null

# lanzo tres servidores de broadcast en la subred pruebas, cada uno con su nombre
for i in 1 2 3; do
    docker rm -f servidor_hola$i >/dev/null 2>&1
    docker run -d --rm --name servidor_hola$i --network pruebas \
        -v $(pwd):/app python:3.7 python -u /app/udp_servidor6_broadcast.py
done
