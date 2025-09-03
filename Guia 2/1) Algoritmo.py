# 1) Variable dependiente : Tiempo de ejecución (Ms)
#    Variable independiente : Cantidad de elementos de entrada(Unidades)

# 2)
import numpy as np

x = np.array([100, 200, 500, 1000, 2000])
y = np.array([2, 4, 10, 20, 40])
pendiente, intercepto = np.polyfit(x, y, 1)

print(f"La pendiente de la funión lineal es {pendiente:.2f} y el intercepto es {intercepto:.2f}")
print(f"f(x) = {pendiente:.2F}x + {intercepto:.2f}")

# 3)
def f(x):
    return 0.02*x

print(f"El tiempo de ejecución del algoritmo si la entrada es de 1500 elementos sera de {f(1500):.0f} milisegundos")

# 4)
from scipy.optimize import fsolve
def f(x):
    return 0.02*x - 50

x = np.linspace(0, 20, 1)
solucion = fsolve(f, x)
print(f"El tamaño de entrada que haría que el tiempo de ejecución sea de 50 milisegundos es de {solucion[0]:.0f} elementos")