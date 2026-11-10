# como email_envia_crudo.py pero el mensaje lleva un gif adjunto (ejercicio 9)
# (solo funciona desde la red de uniovi: desde fuera el relay rechaza el destinatario)
import socket
import sys
import email.message, email.policy, email.utils

def RecvReply(s, codigo):
    "recibo la respuesta del servidor y compruebo que empieza por el codigo esperado"
    respuesta = s.recv(1024)
    print(respuesta.decode("utf-8").strip())
    # los tres primeros bytes son el codigo de respuesta smtp
    if respuesta[:3] != codigo:
        print("Error: esperaba", codigo.decode(), "y he recibido", respuesta[:3].decode())
        sys.exit()

server = "relay.uniovi.es"
port = 25
fromaddr = "uo251273@uniovi.es"
toaddr = "uo251273@uniovi.es"
subject = "Prueba de envio con adjunto"
data = "Hola, este correo lo he enviado hablando smtp directamente por un socket."

# construyo el mensaje con la biblioteca email (ejercicio 8) en vez de con una plantilla
mensaje = email.message.EmailMessage()
mensaje['To'] = toaddr
mensaje['From'] = fromaddr
mensaje['Subject'] = subject
mensaje['Date'] = email.utils.formatdate(localtime=True)
mensaje['Message-ID'] = email.utils.make_msgid()
mensaje.set_content(data)
# leo el gif en binario y lo adjunto indicando su tipo mime (image/gif) y su nombre
with open("logoatc.gif", "rb") as f:
    gif = f.read()
mensaje.add_attachment(gif, "image", "gif", filename="atc.gif")
# a los bytes del mensaje les pongo yo detras la linea final con solo un punto
# con la politica SMTP las lineas acaban en \r\n, como exige el protocolo
binario = mensaje.as_bytes(policy=email.policy.SMTP) + b"\r\n.\r\n"

# me conecto al servidor smtp y leo su saludo (220)
s = socket.socket()
s.connect((server, port))
RecvReply(s, b"220")

# me presento con el nombre de mi maquina
s.send(b"HELO " + socket.gethostname().encode() + b"\r\n")
RecvReply(s, b"250")

# remitente y destinatario del sobre
s.send(b"MAIL FROM:<" + fromaddr.encode() + b">\r\n")
RecvReply(s, b"250")
s.send(b"RCPT TO:<" + toaddr.encode() + b">\r\n")
RecvReply(s, b"250")

# aviso de que va el contenido (354) y lo mando con su punto final
s.send(b"DATA\r\n")
RecvReply(s, b"354")
s.send(binario)
RecvReply(s, b"250")

# cierro la conversacion
s.send(b"QUIT\r\n")
RecvReply(s, b"221")
s.close()
