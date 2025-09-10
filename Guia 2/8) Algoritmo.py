# 1)
import numpy as np
x = np.array([0, 20, 40, 60, 80, 100])
y = np.array([2, 3, 4, 5, 6, 7])

pendiente, intercepto = np.polyfit(x, y, 1)
print(f"T(x) = {pendiente:.2f}*X + {intercepto:.2f}")

# 2)
def T(x):
    return 0.05*x + 2

print(f"El tiempo de ejecución del algoritmo para 67 elementos de entrada es de {T(67)} milisegundos")

# 3)
from scipy.optimize import fsolve
def T(x):
    return 0.05*x + 2 - 6.4

xo = np.linspace(0, 100, 1)
solucion = fsolve(T, xo)
print(f"Si el tiempo de ejecución es de 6.4 milisegundos, se ingresaron {solucion[0]:.0f} elementos")