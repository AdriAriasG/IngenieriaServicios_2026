import socket
import sys
import random

# si me pasan el puerto por linea de comandos lo uso, si no uso el 9999
if len(sys.argv) > 1:
    puerto = int(sys.argv[1])
else:
    puerto = 9999

# creo el socket udp y lo asocio al puerto en todas las interfaces
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(("", puerto))
print("Servidor UDP (con perdidas simuladas y OK) escuchando en el puerto", puerto)

# bucle infinito: con un 50% simulo la perdida; si no, lo muestro y respondo OK
while True:
    datagrama, origen = s.recvfrom(1024)
    # el datagrama ya ha llegado a mi socket, pero finjo que no
    if random.randint(1, 2) == 1:
        print("Simulando paquete perdido")
    else:
        # paso los bytes a cadena nada mas recibirlos
        texto = datagrama.decode("utf8")
        print("Recibido desde", origen, ":", texto)
        # confirmo al cliente con otro datagrama
        s.sendto("OK".encode("utf8"), origen)
