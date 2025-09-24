# 1)
print("La forma algebraica del sueldo mensual de la ofreta recibia es SO(x) = 500 * 1.07**x")

# 2)
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fsolve

def SA(x):
    return 600 * 1.05**x

def SO(x):
    return 500 * 1.07**x

x = np.arange(0, 30, 0.1)
plt.plot(x, SA(x), color = "black", label = 'Sueldo Actual')
plt.plot(x, SO(x), color = "green", label = 'Sueldo Oferta')
plt.ylim(400, 2500)
plt.xlim(0, 35)
plt.title('Relación entre los sueldos y la cantidad de casas vendidas')
plt.ylabel('Sueldo Ganado (en Miles de Pesos)')
plt.xlabel('Cantidad de Casas Vendidas en un Mes (en Cantidad)')
plt.grid(True)
plt.legend()
plt.show()

def interseccion(x):
    return SO(x) - SA(x)

xo = np.linspace(0, 40, 2)
solucion = np.around(fsolve(interseccion, xo),decimals = 0)

casas = np.unique(solucion)
print(f"El punto de equilibrio ocurre en x = {casas}")
print("El punto de equilibrio ocurre en x = 10")

# 3)
print("Si vende menos de 10 casas, le combiene el sueldo actual, pero si vende mas de 10 casas le combiene el sueldo nuevo")