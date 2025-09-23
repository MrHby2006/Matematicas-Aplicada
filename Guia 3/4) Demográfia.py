# 1)
print("Dom C(x): [0, 63]")
print("Dom E(x): [0, 63]")
print("Dom H(x): [0, 63]")

# 2)
import numpy as np
import matplotlib.pyplot as plt

def C(x):
    return 19493*np.exp(0.01*x)

def E(x):
    return 17575*np.exp(0.012*x)

def H(x):
    return 10117*np.exp(0.015*x)

x = np.arange(0, 65, 0.1)
plt.plot(x, C(x), color = "red", label = 'Chile')
plt.plot(x, E(x), color = "yellow", label = 'Ecuador')
plt.plot(x, H(x), color = "blue", label = 'Honduras')
plt.title('Relación entre la población entre Chile, Ecuador y Honduras')
plt.ylabel('Población en Miles de Habitantes')
plt.xlabel('Tiempo transcurrido desde 1960 en Años')
plt.grid(True)
plt.legend()
plt.show()

# 3)
print(f"Según el modelo a inicios de 1960 la población de Chile era de {C(0):.0f} mil de habitantes")
print(f"Según el modelo a inicios de 1960 la población de Ecuador era de {E(0):.0f} mil de habitantes")
print(f"Según el modelo a inicios de 1960 la población de Honduras era de {H(0):.0f} mil de habitantes")

# 4)
print("------------------------------------------------------------------------------------------------")
print(f"Según el modelo en el año 2000 la población de Chile era de {C(40):.0f} mil de habitantes")
print(f"Según el modelo en el año 2000 la población de Ecuador era de {E(40):.0f} mil de habitantes")
print(f"Según el modelo en el año 2000 la población de Honduras era de {H(40):.0f} mil de habitantes")

# 5)
from scipy.optimize import fsolve

def interseccion(x):
    return  C(x) - E(x)

xo = np.linspace(0, 20, 1)
solucion = fsolve(interseccion, xo)
unica = np.unique(solucion)

print("------------------------------------------------------------------------------------------------")
print(f"La pobración de Ecuador supera a la de Chile en el año {1960+unica[0]:.0f} aproximadamente")

# 6)
def interseccio(x):
    return  C(x) - H(x)

xo = np.linspace(0, 20, 1)
solucio = fsolve(interseccio, xo)
unica = np.unique(solucio)
print("------------------------------------------------------------------------------------------------")
print(f"La pobración de Honduras es igual a la de Chile transcurridos {1960+unica[0]:.0f} años")
print("EL valor encontrado esta fuera del domino contextualizado, por lo tanto, la solución no es valida para el problema")