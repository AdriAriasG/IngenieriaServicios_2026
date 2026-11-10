# con poplib leo todos los correos y muestro un resumen de cada uno (remite, asunto y comienzo)
import poplib
import getpass
import email
import email.header

def imprime_resumen_mensaje(msg_bytes):
    "muestro remite, asunto y el principio del cuerpo de un mensaje recibido en bytes (funcion del guion)"
    # paso los bytes a un objeto mensaje
    msg = email.message_from_bytes(msg_bytes)
    # saco las cabeceras From y Subject
    remite = msg.get("From", "<desconocido>")
    asunto = msg.get("Subject", "<sin asunto>")

    # si llevan unicode vienen codificadas y hay que decodificarlas
    remite = email.header.make_header(email.header.decode_header(remite))
    asunto = email.header.make_header(email.header.decode_header(asunto))

    # saco el cuerpo
    cuerpo = msg.get_payload()

    # si es multipart me devuelve una lista de partes: me quedo con la primera
    # (str por si esa parte es a su vez multipart y tambien viene como lista)
    if type(cuerpo) == list:
        parte_1 = cuerpo[0].get_payload()
        cuerpo = "---Multipart. Parte 1\n" + str(parte_1)

    # muestro las cabeceras y los primeros 500 caracteres del cuerpo
    print("From:", remite)
    print("Subject:", asunto)
    print(cuerpo[:500])
    if len(cuerpo) > 500:
        print("...[omitido]")
    print("-" * 80)

server = "pop.gmail.com"
# usuario de gmail y su clave de aplicacion, pedidos por teclado
username = input("Usuario: ")
password = getpass.getpass("Contraseña: ")

# conexion cifrada y entrada en sesion
pop3_mail = poplib.POP3_SSL(server)
pop3_mail.user(username)
pop3_mail.pass_(password)

# stat devuelve (numero de mensajes, bytes totales)
num_mensajes, total_bytes = pop3_mail.stat()
print("Hay", num_mensajes, "mensajes")

for numero in range(1, num_mensajes + 1):
    respuesta, lineas, tamano = pop3_mail.retr(numero)
    # poplib me da una lista de lineas sin el \r\n: las vuelvo a juntar en bytes
    imprime_resumen_mensaje(b"\r\n".join(lineas))

pop3_mail.quit()
