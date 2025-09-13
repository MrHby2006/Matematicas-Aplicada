# 1)
import numpy as np
import matplotlib.pyplot as plt
def C1(t):
    return 12*t + 50
def C2(t):
    return 8*t + 110

t = np.arange(0, 15, 0.1)
plt.plot(t, C1(t), color = "black", label = 'Empresa 1')
plt.plot(t, C2(t), color = "grey", label = 'Empresa 2')
plt.title('Relación entre el costo de un proyecto y el tiempo')
plt.ylabel('Costo del proyecto (en Millones de Pesos)')
plt.xlabel('Tiempo (en Semanas)')
plt.grid(True)
plt.legend()
plt.show()

# 2)
from scipy.optimize import fsolve
def C1(t):
    return 12*t + 50 - 155

xo = np.linspace(0, 100, 1)
solucion = fsolve(C1, xo)
print(f"Si se pagaron 155 millones de pesos en el proyecto en la empresa 1, pasaron {solucion[0]:.0f} semanas")

# 3)
print("Segun el grafico del ejercicio 1, combiene desarrollar el proyecto de la empresa 1 en la semana 0, ya que costara lo mínimo")
print("Y con el proyecto de la empresa 2 tambien combiene desarrollar el proyecto en la semana 0, ya que tambien su coste será el mínimo")