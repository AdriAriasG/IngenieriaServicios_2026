#!/bin/bash
# me coloco en la carpeta del script: aqui estan applications, conf y content
cd "$(dirname "$0")"

# paro el contenedor anterior si existia (con --rm se borra solo)
docker stop wowza 2>/dev/null

# wowza con todos sus puertos: 1935 streaming, 8086-8088 administracion,
# 5004-5008/udp para recibir video en directo; monto mis carpetas para que
# las aplicaciones, la configuracion y los videos no se pierdan
docker run -it --rm -d --name wowza \
    -p 1935:1935 -p 8086:8086 -p 8087:8087 -p 8088:8088 \
    -p 5004-5008:5004-5008/udp \
    -e WSE_MGR_USER=wowza \
    -e WSE_MGR_PASS=clavesecreta \
    -v $(pwd)/applications:/usr/local/WowzaStreamingEngine/applications \
    -v $(pwd)/conf:/usr/local/WowzaStreamingEngine/conf \
    -v $(pwd)/content:/usr/local/WowzaStreamingEngine/content \
    --entrypoint /sbin/entrypoint.sh \
    wowzamedia/wowza-streaming-engine-linux:4.8.17
