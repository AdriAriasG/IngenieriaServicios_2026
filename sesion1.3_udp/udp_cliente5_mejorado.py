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

# el numero de secuencia hace de identificador del datagrama
numero = 1

while True:
    linea = input("Mensaje (FIN para terminar): ")
    if linea == "FIN":
        break
    mensaje = str(numero) + ": " + linea

    # reintento duplicando el timeout hasta recibir el OK de este identificador
    timeout = 0.1
    confirmado = False
    while not confirmado and timeout <= 2:
        s.sendto(mensaje.encode("utf8"), (ip, puerto))
        s.settimeout(timeout)
        try:
            datagrama, origen = s.recvfrom(1024)
            respuesta = datagrama.decode("utf8")
            # mejora: solo acepto el OK que lleva el identificador de este mensaje
            if respuesta == "OK " + str(numero):
                print("Recibido", respuesta, "desde", origen)
                confirmado = True
            else:
                print("Ignoro confirmacion que no es la esperada:", respuesta)
        except socket.timeout:
            print("Sin confirmacion, reintento")
            timeout = timeout * 2

    if not confirmado:
        print("Puede que el servidor este caido. Intentelo mas tarde")
        break
    numero = numero + 1

s.close()
