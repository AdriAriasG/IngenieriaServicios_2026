import socket
import sys

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

# primero envio las tres lineas seguidas
for linea in ["UNO", "DOS", "TRES"]:
    s.sendall(bytes(linea + "\r\n", "utf8"))

# despues leo tres respuestas y las muestro con repr para ver los \r\n
for i in range(3):
    respuesta = s.recv(80)
    print(repr(respuesta))

s.close()
