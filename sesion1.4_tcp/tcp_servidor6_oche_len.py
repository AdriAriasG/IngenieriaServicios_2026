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
    # fichero en binario: la longitud son bytes, y asi read(n) lee n bytes
    f = sd.makefile("rb")
    while True:
        # primero la longitud en ascii, terminada en \n
        cabecera = f.readline()
        if cabecera == b"":
            print("El cliente ha cerrado la conexion")
            f.close()
            sd.close()
            break
        longitud = int(cabecera)
        # despues el mensaje, con exactamente esa longitud
        mensaje = f.read(longitud).decode("utf8")
        respuesta = mensaje[::-1].encode("utf8")
        # contesto con el mismo formato: longitud, \n y mensaje
        sd.sendall(bytes("%d\n" % len(respuesta), "utf8") + respuesta)
