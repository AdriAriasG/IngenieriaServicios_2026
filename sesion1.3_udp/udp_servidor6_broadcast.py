import socket

# puerto prefijado del protocolo HOLA
puerto = 12345

# creo el socket udp, lo pongo en modo broadcast y lo asocio al puerto
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
s.bind(("", puerto))
print("Servidor HOLA escuchando en el puerto", puerto)

while True:
    datagrama, origen = s.recvfrom(1024)
    texto = datagrama.decode("utf8")
    print("Recibido desde", origen, ":", texto)
    if texto == "BUSCANDO HOLA":
        # aviso al cliente de que implemento el servicio
        s.sendto("IMPLEMENTO HOLA".encode("utf8"), origen)
    elif texto == "HOLA":
        # doy el servicio: le devuelvo su propia ip
        s.sendto(("HOLA: " + origen[0]).encode("utf8"), origen)
