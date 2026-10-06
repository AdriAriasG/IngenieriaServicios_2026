import socket
import sys

# leo bytes de uno en uno hasta tener una linea completa (termina en \r\n)
def recibe_mensaje(sd):
    # uso una lista y no concatenacion, es mucho mas eficiente
    buffer = []
    while True:
        byte = sd.recv(1)
        if byte == b"":
            return b"".join(buffer)
        buffer.append(byte)
        if len(buffer) >= 2 and buffer[-2] == b"\r" and buffer[-1] == b"\n":
            return b"".join(buffer)

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

# envio las tres lineas seguidas
for linea in ["UNO", "DOS", "TRES"]:
    s.sendall(bytes(linea + "\r\n", "utf8"))

# leo las tres respuestas, cada una completa gracias a recibe_mensaje
for i in range(3):
    respuesta = recibe_mensaje(s)
    print(repr(respuesta))

s.close()
