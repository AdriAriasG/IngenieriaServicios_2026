# parto de la imagen de python
FROM python:3.7

# instalo flask, gunicorn y las librerias de la aplicacion dentro de la imagen
RUN pip install flask && pip install gunicorn
RUN pip install flask-sqlalchemy pymysql flask-migrate
# libreria de prometheus para exponer las metricas en /metrics
RUN pip install prometheus-client

# copio toda la carpeta amigos a /amigos del contenedor
RUN mkdir /amigos
COPY . /amigos
WORKDIR /amigos

EXPOSE 5000

# gunicorn sirve la variable app del modulo lanzar
CMD ["/usr/local/bin/gunicorn", "-b", "0.0.0.0:5000", "-w", "4", "lanzar:app"]
