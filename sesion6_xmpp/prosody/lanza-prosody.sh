#!/bin/bash
# me coloco en la carpeta del script: aqui estan etc y data
cd "$(dirname "$0")"

# paro el contenedor anterior si existia (con --rm se borra solo)
docker stop prosody 2>/dev/null

# prosody en la red pruebas (para que luego el bot en otro contenedor lo encuentre por nombre),
# con el puerto 5222 de clientes publicado, mi configuracion en etc y los datos
# (usuarios, rosters, mensajes pendientes) guardados en data para que no se pierdan
docker run --rm -d --name prosody --network pruebas \
  -p 5222:5222 \
  -v $(pwd)/etc/prosody:/etc/prosody \
  -v $(pwd)/data:/var/lib/prosody \
  unclev/prosody-docker-extended:0.10
