# muestro todas las ips (registros A) asignadas a apple.com
import dns.resolver

# en el guion es query(); en dnspython 2 esa funcion esta obsoleta y se llama resolve()
respuesta = dns.resolver.resolve('apple.com')
# la respuesta se puede recorrer como una lista: un elemento por cada ip
for dato in respuesta:
    print(dato.address)
