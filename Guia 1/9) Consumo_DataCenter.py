# 1) Variable dependiente : El consumo de energía de un Data Center (En kWh)
#    Variable independiente : El tiempo desde el inicio del monitoreo (En Hrs)

# 2)
import math
def E(t):
    return 50 * math.log(t + 1) + 200 

print(f"Luego de 5 horas, se a consumido {E(5):.0f} kWh")

# 3)
import math
def E(t):
    return 50 * math.log(t + 1) + 200 - 350
print(f"Se necesitan {E(t):.0f} horas para llegar a los 350 kWh")

# 4)
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

def E(t):
    return 50 * math.log(t + 1) + 200 

t = np.arange(0, 350, 0.1)
plt.plot(t, E(t), label = 'E(t)')
plt.title('Relación entre el consumo de energía de un Data Center en kWh y el tiempo de monitoreo en Hrs')
plt.ylabel('Energía (En kWh)')
plt.xlabel('Tiempo (En Hrs)')
plt.grid(True)
plt.show()