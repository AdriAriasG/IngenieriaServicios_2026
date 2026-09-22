import socket
import sys

# si me pasan el puerto por linea de comandos lo uso, si no uso el 9999
if len(sys.argv) > 1:
    puerto = int(sys.argv[1])
else:
    puerto = 9999

# creo el socket udp y lo asocio al puerto en todas las interfaces
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(("", puerto))
print("Servidor UDP escuchando en el puerto", puerto)

# bucle infinito: por cada datagrama que llega muestro su contenido y su origen
while True:
    datagrama, origen = s.recvfrom(1024)
    # paso los bytes a cadena nada mas recibirlos
    texto = datagrama.decode("utf8")
    print("Recibido desde", origen, ":", texto)
