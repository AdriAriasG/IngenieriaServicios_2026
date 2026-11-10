# modulo con la funcion seno() del ejercicio 3
import math

def seno():
    """devuelve una lista con sin(x) para x entre 0 y pi a intervalos de 0.1

    no recibe parametros; se puede importar desde otro programa con import seno
    """
    valores = []
    x = 0.0
    while x <= math.pi:
        valores.append(math.sin(x))
        x = x + 0.1
    return valores

# si ejecuto el fichero directamente, pruebo la funcion
if __name__ == "__main__":
    print(seno())
