# acepto a ciegas cualquier clave del servidor (AutoAddPolicy): funciona pero es inseguro
import getpass
import paramiko
import time

client = paramiko.SSHClient()
# admito y guardo en memoria la clave que mande el servidor, sin preguntar
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# pido la clave al usuario en vez de escribirla en el codigo
clave = getpass.getpass("Clave de alumno: ")
client.connect('localhost', username='alumno', password=clave)
print("Conectado!!")

# ejecuto el comando remoto y me quedo con sus salidas
stdin, stdout, stderr = client.exec_command('ls')

# muestro lo que ha devuelto el comando (rstrip quita los saltos de linea)
for line in stdout:
    print(line.rstrip())
# doy tiempo a que se vacie el buffer
time.sleep(1)
client.close()
