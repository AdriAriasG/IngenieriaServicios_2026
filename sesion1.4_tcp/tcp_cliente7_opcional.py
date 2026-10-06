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

# valores por defecto, que cambio si me los pasan por linea de comandos
ip = "localhost"
puerto = 9999
if len(sys.argv) > 1:
    ip = sys.argv[1]
if len(sys.argv) > 2:
    puerto = int(sys.argv[2])

# creo el socket tcp y me conecto al servidor
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((ip, puerto))

# envio las tres lineas seguidas, cada una con su longitud en 2 bytes big endian
for linea in ["UNO", "DOS", "buenos dias"]:
    datos = linea.encode("utf8")
    s.sendall(struct.pack(">H", len(datos)) + datos)

# leo las tres respuestas: 2 bytes de longitud y despues el mensaje
for i in range(3):
    longitud = struct.unpack(">H", recvall(s, 2))[0]
    respuesta = recvall(s, longitud).decode("utf8")
    print(repr(respuesta))

s.close()
