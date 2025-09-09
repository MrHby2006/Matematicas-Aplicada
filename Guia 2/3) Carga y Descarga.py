# 1) 
import numpy as np
tamaño = np.array([50, 100, 250, 500, 1000])
carga = np.array([10, 20, 50, 100, 200])
descarga = np.array([8, 16, 40, 80, 160])

m_carga,n_carga = np.polyfit(tamaño,carga,1)
m_descarga,n_descarga = np.polyfit(tamaño,descarga,1)

print(f"La pendiente de la función es {m_carga:.2f} y el intercepto es {n_carga:.2f}")
print(f"La pendiente de la función es {m_descarga:.2f} y el intercepto es {n_descarga:.2f}")

# 2) Función f(x):
#    Variable dependiente : Tiempo de carga (S) 
#    Variable independiente : Tamaño del archivo (MB)

#    Función g(x):
#    Variable dependiente : Tiempo de descarga (S) 
#    Variable independiente : Tamaño del archivo (MB)

# 3)
def f(x):
    return 0.2*x
print(f"El tiempo de carga para un archivo de 750 MB es de {f(750):.0f} segundos")

def g(x):
    return 0.16*x
print(f"El tiempo de descarga para un archivo de 750 MB es de {g(750):.0f} segundos")

# 4)
from scipy.optimize import fsolve
def f(x):
    return 0.2*x - 163
x = np.linspace(0, 20, 1)
solucion = fsolve(f, x)
print(f"El tamaño deñ archivo si el tiempo de carga es de 163 segundos es de{solucion[0]:.0f} MB")

# 5)
def g(x):
    return 0.16*x - 195
x = np.linspace(0, 20, 1)
solucion1 = fsolve(g, x)
print(f"El tamaño del archivo si el tiempo de descarga es de 195 segundos es de {solucion1[0]:.0f} MB") # FALSOOOOOOOOOO

# 6)
import matplotlib.pyplot as plt
tiempo = np.arange(0, 15, 0.1)
metro = 0.4*tiempo       #Como se grafican
bus = 0.3*tiempo         #dos o más variables
plt.plot(tiempo, metro, label = 'Metro')
plt.plot(tiempo, bus, label = 'Bus')
plt.title('Distancia recorrida por minutos')
plt.ylabel('Distancia(Km)')
plt.xlabel('Tiempo (M)')
plt.legend()
plt.grid(True)
plt.show()