# 1)
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fsolve

def f(x):
    return np.sqrt(500*x + 2000)

def g(x):
    return np.sqrt(800*x + 1000)

def interseccion(x):
    return f(x) - g(x)

xo = np.linspace(0, 10, 2)
solucion = np.around(fsolve(interseccion, xo),decimals = 2)
intensidad = np.unique(solucion)

print(f"El punto de equilibro ocurre en x = {intensidad}")
print(f"Cuando la intensidad es de 3.33 lux, la taza de crecimiento es igual en ambas especies: {f(3.33):.2f} mm/dia")

# 2)
def f(x):
    return np.sqrt(500*x + 2000)

def g(x):
    return np.sqrt(800*x + 1000)

x = np.arange(0, 200, 0.1)
plt.plot(x, f(x), label = 'Primera Especie')
plt.plot(x, g(x), label = 'Segunda Especie')
plt.xlim(0, 20)
plt.ylim(0, 150)
plt.title('Relación entre la tasa de crecimiento de dos especies y la intensidad de la luz')
plt.ylabel('Tasa de Crecimiento (mm/dia)')
plt.xlabel('Intensidad de la Luz (Lux)')
plt.grid(True)
plt.legend()
plt.show()