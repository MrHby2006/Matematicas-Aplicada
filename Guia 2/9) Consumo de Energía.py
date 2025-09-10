# 1)
import numpy as np
x = np.array([0, 10, 20, 30, 40, 50])
y = np.array([500, 400, 300, 200, 100, 0])

pendiente, intercepto = np.polyfit(x, y, 1)
print(f"E(t) = {pendiente:.0f}*t + {intercepto:.0f}")

# 2)
print("La pendiente m = -10, por ende el consumo de energía disminuye 10kWh por cada mes desde la optimización")

# 3)
from scipy.optimize import fsolve
def E(t):
    return -10*t + 500

print(f"Luego de un año el consumo de energía despues de la implementación de la optimización es de {E(12)} kWh por hora")

# 4)
def E(t):
    return -10*t + 500 - 200

xo = np.linspace(0, 100, 1)
solucion = fsolve(E, xo)
print(f"Si el consumo de energía es de 200 kWh transcurieron {solucion[0]:.0f} meses")