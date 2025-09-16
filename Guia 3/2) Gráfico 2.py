# 1)
import numpy as np
import matplotlib.pyplot as plt

def h(x):
    return 2 * (x - 2)**2

def i(x):
    return x + 1

x = np.arange(-5, 50, 0.01)
plt.plot(x, h(x),color = "lime", label = 'h(x)')
plt.plot(x, i(x),color = "yellow", label = 'i(x)')
plt.xlim(-2,5)
plt.ylim(-1,10)
plt.title('Comparativo entre dos Funciones')
plt.ylabel('Y')
plt.xlabel('X')
plt.grid(True)
plt.legend()
plt.show()

# 2)
from scipy.optimize import fsolve
def h(x):
    return 2 * (x - 2)**2

def i(x):
    return x + 1

xo = np.linspace(0, 15, 1)
solucion_h = fsolve(h, xo)
solucion_i = fsolve(i, xo)

print(f"La función h(x) intersecta al eje x en {solucion_h[0]:.0f} y la función i(x) en {solucion_i[0]:.0f}")
print("Representado seria (0,2) y (0,-1)")

# 3)
def inter(x):
    return i(x) - h(x) 

xo = np.linspace(0, 15, 1)
solucion = np.around(fsolve(inter, xo),decimals = 2)
interseccion = np.unique(solucion)
print(f"Los puntos de intersección de las funciones en x son: {interseccion}")
print(f"h(1) = {h(1):.2f}")
print(f"i(3.5) = {i(3.5):.2f}")
print("Las funciones h(x) e i(x) se intersectan en los puntos (1,2) y (3.5,4.5)")

# 4)
print("En base al gráfico y al desarrollo de la pregunta anterior podemos concluir que la función h(x) es menor o igual que i(x) desde x = 1 hasta x = 3.5")

# 5)
def S(x):
    return h(x) - 50

xo = np.linspace(-200, 200, 50)
solucion = np.around(fsolve(S, xo),decimals = 2)
interseccion = np.unique(solucion)

print(f"La función h(x) = 50 en x = {interseccion}")
print("La fucnión h(x) es igual a 50 en los puntos (-3,50) y (7,50)")