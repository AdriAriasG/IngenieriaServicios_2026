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
    # convierto el socket en un fichero para poder usar readline
    f = sd.makefile(encoding="utf8", newline="\r\n")
    while True:
        # readline devuelve un str con la linea completa, incluido el \r\n
        mensaje = f.readline()
        if mensaje == "":
            print("El cliente ha cerrado la conexion")
            f.close()
            sd.close()
            break
        # quito el fin de linea y le doy la vuelta
        linea = mensaje[:-2]
        linea = linea[::-1]
        sd.sendall(bytes(linea + "\r\n", "utf8"))
