# descargo por sftp todos los ficheros (no las subcarpetas) de una carpeta remota
import base64
import getpass
import paramiko
from stat import S_ISDIR

client = paramiko.SSHClient()
# conexion segura como en ssh_ejemplo_seguro.py: registro la clave publica del servidor
key = paramiko.Ed25519Key(data=base64.b64decode(b'AAAAC3NzaC1lZDI1NTE5AAAAIH8J6TnMZh7dKTYboXaCFkGpHfcWXKjDJH9bUyr9sELB'))
client.get_host_keys().add('localhost', 'ssh-ed25519', key)
clave = getpass.getpass("Clave de alumno: ")
client.connect('localhost', username='alumno', password=clave)

# abro el canal sftp y me cambio a la carpeta que me digan
sftp = client.open_sftp()
carpeta = input("Carpeta remota: ")
sftp.chdir(carpeta)

for nombre in sftp.listdir():
    # miro en st_mode si es una carpeta; si lo es me la salto
    if S_ISDIR(sftp.stat(nombre).st_mode):
        print("Me salto la carpeta", nombre)
    else:
        # me traigo una copia con el mismo nombre a la carpeta local actual
        sftp.get(nombre, nombre)
        print("Descargado", nombre)

sftp.close()
client.close()
