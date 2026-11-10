# igual que el ejercicio 1 pero guardo los valores en una lista y la imprimo al final
import math

valores = []
x = 0.0
while x <= math.pi:
    valores.append(math.sin(x))
    x = x + 0.1
print(valores)
