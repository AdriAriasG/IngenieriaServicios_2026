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

while True:
    linea = input("Mensaje (FIN para terminar): ")
    if linea == "FIN":
        break
    # pongo el numero delante: "1: Hola"
    mensaje = str(numero) + ": " + linea

    # reintento el envio duplicando el timeout hasta recibir el OK o pasar de 2 segundos
    timeout = 0.1
    confirmado = False
    while not confirmado and timeout <= 2:
        s.sendto(mensaje.encode("utf8"), (ip, puerto))
        s.settimeout(timeout)
        try:
            datagrama, origen = s.recvfrom(1024)
            print("Recibido", datagrama.decode("utf8"), "desde", origen)
            confirmado = True
        except socket.timeout:
            # no ha llegado el OK: duplico el timeout y vuelvo a enviar el mismo mensaje
            print("Sin confirmacion, reintento")
            timeout = timeout * 2

    # si me paso de 2 segundos asumo que el servidor esta caido y termino
    if not confirmado:
        print("Puede que el servidor este caido. Intentelo mas tarde")
        break

    # solo incremento el numero cuando el datagrama se ha confirmado
    numero = numero + 1

s.close()
