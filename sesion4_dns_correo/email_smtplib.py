# envio un correo con gmail usando smtplib, que se ocupa de los comandos y codigos de smtp
import smtplib
import getpass
import email.message, email.utils

server = "smtp.gmail.com"
port = 587
# usuario de gmail y su clave de aplicacion, pedidos por teclado
username = input("Usuario: ")
password = getpass.getpass("Contraseña: ")
fromaddr = username
toaddr = "qratz.otros@gmail.com"
subject = "Prueba de envio con smtplib"
data = "Hola, este correo lo he enviado con smtplib."

# construyo el mensaje con la biblioteca email
mensaje = email.message.EmailMessage()
mensaje['To'] = toaddr
mensaje['From'] = fromaddr
mensaje['Subject'] = subject
mensaje['Date'] = email.utils.formatdate(localtime=True)
mensaje['Message-ID'] = email.utils.make_msgid()
mensaje.set_content(data)
# aqui no hace falta el punto final: lo pone smtplib
binario = mensaje.as_bytes()

# me conecto y activo la depuracion para ver los comandos y las respuestas
s = smtplib.SMTP(server, port)
s.set_debuglevel(1)
# cifro el canal y me autentico
s.starttls()
s.login(username, password)
# envio el mensaje y cierro la conexion
s.sendmail(fromaddr, toaddr, binario)
s.quit()
