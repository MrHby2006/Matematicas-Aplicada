# 1)
import numpy as np
#              DC1  DC2  DC3
D = np.array([[100, 150, 200],# Ene
              [120, 180, 220],# Feb
              [140, 210, 250]])# Mar
C = np.array([[50],# DC1
              [40],# DC2
              [30]])# DC3
T = np.dot(D,C)

print(f"El costo total de almacenamiento por es es \n\n{T}")

# 2)
print("-----------------------")
print("La afirmación que hace el trabajador no es cierta ya que el costo total es mas alto en Marzo que en Febrero")

# 3)
print("-----------------------")
T_nuevo = np.dot(D, 1.023 * C)
print(f"El nuevo costo total de almacenamiento por mes es: \n\n{T_nuevo}")