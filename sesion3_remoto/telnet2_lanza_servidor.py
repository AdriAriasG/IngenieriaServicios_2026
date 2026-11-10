# entro por telnet y arranco udp_servidor3_con_ok.py si no estaba ya en ejecucion
import telnetlib
import time

HOST = "localhost"
# usuario y clave incrustados en el codigo (mala practica, pero lo pide el ejercicio)
user = "alumno"
password = "alumno"

# me conecto y hago login igual que en el ejercicio 1
tn = telnetlib.Telnet(HOST)
tn.read_until(b"login: ")
tn.write(user.encode('ascii') + b"\n")
tn.read_until(b"Password: ")
tn.write(password.encode('ascii') + b"\n")

# espero al prompt: cuando llega el $ el shell remoto ya acepta comandos
tn.read_until(b"$")

# pido la lista de procesos y leo hasta el siguiente prompt
# con ww para que no corte las lineas al ancho de la terminal (80 columnas) y se vea el .py
tn.write(b"ps -efww\n")
respuesta = tn.read_until(b"$")

if b"udp_servidor3_con_ok.py" in respuesta:
    print("El servidor ya está en ejecución")
else:
    # lo lanzo con nohup para que siga vivo al cerrar telnet, y con & para recuperar el prompt
    tn.write(b"nohup python3 udp_servidor3_con_ok.py &\n")
    # le doy un segundo para que arranque
    time.sleep(1)

# cierro el shell remoto y muestro todo lo que quede por leer, para depurar
tn.write(b"exit\n")
print(tn.read_all().decode('utf-8'))
