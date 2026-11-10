# como email_crear_mensaje_prueba.py pero con un gif adjunto (ejercicio 9)
import email.message, email.policy, email.utils

mensaje = email.message.EmailMessage()
# las cabeceras se ponen como en un diccionario
mensaje['To'] = 'Desti Natario <destinatario@example.com>'
mensaje['From'] = 'Remi Tente <remitente@example.com>'
mensaje['Subject'] = 'Mensaje de prueba'
# fecha en el formato del estandar y un identificador unico para el mensaje
mensaje['Date'] = email.utils.formatdate(localtime=True)
mensaje['Message-ID'] = email.utils.make_msgid()
# el texto del mensaje
mensaje.set_content("Esto es una prueba")

# leo el gif en binario y lo adjunto indicando su tipo mime (image/gif) y su nombre
with open("logoatc.gif", "rb") as f:
    gif = f.read()
mensaje.add_attachment(gif, "image", "gif", filename="atc.gif")

# paso el mensaje a bytes, listo para mandarlo por un socket, y lo muestro
binario = mensaje.as_bytes()
print(binario.decode("utf-8"))
