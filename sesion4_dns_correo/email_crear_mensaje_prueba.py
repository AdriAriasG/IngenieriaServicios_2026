# creo un mensaje que cumple el estandar con la biblioteca email y lo muestro
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

# paso el mensaje a bytes, listo para mandarlo por un socket, y lo muestro
binario = mensaje.as_bytes()
print(binario.decode("utf-8"))
