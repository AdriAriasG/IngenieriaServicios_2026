# envio un correo por smtp en crudo usando gmail: starttls para cifrar y auth login para autenticarme
import socket
import ssl
import sys
import base64
import getpass
import email.message, email.policy, email.utils

def RecvReply(s, codigo):
    "recibo la respuesta del servidor y compruebo que empieza por el codigo esperado"
    respuesta = s.recv(1024)
    print(respuesta.decode("utf-8").strip())
    # los tres primeros bytes son el codigo de respuesta smtp
    if respuesta[:3] != codigo:
        print("Error: esperaba", codigo.decode(), "y he recibido", respuesta[:3].decode())
        sys.exit()

server = "smtp.gmail.com"
port = 587
# usuario de gmail y su clave de aplicacion, pedidos por teclado
username = input("Usuario: ")
password = getpass.getpass("Contraseña: ")
# el remitente es la propia cuenta de gmail; para el experimento del remite falso se cambia aqui
fromaddr = username
toaddr = "qratz.otros@gmail.com"
subject = "Prueba de envio por smtp en crudo con gmail"
data = "Hola, este correo lo he enviado hablando smtp por un socket cifrado con TLS."

# construyo el mensaje con la biblioteca email
mensaje = email.message.EmailMessage()
mensaje['To'] = toaddr
mensaje['From'] = fromaddr
mensaje['Subject'] = subject
mensaje['Date'] = email.utils.formatdate(localtime=True)
mensaje['Message-ID'] = email.utils.make_msgid()
mensaje.set_content(data)
# a los bytes del mensaje les pongo yo detras la linea final con solo un punto
# con la politica SMTP las lineas acaban en \r\n, como exige el protocolo
binario = mensaje.as_bytes(policy=email.policy.SMTP) + b"\r\n.\r\n"

# me conecto y leo el saludo (220)
s = socket.socket()
s.connect((server, port))
RecvReply(s, b"220")

# EHLO en vez de HELO: la respuesta trae los comandos extendidos, entre ellos STARTTLS
s.send(b"EHLO " + socket.gethostname().encode() + b"\r\n")
RecvReply(s, b"250")

# pido cifrar la conexion y, si me dice 220, negocio TLS sobre el mismo socket
s.send(b"STARTTLS\r\n")
RecvReply(s, b"220")
context = ssl.create_default_context()
sc = context.wrap_socket(s, server_hostname=server)
# a partir de aqui todo va por el socket cifrado sc

# gmail exige volver a presentarse con EHLO una vez cifrado el canal
sc.send(b"EHLO " + socket.gethostname().encode() + b"\r\n")
RecvReply(sc, b"250")

# autenticacion: usuario y clave en base64, cada uno tras un 334
sc.send(b"AUTH LOGIN\r\n")
RecvReply(sc, b"334")
sc.send(base64.b64encode(username.encode("ascii")) + b'\r\n')
RecvReply(sc, b"334")
sc.send(base64.b64encode(password.encode("utf8")) + b'\r\n')
# si la clave es buena responde 235
RecvReply(sc, b"235")

# el resto es igual que sin cifrar, pero por sc
sc.send(b"MAIL FROM:<" + fromaddr.encode() + b">\r\n")
RecvReply(sc, b"250")
sc.send(b"RCPT TO:<" + toaddr.encode() + b">\r\n")
RecvReply(sc, b"250")
sc.send(b"DATA\r\n")
RecvReply(sc, b"354")
sc.send(binario)
RecvReply(sc, b"250")
sc.send(b"QUIT\r\n")
RecvReply(sc, b"221")
sc.close()
