# 1)
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fsolve

def A(t):
    return 1.4*t**4 - 2.55*t**3 - 3.37*t**2 + 2.75*t + 10

def B(t):
    return t**4 - 2.67*t**3 - t**2 + 2*t + 20

t = np.arange(0, 6, 0.1)
plt.plot(t, A(t), color = "green", label = 'Proceso A')
plt.plot(t, B(t), color = "yellow", label = 'Proceso B')
plt.title('Relación entre Eficiencia de Modelos de Filtrado y el Tiempo')
plt.ylabel('Eficiencia de Filtrado (Porcentaje)')
plt.xlabel('Tiempo (Horas)')
plt.grid(True)
plt.legend()
plt.show()

# 2)
print(f"La eficiencia del Proceso A después de 3 horas y media es: {A(3.5):.2f}%")
print(f"La eficiencia del Proceso B después de 3 horas y media es: {B(3.5):.2f}%")

# 3)
def interseccion(t):
    return A(t) - B(t)

xo = np.linspace(3, 3.5, 1)
solucion = fsolve(interseccion, xo)
eficiencia_en_solucion = solucion[0]

print(f"El proceso A tiene la misma eficiencia que el B en {solucion[0]:.2f} horas.")
print(f"La eficiencia en ese punto es de {eficiencia_en_solucion:.2f}%.")

# 4)
print("Combiene el proceso B entre las 0 y 2.77 horas, despues de eso es mas combeniente el proceso A")