
# 1) Variable dependiente : Tiempo de ejecución de un algoritmo ordenador (Segundos)
#    Variable independiente : Cantidad de elementos a ordenar (Unidades)

# 2) Dom A(n) = [0, 1562]

# 3)
import numpy as np
from scipy.optimize import fsolve

def A(n):
    return 0.01 * n**2 + 0.5 * n + 2

print(f"Se ordenaron 1200 elementos transcurridos {A(1200):.0f} segundos")

# 4)
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
n = np.arange(0, 1562, 0.1)
plt.plot(n, A(n), label = 'A(n)')
plt.title('Relacion entre el tiempo en segundos de un algoritmo de ordenacion y la cantidad de elementos que puede ordenar')
plt.ylabel('Tiempo (Segundos)')
plt.xlabel('Elementos (Unidad)')
plt.grid(True)
plt.show()

# 5)
segundos = 6 * 3600
print(segundos)

def A(n):
    return 0.01 * n**2 + 0.5 * n + 2 - 21600

n = np.linspace(0, 1563, 10)
sol = fsolve(A, n)

print(f"Luego de 6 horas de funcionamiento el algoritmo ordena {sol[0]:.0f} elementos")