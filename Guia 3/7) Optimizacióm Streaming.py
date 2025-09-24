# 1)
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fsolve

def I(x):
    return 10*x**2 + 50*x

def C(x):
    return 5*x**2 + 80*x + 100

def interseccion(x):
    return I(x) - C(x)

xo = np.linspace(0, 10, 2)
solucion = np.around(fsolve(interseccion, xo),decimals = 1)
suscriptores = np.unique(solucion)

print(f"El punto de equilibro ocurre en x = {suscriptores}")
print(f"Cuando la plataforma tiene 8.4 mil suscriptores, el ingreso y el csto son iguales a {I(8.4)} mil pesos")

# 2)
def I(x):
    return 10*x**2 + 50*x

def C(x):
    return 5*x**2 + 80*x + 100

x = np.arange(0, 200, 0.1)
plt.plot(x, I(x), color = "blue", label = 'Ingreso por suscriptor')
plt.plot(x, C(x), color = "red", label = 'Costo de operación')
plt.xlim(0, 20)
plt.ylim(0, 4000)
plt.title('Relación entre los ingresos y costos en función de cantidad de suscriptores')
plt.ylabel('Ingreso y Costos (miles de pesos)')
plt.xlabel('Cantidad de suscriptores (miles)')
plt.grid(True)
plt.legend()
plt.show()

print("Cuando la plataforma de streaming tiene meso de 8400 (8.4 mil) suscriptores los costos de operación superan a los ingresos por suscripción")