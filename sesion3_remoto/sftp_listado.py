# listado de la carpeta del usuario en el servidor remoto usando sftp sobre ssh
import base64
import getpass
import paramiko

client = paramiko.SSHClient()
# conexion segura como en ssh_ejemplo_seguro.py: registro la clave publica del servidor
key = paramiko.Ed25519Key(data=base64.b64decode(b'AAAAC3NzaC1lZDI1NTE5AAAAIH8J6TnMZh7dKTYboXaCFkGpHfcWXKjDJH9bUyr9sELB'))
client.get_host_keys().add('localhost', 'ssh-ed25519', key)
clave = getpass.getpass("Clave de alumno: ")
client.connect('localhost', username='alumno', password=clave)

# abro un canal sftp sobre la conexion ssh ya establecida
sftp = client.open_sftp()

# sin chdir: por defecto estoy en la carpeta del usuario
listado = sftp.listdir()
for nombre in listado:
    print(nombre)

sftp.close()
client.close()
