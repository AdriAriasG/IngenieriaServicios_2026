import socket
import sys

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
    # atiendo al cliente hasta que cierre la conexion
    while True:
        # supongo que cada recv trae una linea completa de menos de 80 bytes
        mensaje = sd.recv(80)
        if mensaje == b"":
            print("El cliente ha cerrado la conexion")
            sd.close()
            break
        mensaje = str(mensaje, "utf8")
        # quito el fin de linea (2 ultimos caracteres) y le doy la vuelta
        linea = mensaje[:-2]
        linea = linea[::-1]
        # respondo con la linea al reves y su fin de linea
        sd.sendall(bytes(linea + "\r\n", "utf8"))
