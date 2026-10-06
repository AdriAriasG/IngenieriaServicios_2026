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

# contador de datagramas enviados, empieza en 1
numero = 1

# leo lineas del teclado y las envio numeradas hasta que escriban FIN
while True:
    linea = input("Mensaje (FIN para terminar): ")
    if linea == "FIN":
        break
    # pongo el numero delante: "1: Hola"
    mensaje = str(numero) + ": " + linea
    # paso la cadena a bytes justo antes de enviarla
    s.sendto(mensaje.encode("utf8"), (ip, puerto))
    numero = numero + 1

    # espero el OK del servidor como mucho una decima de segundo
    s.settimeout(0.1)
    try:
        datagrama, origen = s.recvfrom(1024)
        print("Recibido", datagrama.decode("utf8"), "desde", origen)
    except socket.timeout:
        # si salta el timeout asumo que el datagrama (o el OK) se ha perdido
        print("Error: no he recibido confirmacion, se ha perdido el datagrama")

s.close()
