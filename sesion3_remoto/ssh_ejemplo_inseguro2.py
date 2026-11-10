# igual que el inseguro pero con WarningPolicy: acepta la clave pero avisa por pantalla
import getpass
import paramiko
import time

client = paramiko.SSHClient()
# admito la clave que mande el servidor, pero saco un aviso si no la conocia
client.set_missing_host_key_policy(paramiko.WarningPolicy())
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
