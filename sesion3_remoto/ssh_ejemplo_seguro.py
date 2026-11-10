# version segura: solo me conecto si el servidor me manda la clave publica que yo ya conozco
import base64
import getpass
import paramiko
import time

client = paramiko.SSHClient()
# no fijo politica: se queda la de por defecto, que rechaza claves desconocidas
# registro la clave publica ed25519 del servidor (de /etc/ssh/ssh_host_ed25519_key.pub)
key = paramiko.Ed25519Key(data=base64.b64decode(b'AAAAC3NzaC1lZDI1NTE5AAAAIH8J6TnMZh7dKTYboXaCFkGpHfcWXKjDJH9bUyr9sELB'))
client.get_host_keys().add('localhost', 'ssh-ed25519', key)
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
