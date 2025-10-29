# 1)
import numpy as np
V = np.array([[30, 34, 20],
              [45, 20, 16],
              [14, 26, 25]])

T = np.array([[35, 30, 26],
              [52, 25, 18],
              [23, 24, 32]])

A = V + T
print(f"La producción mensual total de ambas plantas es de: \n{A}")

# 2)
print("---------------------------------")
print("EL elemento A_21 es 97, en un mes, ambas plantas de la empresa fabricadora de zapatos produjeron 97000 pares de zapatos negros para niños")

# 3)
print("---------------------------------")
V1 = V * 1.3
T1 = T * 0.9
B = V1 + T1
print(f"La producción mensual total de ambas plantas para el prximo año es de: \n{B}")

# 4)
print("---------------------------------")
print("EL elemento B_13 es 49.4, en un mes, ambas plantas de la empresa fabricadora de zapatos produjeron 49400 pares de zapatos blancos para caballeros")