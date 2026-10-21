# parto de la imagen de python que ya tengo descargada
FROM python:3.7

# instalo flask y gunicorn dentro de la imagen (global en el contenedor)
RUN pip install flask && pip install gunicorn

# copio mi aplicacion a la carpeta /app del contenedor
RUN mkdir /app
COPY hola_flask.py /app

# el contenedor arranca en /app
WORKDIR /app

# gunicorn escucha en el puerto 5000
EXPOSE 5000

# lanzo gunicorn con 4 workers sirviendo la variable app del modulo hola_flask
CMD ["/usr/local/bin/gunicorn", "-b", "0.0.0.0:5000", "-w", "4", "hola_flask:app"]
