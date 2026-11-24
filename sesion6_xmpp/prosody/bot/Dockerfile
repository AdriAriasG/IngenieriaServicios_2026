# parto de la imagen de python que ya tengo descargada
FROM python:3.7

# instalo la biblioteca xmpp en la version del guion
RUN pip install wheel slixmpp==1.8.6

# copio el bot y el certificado del servidor en el que confia
RUN mkdir /bot
COPY bot.py ingserv003.crt /bot/
WORKDIR /bot

# -u para que los print salgan al momento en docker logs
CMD ["python", "-u", "bot.py"]
