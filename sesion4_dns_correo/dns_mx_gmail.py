# muestro las maquinas que reciben el correo de gmail.com (registros MX) con su ip,
# en el orden en que un MTA las probaria: de menor a mayor numero de prioridad
import dns.resolver

# en el guion es query(); en dnspython 2 esa funcion esta obsoleta y se llama resolve()
respuesta = dns.resolver.resolve('gmail.com', 'MX')

# guardo parejas (prioridad, maquina); al ordenar una lista de tuplas se ordena por el primer valor
servidores = []
for mx in respuesta:
    servidores.append((mx.preference, mx.exchange))
servidores.sort()

for prioridad, maquina in servidores:
    # exchange solo da el nombre de la maquina; hago otra consulta para sacar su ip
    ips = dns.resolver.resolve(maquina)
    print(prioridad, maquina, ips[0].address)
