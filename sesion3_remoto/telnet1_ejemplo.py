# ejemplo de la documentacion de telnetlib, cambiado para listar /home
import getpass
import telnetlib
import time

HOST = "localhost"
# pido el usuario y la clave de la maquina remota
user = input("Enter your remote account: ")
password = getpass.getpass()

# me conecto al puerto 23; telnetlib se ocupa de la negociacion
tn = telnetlib.Telnet(HOST)

# espero a que me pida el login y se lo mando
tn.read_until(b"login: ")
tn.write(user.encode('ascii') + b"\n")
# si hay clave espero a que la pida y se la mando
if password:
    tn.read_until(b"Password: ")
    tn.write(password.encode('ascii') + b"\n")

# espero a que termine el login: lo que escriba antes de que salga el shell se pierde
time.sleep(1)

# lanzo el comando y cierro el shell remoto
tn.write(b"ls /home\n")
tn.write(b"exit\n")

# leo todo hasta que se cierra la conexion y lo muestro
print(tn.read_all().decode('utf-8'))
