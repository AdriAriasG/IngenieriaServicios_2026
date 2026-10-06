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

# envio cada linea y leo su respuesta antes de enviar la siguiente
for linea in ["HOLA", "UNO", "buenos dias"]:
    s.sendall(bytes(linea + "\r\n", "utf8"))
    respuesta = s.recv(80)
    print(str(respuesta, "utf8"))

s.close()
