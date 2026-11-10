# me conecto a la web de wikipedia usando getaddrinfo() para saber como crear el socket
import socket

# cada elemento es una forma de conectar: (familia, tipo, protocolo, nombre canonico, direccion)
opciones = socket.getaddrinfo("en.wikipedia.org", "www")

# me quedo con la primera opcion de ipv4 (para probar ipv6 se cambia AF_INET por AF_INET6)
for familia, tipo, protocolo, canonico, direccion in opciones:
    if familia == socket.AF_INET:
        break

# creo el socket y me conecto con los valores que me ha dado getaddrinfo
s = socket.socket(familia, tipo, protocolo)
s.connect(direccion)
print("Conectado a", direccion)

# pido el recurso raiz; Connection: close para que el servidor cierre al acabar
peticion = "GET / HTTP/1.1\r\nHost: en.wikipedia.org\r\nConnection: close\r\n\r\n"
s.send(peticion.encode("ascii"))

# recibo hasta que el servidor cierra la conexion y lo muestro
respuesta = b""
datos = s.recv(1024)
while datos:
    respuesta = respuesta + datos
    datos = s.recv(1024)
print(respuesta.decode("utf-8", "replace"))
s.close()
