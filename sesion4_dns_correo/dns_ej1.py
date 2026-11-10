# primera prueba de dnspython: ip de en.wikipedia.org y la respuesta del servidor
import dns.resolver

# en el guion es query(); en dnspython 2 esa funcion esta obsoleta y se llama resolve()
respuesta = dns.resolver.resolve('en.wikipedia.org')
print(respuesta[0].address)

# respuesta completa del servidor dns, en forma legible
print(respuesta.response)

# la misma respuesta en el formato binario del protocolo (solo por curiosidad)
print(respuesta.response.to_wire())
