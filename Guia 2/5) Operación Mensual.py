# 1) Variable dependiente : El costo de operación mensual de un data center (en Miles de Dolares)
#    Variable independiente : El número de servidores (en Unidades)

# 2)
print("El número al lado de x es 1.5, por ende la pendiente crecera el costo de operación mensual 1.5 por cada servidor")

# 3)
print("El número de intercepto es 10, por ende el costo de operaciones es de 10000 dolares")

# 4)
import numpy as np
def C(x):
    return 1.5*x + 10
print(f"El costo operacional mensual cuando hay 47 servidores es de {C(47)} mil dolares")

# 5)
from scipy.optimize import fsolve
def C(x):
    return 1.5*x + 10 -92.5

xo = np.linspace(0, 1000, 1)
solucion = fsolve(C, xo)
print(f"Para que el costo sea de 92500 dolares se requiere de {solucion[0]:.0f} servidores")