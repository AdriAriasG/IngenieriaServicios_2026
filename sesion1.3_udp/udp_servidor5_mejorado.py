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
print("Servidor UDP mejorado escuchando en el puerto", puerto)

while True:
    datagrama, origen = s.recvfrom(1024)
    # el datagrama ya ha llegado a mi socket, pero finjo que no
    if random.randint(1, 2) == 1:
        print("Simulando paquete perdido")
    else:
        texto = datagrama.decode("utf8")
        print("Recibido desde", origen, ":", texto)
        # mejora: el OK lleva el identificador del datagrama que confirmo ("1: Hola" -> "OK 1")
        identificador = texto.split(":")[0]
        s.sendto(("OK " + identificador).encode("utf8"), origen)
