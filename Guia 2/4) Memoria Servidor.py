# 1) Variable dependiente : El uso de memoria de un servidor (en GB)
#    Variable independiente : El número de usuarios activos (en Unidades)

# 2)
print("EL uso de memoria aumenta 0.5 GB por cada usuario activo")

# 3)
print("La memoria sera de 2 GB, ya que si se multiplica 0.5 X 0, dara 0, dejando solo el 2")

# 4)
import numpy as np
def M(x):
    return 0.5*x + 2

print(f"La memoria del servidor usada cuando hay 637 usuarios es de {M(637):.1f}")

# 5)
def M(x):
    return 0.5*x + 2 - 32
from scipy.optimize import fsolve
xo = np.linspace(0, 1000, 1)
solucion = fsolve(M, xo)
print(f"Para usar 32 GB se requiere {solucion[0]:.0f} usuarios activos")

# 6)
def M(x):
    return 0.5*x + 2 - 59.8
from scipy.optimize import fsolve
xo = np.linspace(0, 1000, 1)
solucion = fsolve(M, xo)
print(f"Para usar 59.8 GB se requiere {solucion[0]} usuarios activos")
print("No es posible tener el uso de memoria de 59.8 GB ya que el número de usuaros requeridos es decimal")