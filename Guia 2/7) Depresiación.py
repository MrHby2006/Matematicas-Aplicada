# 1) Variable dependiente : El valor residual (en Miles de Dolares)
#    Variable independiente : La antigüedad del equipo (en Años)

# 2)
print("El valor al lado de t es -1.2, por ende el valor residual disminuye 1.2 mil dolares (1200) por cada año")

# 3)
print("El valor residual inicial es de 10000 ya que el coeficiente de posición (intercepto) es 10")

# 4)
import numpy as np
from scipy.optimize import fsolve

def R(t):
    return -1.2*t + 10 - 0.4

xo = np.linspace(0, 1000, 1)
solucion = fsolve(R, xo)
print({solucion[0]})
print("Dom R(t) = [0, 8]")

# 5)
def R(t):
    return -1.2*t + 10

print(f"El valor residual luego de 3 años y 6 meses será de {R(3.5)} mies de dolares")

# 6)
def R(t):
    return -1.2*t + 10 - 4

xo = np.linspace(0, 1000, 1)
solucion = fsolve(R, xo)
print(f"Si el valor residual es de 4000 dolares el equipo tiene {solucion[0]} años de antigüedad")

# 7)
import matplotlib.pyplot as plt

def R(t):
    return -1.2*t + 10

t = np.arange(0, 8, 1)
plt.plot(t, R(t), label = 'R(t)')
plt.title('Valor residual segun la Antigüedad(Miles de Dolares)')
plt.ylabel('Valor residula (en Miles de Dolares)')
plt.xlabel('Años de Antigüedad (en Años)')
plt.grid()
plt.show()