import socket
import struct
import sys

# recibo exactamente n bytes, llamando a recv las veces que haga falta
def recvall(sock, n):
    trozos = []
    faltan = n
    while faltan > 0:
        trozo = sock.recv(faltan)
        if trozo == b"":
            break
        trozos.append(trozo)
        faltan = faltan - len(trozo)
    return b"".join(trozos)

# si me pasan el puerto por linea de comandos lo uso, si no uso el 9999
if len(sys.argv) > 1:
    puerto = int(sys.argv[1])
else:
    puerto = 9999

# creo el socket tcp de escucha, lo asocio al puerto y lo pongo en modo pasivo
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("", puerto))
s.listen(5)
print("Servidor oche escuchando en el puerto", puerto)

while True:
    print("Esperando un cliente")
    sd, origen = s.accept()
    print("Nuevo cliente conectado desde %s, %d" % origen)
    while True:
        # leo los 2 bytes de la longitud (big endian), sin bucles ni terminadores
        cabecera = recvall(sd, 2)
        if len(cabecera) < 2:
            print("El cliente ha cerrado la conexion")
            sd.close()
            break
        # unpack devuelve una tupla, me quedo con el primer elemento
        longitud = struct.unpack(">H", cabecera)[0]
        mensaje = recvall(sd, longitud).decode("utf8")
        respuesta = mensaje[::-1].encode("utf8")
        # contesto con el mismo formato: 2 bytes de longitud y el mensaje
        sd.sendall(struct.pack(">H", len(respuesta)) + respuesta)
