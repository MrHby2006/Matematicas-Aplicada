# 1) Variable dependiente : Tiempo de transferencia (Min)
#    Variable independiente : Volumen de los datos transferidos (GB)

# 2)
import numpy as np
x = np.array([5, 10, 25, 50, 100])
y = np.array([10, 20, 50, 100, 200])
pendiente, intercepto = np.polyfit(x, y, 1)

print(f"La pendiente de la funión lineal es {pendiente:.2f} y el intercepto es {intercepto:.2f}")
print(f"f(x) = {pendiente:.2F}x + {intercepto:.2f}")

# 3)
print("Pendiente = 2 \nLa pendiente aumentara 2 minutos por cada GB de datos a transferir")

# 4)
def T(x):
    return 2*x

print(f"El tiempo de transferencia de 73.2 GB es de {T(73.2):.1f} minutos")

# 5)
from scipy.optimize import fsolve
def T(x):
    return 2*x - 123.5
x = np.linspace(0, 20, 1)
solucion = fsolve(T, x)
print(f"La cantidad de datos que se pueden transferir en 123.5 minutos es de {solucion[0]:.1f} GB")

# 6)
import matplotlib.pyplot as plt

def T(x):
    return 2*x

x = np.arange(0, 200, )
plt.plot(x, T(x), label = 'T(x)')
plt.title('Relación entre el tiempo de transferencia y el volumen de datos')
plt.ylabel('Tiempo de transferencia (Min)')
plt.xlabel('Volumen de datos (GB)')
plt.grid()
plt.show()