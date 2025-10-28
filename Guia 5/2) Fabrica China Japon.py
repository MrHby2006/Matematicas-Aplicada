# 1
print("EL orden de la matriz J y C es 5 X 3")

# 2
print("------------------------------")
print("J_21 = 120 El costo de producción mensual del 1er tipo de componente para el 2do modelo de computador es de 120000 dolares")
print("C_12 = 190 El costo de producción mensual del 2do tipo de componente para el 1er modelo de computador es de 190000 dolares")

# 3
print("------------------------------")
import numpy as np
J = np.array([[100, 200, 150],
              [120, 210, 170],
              [112, 200, 131],
              [124, 310, 170],
              [136, 156, 140]])

C = np.array([[110, 190, 160],
              [130, 220, 180],
              [146, 190, 141],
              [143, 312, 163],
              [137, 116, 156]])
T = J + C
print(f"El costo total de producción considerando ambas sucursales es de: \n{T}")

# 4
print("------------------------------")
print("Es correcto, en Japon el costo del componente 3 del modeo 4 es de 170000 dolares y en China es de 163000 dolares, por \nlo tanto, el costo de Japon es 7000 dolares mas caro que en China")