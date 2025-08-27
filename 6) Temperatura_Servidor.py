
# 1) Variable dependiente : Temperatura del servidor(°C).
#    Variable independiente : Tiempo transurrido (en horas) en un día laboral.

# 2) Dom T(t)=[0, 9]

# 3)

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

def T(t):
    return -0.5*t**2 + 3*t + 20

fig,ax=plt.subplots()

t = np.arange(0, 9, 0.01)
plt.plot(t, T(t), label = 'T(t)')
plt.title('Relación entre la temperatura de un servidor y el tiempo transcurrido en horas')
plt.ylabel('Temperatura (°C)')
plt.xlabel('Tiempo (Hrs)')
plt.grid(True)
plt.show()

# 4)
t1 = 3
print(f"El servidor alcanza su máxima temperatura a las 3 horas desde inicio de la jornada laboral y es de {T(t1)}°C")

# 5)
t2 = 5
print(f"El servidor alcanza una temperatura de{T(t2)}°C a las 13:00 Hrs")

t3 = 9
print(f"El servidor alcanza una temperatura de{T(t3)}°C al final de la jornada laboral")
