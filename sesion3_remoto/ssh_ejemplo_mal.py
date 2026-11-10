# primera version: no funciona porque paramiko no conoce la clave publica del servidor
import paramiko
import time

client = paramiko.SSHClient()
client.connect('localhost', username='alumno', password='clave-mal')
print("Conectado!!")

# ejecuto el comando remoto y me quedo con sus salidas
stdin, stdout, stderr = client.exec_command('ls')

# muestro lo que ha devuelto el comando (rstrip quita los saltos de linea)
for line in stdout:
    print(line.rstrip())
# doy tiempo a que se vacie el buffer
time.sleep(1)
client.close()
