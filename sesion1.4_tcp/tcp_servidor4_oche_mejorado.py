import socket
import sys

# leo bytes de uno en uno hasta tener una linea completa (termina en \r\n)
def recibe_mensaje(sd):
    # uso una lista y no concatenacion, es mucho mas eficiente
    buffer = []
    while True:
        byte = sd.recv(1)
        if byte == b"":
            # el cliente ha cerrado la conexion
            return b""
        buffer.append(byte)
        # compruebo si los dos ultimos bytes son el fin de linea
        if len(buffer) >= 2 and buffer[-2] == b"\r" and buffer[-1] == b"\n":
            return b"".join(buffer)

# si me pasan el puerto por linea de comandos lo uso, si no uso el 9999
if len(sys.argv) > 1:
    puerto = int(sys.argv[1])
else:
    puerto = 9999

# creo el socket tcp de escucha, lo asocio al puerto y lo pongo en modo pasivo
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("", puerto))
s.listen(5)
print("Servidor oche escuchando en el puerto", puerto)

while True:
    print("Esperando un cliente")
    sd, origen = s.accept()
    print("Nuevo cliente conectado desde %s, %d" % origen)
    while True:
        mensaje = recibe_mensaje(sd)
        if mensaje == b"":
            print("El cliente ha cerrado la conexion")
            sd.close()
            break
        mensaje = str(mensaje, "utf8")
        # quito el fin de linea y le doy la vuelta
        linea = mensaje[:-2]
        linea = linea[::-1]
        sd.sendall(bytes(linea + "\r\n", "utf8"))
