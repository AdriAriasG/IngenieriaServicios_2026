# como email_pop3_recibe_crudo.py pero muestro Subject y From de todos los correos
import socket
import ssl
import sys
import getpass

def RecvReply(s):
    "recibo la respuesta del servidor y compruebo que es de exito (+OK)"
    respuesta = s.recv(1024)
    print(respuesta.decode("utf-8").strip())
    if respuesta[:3] != b"+OK":
        print("Error: el servidor no ha respondido +OK")
        sys.exit()
    return respuesta

server = "pop.gmail.com"
port = 995
# usuario de gmail y su clave de aplicacion, pedidos por teclado
username = input("Usuario: ")
password = getpass.getpass("Contraseña: ")

# en pop3 de gmail el canal va cifrado desde el principio (puerto 995)
s = socket.socket()
s.connect((server, port))
context = ssl.create_default_context()
sc = context.wrap_socket(s, server_hostname=server)
# mensaje de bienvenida
RecvReply(sc)

# entro en sesion con USER y PASS
sc.send(b"USER " + username.encode() + b"\r\n")
RecvReply(sc)
sc.send(b"PASS " + password.encode() + b"\r\n")
RecvReply(sc)

# STAT responde "+OK numero_de_mensajes bytes_totales"
sc.send(b"STAT\r\n")
respuesta = RecvReply(sc)
num_mensajes = int(respuesta.split()[1])
print("Hay", num_mensajes, "mensajes")

# recorro todos los mensajes, del 1 al ultimo
for numero in range(1, num_mensajes + 1):
    # pido el mensaje; llega en varios trozos hasta la linea con solo un punto
    sc.send(b"RETR " + str(numero).encode() + b"\r\n")
    mensaje = sc.recv(1024)
    while not mensaje.endswith(b"\r\n.\r\n"):
        mensaje = mensaje + sc.recv(1024)

    # busco en las lineas del mensaje las cabeceras Subject y From
    print("--- Mensaje", numero)
    for linea in mensaje.decode("utf-8", "replace").split("\r\n"):
        if linea.startswith("Subject:") or linea.startswith("From:"):
            print(linea)
        # la primera linea vacia separa las cabeceras del cuerpo
        if linea == "":
            break

# cierro la sesion
sc.send(b"QUIT\r\n")
RecvReply(sc)
sc.close()
