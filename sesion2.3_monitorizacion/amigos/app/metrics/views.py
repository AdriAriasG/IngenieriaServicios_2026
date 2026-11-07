import time
from flask import Response, g
from app.metrics import metrics
from prometheus_client import (
    Counter,
    Histogram,
    generate_latest,
    CONTENT_TYPE_LATEST
)

# contador de todas las peticiones http que recibo
http_requests_total = Counter(
    "amigos_http_requests_total",
    "Número total de peticiones HTTP recibidas por Amigos"
)

# contador de las respuestas de error (codigo 400 o mayor)
http_errors_total = Counter(
    "amigos_http_errors_total",
    "Número total de respuestas HTTP de error"
)

# histograma con el tiempo que tardo en responder cada peticion
http_request_duration_seconds = Histogram(
    "amigos_http_request_duration_seconds",
    "Tiempo de respuesta de las peticiones HTTP en segundos"
)

@metrics.before_app_request
def before_request():
    "apunto la hora a la que empieza cada peticion de toda la app"
    g.start_time = time.perf_counter()

@metrics.after_app_request
def after_request(response):
    "al terminar cada peticion actualizo los contadores y el histograma"
    http_requests_total.inc()
    # cuento como error cualquier respuesta 4xx o 5xx
    if response.status_code >= 400:
        http_errors_total.inc()
    # tiempo que ha tardado desde el before_request
    duration = time.perf_counter() - g.start_time
    http_request_duration_seconds.observe(duration)
    return response

@metrics.route("/metrics")
def metrics_endpoint():
    "devuelvo todas las metricas en el formato de texto que entiende prometheus"
    return Response(
        generate_latest(),
        mimetype=CONTENT_TYPE_LATEST
    )
