import socket
import sys

# valores por defecto, que cambio si me los pasan por linea de comandos
ip = "localhost"
puerto = 9999
if len(sys.argv) > 1:
    ip = sys.argv[1]
if len(sys.argv) > 2:
    puerto = int(sys.argv[2])

# creo el socket udp (en el cliente no hace falta bind)
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# leo lineas del teclado y las envio hasta que escriban FIN
while True:
    linea = input("Mensaje (FIN para terminar): ")
    if linea == "FIN":
        break
    # paso la cadena a bytes justo antes de enviarla
    s.sendto(linea.encode("utf8"), (ip, puerto))

s.close()
