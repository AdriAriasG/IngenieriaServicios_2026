# imprimo sin(x) para x entre 0 y pi a intervalos de 0.1
import math

x = 0.0
while x <= math.pi:
    print(x, math.sin(x))
    x = x + 0.1
