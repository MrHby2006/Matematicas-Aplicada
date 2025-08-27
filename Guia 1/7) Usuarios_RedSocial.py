
# 1) Variable dependiente : Número de usuarios de una red social (unidad)
#    Variable independiente : Tiempo transcurrido (Meses)

# 2)
import numpy as np
def U(t):
    return 1000 / (1 + 9*np.exp(-0.5*t))


t = 12
print(f"Transcurrido {t} meses, la red social tiene {U(t):.0f} usuarios")

# 3)
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
t = np.arange(0, 24, 0.1)
plt.plot(t, U(t), label = 'U(t)')
plt.title('Relacion entre la cantidad de usuarios y el tiempo transcurrido en meses')
plt.ylabel('Cantidad de usuarios (Unidades)')
plt.xlabel('Tiempo (Meses)')
plt.grid(True)
plt.show()

# 4)
from scipy.optimize import fsolve

def U(t):
    return 1000 / (1 + 9*np.exp(-0.5*t))-800

t = np.linspace(0, 25, 1)
sol = fsolve(U, t)

print(f"La red social llego a los 800 usuarios transcurridos {sol[0]:.0f} meses aproximadamente")