# igual que telnet1_ejemplo.py pero descarto el mensaje de bienvenida
import getpass
import telnetlib

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

# leo y descarto la bienvenida hasta el prompt, que acaba en $
tn.read_until(b"$")

# lanzo el comando y leo hasta el siguiente prompt: eco del comando y su salida
tn.write(b"ls /home\n")
salida = tn.read_until(b"$")
print(salida.decode('utf-8'))

# cierro el shell remoto
tn.write(b"exit\n")
tn.close()
