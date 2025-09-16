# 1)
import numpy as np
import matplotlib.pyplot as plt

def r(x):
    return -1.5*x**2 + 11.5*x - 15

def g(x):
    return 1.58*x**4 - 19.17*x**3 + 80.92*x**2 - 139.33*x + 85

x = np.arange(0, 50, 0.01)
plt.plot(x, r(x), color = "orange", label = 'r(x)')
plt.plot(x, g(x), color = "cyan", label = 'g(x)')
plt.xlim(0,6)
plt.ylim(-10,10)
plt.title('Comparativo entre dos Funciones')
plt.ylabel('Y')
plt.xlabel('X')
plt.grid(True)
plt.legend()
plt.show()

# 2)
from scipy.optimize import fsolve
def inter(x):
    return g(x) - r(x)

xo = np.linspace(0, 15, 15)
solucion = np.around(fsolve(inter, xo),decimals = 2)
interseccion = np.unique(solucion)
print(f"Los punto de intersección de ambas funciones en x son: {interseccion}")