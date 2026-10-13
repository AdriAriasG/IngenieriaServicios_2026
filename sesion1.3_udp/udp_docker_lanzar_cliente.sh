#!/bin/bash
# me coloco en la carpeta del script para que $(pwd) apunte a ella
cd "$(dirname "$0")"

# direccion de broadcast de la subred pruebas (172.18.0.0/16 -> 172.18.255.255)
# la he sacado con docker inspect (IPAddress e IPPrefixLen de un servidor)
BROADCAST=172.18.255.255

# lanzo el cliente en la misma subred, pasandole la direccion de broadcast
docker run --rm --network pruebas -v $(pwd):/app python:3.7 \
    python /app/udp_cliente6_broadcast.py $BROADCAST
