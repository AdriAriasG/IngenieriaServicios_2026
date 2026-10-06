import socket
import sys

# recibo exactamente n bytes, llamando a recv las veces que haga falta
def recvall(sock, n):
    trozos = []
    faltan = n
    while faltan > 0:
        # pido solo los bytes que me faltan, no de uno en uno
        trozo = sock.recv(faltan)
        if trozo == b"":
            # el otro extremo ha cerrado: devuelvo lo que haya llegado
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
print("Servidor TCP escuchando en el puerto", puerto)

# bucle principal de espera por clientes
while True:
    print("Esperando un cliente")
    sd, origen = s.accept()
    print("Nuevo cliente conectado desde %s, %d" % origen)
    continuar = True
    # bucle de atencion al cliente conectado
    while continuar:
        # leo del socket de datos sd, no del de escucha s
        datos = recvall(sd, 5)
        datos = datos.decode("ascii")
        if datos == "":
            # si no llegan datos es que el cliente ha cerrado el socket
            print("Conexion cerrada de forma inesperada por el cliente")
            sd.close()
            continuar = False
        elif datos == "FINAL":
            print("Recibido mensaje de finalizacion")
            sd.close()
            continuar = False
        else:
            print("Recibido mensaje: %s" % datos)
