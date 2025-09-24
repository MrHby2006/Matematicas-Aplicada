# 1)
print("La función I(x) indica que al inicio de la campaña el ingreso por las ventas es $1_000_000 (El intercepto es 1_000). A medida que las semanas aumentas el ingreso por las ventas diminuye en $20_000 pesos por semana (Pendiente es -20)")
print("La función C(x) indica que al inicio de la campaña el costo por inversión es de $500_000 (Intercepto es 500). A medida que las semanas aumentan el costo por inversión aumenta en $200_000 por semana (Pendiente es de 200)")

# 2)
import numpy as np
import matplotlib.pyplot as plt

def I(x):
    return -20*x + 1000

def C(x):
    return 200*x + 500

x = np.arange(0, 200, 0.1)
plt.plot(x, I(x), color = "green", label = 'Ingreso')
plt.plot(x, C(x), color = "red", label = 'Costo')
plt.xlim(0, 7)
plt.ylim(500, 1250)
plt.title('Relación entre el ingreso y Costo en función del tiempo')
plt.ylabel('Ingresos y Costos de inversión (en Miles de Pesos)')
plt.xlabel('EL tiempo (en Semanas)')
plt.grid(True)
plt.legend()
plt.show()

# 3)
from scipy.optimize import fsolve

def interseccion(x):
    return I(x) - C(x)

xo = np.linspace(0, 20, 5)
solucion = np.around(fsolve(interseccion, xo),decimals = 1)
semana = np.unique(solucion)

print(f"EL punto de equiibrio ocurre cuando x = {semana}")
print(f"Cuando han transcurrido {semana[0]} semanas el ingreso y el costo por inversión son iguales : ${I(2.3):.0f} miles de pesos")

# 4)
print("Aconsejariamos no continuar con la campaña, ya que transcurridas 2.3 semanas los costos de inversión comienzan a superar los ingresos, por lo que no conviene continuar con la campaña despues de la semana 2")