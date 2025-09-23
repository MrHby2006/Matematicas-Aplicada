# 1)
import numpy as np
import matplotlib.pyplot as plt

def w(x):
    return 0.6*x**2 + 1.5
def t(x):
    return 0.8*x**3 -10*x + 10

x = np.arange(-10, 10, 0.01)
plt.plot(x, w(x), color = "blue", label = 'w(x)')
plt.plot(x, t(x), color = "red", label = 't(x)')
plt.xlim(-3,4)
plt.ylim(-4,24)
plt.title('Comparativa entre dos funciones')
plt.ylabel('Y')
plt.xlabel('X')
plt.grid(True)
plt.legend()
plt.show()

# 2)
from scipy.optimize import fsolve

def interseccion(x):
    return w(x) - t(x)

x = np.linspace(-4, 4, 4)
solucion = np.around(fsolve(interseccion, x),decimals = 2)
unica = np.unique(solucion)

print(f"Los puntos de intersección de las funciones w(x) y t(x) estan en x:{unica}")
print("La función w(x) es mayor a t(x) para los valores de x mayores a 0.86 y menores a 3.47 [0.86, 3.47]")

# 3)
def S(x):
    return t(x) - 6
x = np.linspace(-4, 4, 4)
solucion = np.around(fsolve(S, x),decimals = 2)
unica = np.unique(solucion)

print(f"La función t(x) es igual a 6 en x:{unica}")