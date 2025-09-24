# 1)
print("Variable depentiente : Energía utilizada (en kWh)")
print("Variable independiente : Cantidad de servidores (en Unidades)")

# 2)
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fsolve

def E(x):
    return 200*np.sqrt(x) + 500

x = np.arange(0, 200, 0.1)
plt.plot(x, E(x), label = 'Energía utilizada')
plt.title('Relación entre la energía utilizada y la cantidad de servidores activos')
plt.ylabel('Energía utilizada (en kWh)')
plt.xlabel('Cantidad de servidores activos (en Unidades)')
plt.grid(True)
plt.show()

# 3)
print(f"La energía utilizada con 25 servidores activos es de {E(25)} kWh")

# 4)
def S(x):
    return (200*np.sqrt(x) + 500) - 1900

xo = np.linspace(0, 100, 10)
solucion = fsolve(S, xo)

print(f"Si la energía utilizada no debe superar los 1900 kWh debe tener como maximo {solucion[0]:.0f} servidores activos")