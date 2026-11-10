# funcion que cuenta cuantas veces aparece cada vocal en una cadena

def contar_vocales(cadena):
    "devuelvo un diccionario con las vocales como claves y sus repeticiones como valores"
    resultado = {"a": 0, "e": 0, "i": 0, "o": 0, "u": 0}
    # recorro la cadena en minusculas letra a letra
    for letra in cadena.lower():
        # si la letra es una de las claves del diccionario, sumo uno
        if letra in resultado:
            resultado[letra] = resultado[letra] + 1
    return resultado

txt = "Esto es una prueba. Esta cadena contiene vocales variadas"
result = contar_vocales(txt)
print(result)
