# 1) Variable dependiente : EL número de visitas diarias de un sitio web (en Unidades)
#    Variable independiente : El número de campañas publicitarias (en Unidades)

# 2)
print("Dom V(x) = [0, 20]")

# 3)
print("El número de visitantes en el sitio web aumenta en 300 por cada campaña publicitaria")

# 4)
def V(x):
    return 300*x + 500

print(f"Si se ejecutan 5 campañas puclicitarias el númeeo de visitas diarias sera de {V(5)}")

# 5)
import numpy as np
from scipy.optimize import fsolve
def V(x):
    return 300*x + 500 - 4700

xo = np.linspace(0, 1000, 1)
solucion = fsolve(V, xo)
print(f"Si se quieren alcanzar las 4700 visits diarias, se deben ejecutar {solucion[0]:.0f} campañas publicitarias")