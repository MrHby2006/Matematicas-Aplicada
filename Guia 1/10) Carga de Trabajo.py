# 1) Variable dependiete : La carga de trabajo que puede ser modelada (En porcentaje)
#    Variable independiente : El tiempo transcurrido desde que inicio el proyecto (En semanas)

# 2)
import numpy as np
t1 = 0
def W(t):
    100 * np.exp(-0.1 * t)
print(f"Al inicio del proyecto el porcentaje es de {W(t1):.f}%")

# 3)
t2 = 4
def W(t):
    100 * np.exp(-0.1 * t)
print(f"Despues de 4 semanas el porcentaje es de {W(t2):.f}%")

# 4)
t3 = 12
def W(t):
    100 * np.exp(-0.1 * t)
print({W(t3)}) #Falso

# 5)
print("Para que el porcentaje este al 55% deben paras casi 6 semanas aproximadamente")

# 6)
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

def W(t):
    100 * np.exp(-0.1 * t)

t = np.arange(0, 12, 0.1)
plt.plot(t, W(t), label = 'W(t)')
plt.title('Relación entre la carga de trabajo en Porcentaje y el tiempo transcurrido en Semanas')
plt.ylabel('Energía (En Porcentaje %)')
plt.xlabel('Tiempo (En Semanas)')
plt.grid(True)
plt.show()