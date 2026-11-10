# version segura contra el servidor ssh de otro nodo (el de otro alumno)
import base64
import getpass
import paramiko
import time

# datos del otro nodo: su ip, su clave publica ed25519 (su /etc/ssh/ssh_host_ed25519_key.pub)
# y el usuario con el que entro
servidor = '192.168.0.63'
clave_publica = b'AAAAC3NzaC1lZDI1NTE5AAAAIH8J6TnMZh7dKTYboXaCFkGpHfcWXKjDJH9bUyr9sELB'
usuario = 'alumno'

client = paramiko.SSHClient()
# no fijo politica: se queda la de por defecto, que rechaza claves desconocidas
# registro la clave publica del otro nodo con su ip, que es como me voy a conectar
key = paramiko.Ed25519Key(data=base64.b64decode(clave_publica))
client.get_host_keys().add(servidor, 'ssh-ed25519', key)
# pido la clave del usuario en ese nodo (puede no ser la misma que la mia)
clave = getpass.getpass("Clave de %s en %s: " % (usuario, servidor))
client.connect(servidor, username=usuario, password=clave)
print("Conectado!!")

# ejecuto el comando remoto y me quedo con sus salidas
stdin, stdout, stderr = client.exec_command('ls')

# muestro lo que ha devuelto el comando (rstrip quita los saltos de linea)
for line in stdout:
    print(line.rstrip())
# doy tiempo a que se vacie el buffer
time.sleep(1)
client.close()
