# leo el primer correo de gmail con poplib, que se ocupa de los comandos y respuestas de pop3
import poplib
import getpass

server = "pop.gmail.com"
# usuario de gmail y su clave de aplicacion, pedidos por teclado
username = input("Usuario: ")
password = getpass.getpass("Contraseña: ")

# conexion cifrada (puerto 995 por defecto) y depuracion para ver el protocolo
pop3_mail = poplib.POP3_SSL(server)
pop3_mail.set_debuglevel(2)

# entro en sesion
pop3_mail.user(username)
pop3_mail.pass_(password)

# retr devuelve una tupla: respuesta del servidor, lista de lineas del mensaje y numero de bytes
respuesta, lineas, tamano = pop3_mail.retr(1)
print(respuesta)
for linea in lineas:
    print(linea)

pop3_mail.quit()
