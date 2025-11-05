# 1)
import numpy as np
            #  R   S
R = np.array([[50, 70], # Iquique
              [80, 110], # Santiago
              [60, 90]]) # Concepción

C = np.array([[80000], [45000]])

T = np.dot(R, C)
print(f"El costo total de instalación para cada ciudad es: \n{T}")

# 2)
print("------------------------------")
print("La ciudad que tiene un mayor costo de instalación es Santiago con 11350000 pesos")

# 3)
print("------------------------------")
C[1] = 0.9*C[1]
Costo_nuevo = np.dot(R, C)
print(f"Los nuevos costos de instalación son: \n{Costo_nuevo}")
print("Considerando el descuento los nuevos costos de instalación seran:\nIquique: $6835000\nSantiago: $10855000\nConcepción: $8445000")