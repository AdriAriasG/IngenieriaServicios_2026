# coding: utf-8
# bot xmpp: responde a los mensajes convirtiendolos en pregunta, avisa de los
# cambios de estado del chat y calcula las expresiones que empiezan por =
import slixmpp          # biblioteca principal para xmpp
import logging          # para el log de depuracion
import getpass          # para pedir la clave sin que se vea
import os               # para leer variables de entorno (clave e ip, util en docker)
import ssl              # para manejar el certificado del servidor

# MiBot hereda de ClientXMPP, que trae ya los callbacks por defecto
class MiBot(slixmpp.ClientXMPP):
    def __init__(self, jid, clave):
        # llamo al constructor de la clase base con los mismos parametros
        super().__init__(jid, clave)

        # registro los eventos que quiero manejar y su callback
        self.add_event_handler("session_start", self.callback_para_session_start)
        self.add_event_handler("message", self.callback_para_message)
        # eventos de la extension chatstates (xep_0085): escribiendo, pausa, etc.
        self.add_event_handler("chatstate_active", self.callback_para_activo)
        self.add_event_handler("chatstate_composing", self.callback_para_escribiendo)
        self.add_event_handler("chatstate_paused", self.callback_para_pausa)
        self.add_event_handler("chatstate_inactive", self.callback_para_inactivo)

    # los callbacks son async porque slixmpp funciona sobre asyncio
    async def callback_para_session_start(self, evento):
        print("Sesión iniciada!")
        # aviso de que estoy online y pido el roster (algunos servidores no
        # entregan mensajes hasta que se ha pedido)
        self.send_presence()
        await self.get_roster()
        print("Roster recibido.")

    async def callback_para_message(self, evento):
        print(f"Recibido un mensaje de tipo {evento['type']} desde {evento['from']}")
        print(f"Que dice: {evento['body']}")

        # solo respondo a los mensajes de chat
        if evento["type"] == "chat":
            cuerpo = evento["body"]
            if cuerpo.startswith("="):
                # calculadora: evaluo lo que va detras del = (eval es peligroso,
                # solo vale para pruebas; si la expresion falla devuelvo el error)
                try:
                    respuesta = str(eval(cuerpo[1:]))
                except Exception as e:
                    respuesta = "Error: " + str(e)
            else:
                # eco: el mismo mensaje entre interrogaciones
                respuesta = "¿%s?" % cuerpo

            # creo el mensaje de respuesta y se lo mando al mismo remitente
            msg = self.Message()
            msg["to"] = evento["from"]
            msg["type"] = "chat"
            msg["body"] = respuesta
            # con chat_state pidgin sigue mandandome sus estados de escritura
            msg["chat_state"] = "active"
            msg.send()

    # callbacks de los estados del chat; bare quita el recurso del jid
    async def callback_para_activo(self, evento):
        print(f"{evento['from'].bare} está activo")

    async def callback_para_escribiendo(self, evento):
        print(f"{evento['from'].bare} está escribiendo...")

    async def callback_para_pausa(self, evento):
        print(f"{evento['from'].bare} ha parado de escribir")

    async def callback_para_inactivo(self, evento):
        print(f"{evento['from'].bare} está inactivo")

# programa principal
if __name__ == "__main__":
    # depuracion: con logging.DEBUG saldria cada stanza
    logging.basicConfig(level=logging.INFO,
                        format='%(levelname)-8s %(message)s')

    # datos del bot; la ip y la clave pueden venir de variables de entorno (para docker)
    jid = "bot@ingserv003"
    ip = os.environ.get("IPSERVIDOR", "localhost")
    puerto = 5222
    clave = os.environ.get("CLAVEBOT")
    if clave is None:
        clave = getpass.getpass("Contraseña: ")

    # el certificado del servidor es autofirmado: confio en la copia que tengo
    # en la carpeta del bot; no compruebo el nombre porque es para 'ingserv003'
    # y me conecto por ip o por 'localhost'
    ssl_context = ssl.create_default_context()
    ssl_context.load_verify_locations("ingserv003.crt")
    ssl_context.check_hostname = False

    # instancio el bot, le pongo el contexto ssl y la extension chatstates
    cliente = MiBot(jid, clave)
    cliente.ssl_context = ssl_context
    cliente.register_plugin("xep_0085")

    # me conecto al servidor y arranco el bucle de eventos (se para con ctrl-c)
    cliente.connect((ip, puerto))
    cliente.process(forever=True)
