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

# envio 5 veces "ABCDE" (justo 5 bytes)
for i in range(5):
    s.send("ABCDE".encode("ascii"))

# aviso del final, cierro y termino
s.send("FINAL".encode("ascii"))
s.close()
