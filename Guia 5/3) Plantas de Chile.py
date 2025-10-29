# 1)
import numpy as np
C = np.array([[120, 200, 155, 125, 230],
              [155, 130, 110, 160, 180],
              [140, 205, 150, 125, 155],
              [130, 120, 230, 225, 125],
              [135, 70, 190, 175, 95],
              [110, 265, 180, 230, 180],
              [185, 85, 120, 135, 150]])

E = 0.8 * C

print(f"La producción de Ecuador es de: \n{E}")

# 2)
print("----------------------------")
print("La expresión que nos permite calcular cada elemento de la matriz T es: \n T_ij = C_ij + E_ij")

# 3)
print("----------------------------")
T = C + E
print(f"La matriz que muestra la producción total de la empresa Beta, conuiderando ambas filiales es: \n{T}")

# 4)
print("----------------------------")
print("El elemento C_34 es 125. En una semana, la filial Chilena de la empresa Beta fabrica 125 unidades del producto 3 en la planta 4")
print("El elemento T_72 es 153. En una semana, ambas filiales de la empresa Beta fabrican 153 unidades del producto 7 en la planta 2")