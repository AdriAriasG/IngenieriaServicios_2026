#!/bin/bash
# paro el contenedor anterior si existia (con --rm se borra solo)
docker stop bot 2>/dev/null

# bot en la red pruebas: encuentra a prosody por su nombre de contenedor;
# la clave no esta en ningun fichero, se la pido aqui y se la paso por variable de entorno
read -s -p "Clave del bot: " CLAVEBOT
echo
docker run --rm -d --name bot --network pruebas \
    -e IPSERVIDOR=prosody -e CLAVEBOT=$CLAVEBOT bot:1.0
