import socket
import sys

# direccion de broadcast de mi subred (por argumento, o la general por defecto)
broadcast = "255.255.255.255"
if len(sys.argv) > 1:
    broadcast = sys.argv[1]
puerto = 12345

# creo el socket udp y lo pongo en modo broadcast
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

# envio por broadcast la busqueda a todos los nodos de la subred
s.sendto("BUSCANDO HOLA".encode("utf8"), (broadcast, puerto))

# recojo respuestas hasta que salte el timeout, guardando la ip del primero
s.settimeout(1)
primero = None
while True:
    try:
        datagrama, origen = s.recvfrom(1024)
        print("Responde el servidor", origen[0], ":", datagrama.decode("utf8"))
        if primero is None:
            primero = origen[0]
    except socket.timeout:
        break

# si ha respondido alguno, pruebo el servicio con el primero (ya sin broadcast)
if primero is None:
    print("No ha respondido ningun servidor")
else:
    s.sendto("HOLA".encode("utf8"), (primero, puerto))
    datagrama, origen = s.recvfrom(1024)
    print("Respuesta del servicio:", datagrama.decode("utf8"))

s.close()
