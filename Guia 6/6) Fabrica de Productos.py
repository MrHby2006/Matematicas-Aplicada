# 1)
import numpy as np
#            Bodega 1 Bodega 2 Bodega 3 Bodega 4 Bodega 5
T = np.array([[500,     400,      300,     200,     100],# Planta 1
              [600,     500,      400,     300,     200],# Planta 2
              [700,     600,      500,     400,     300],# Planta 3
              [800,     700,      600,     500,     400]])# Planta4
#             Ene Feb Mar Abr May Jun
C = np.array([[5,  6,  7,  8,  9,  6],# Bodega 1
              [4,  5,  6,  7,  8,  7],# Bodega 2
              [3,  4,  5,  6,  7,  9],# Bodega 3
              [2,  3,  4,  5,  6,  6],# Bodega 4
              [8,  5,  6,  3,  7,  5]])# Bodega 5
G = np.dot(T, C)

print(f"La matriz G es: \n\n{G}")

# 2)
print("---------------------")
print("El elemento T_14 es 200. Mensualmente se transportan 200 unidades del producto desde la planta 1 hasta bodega 4")
print("El elemento C_53 es 6. El costo unitario de almacenar el producto en la bodega 5 en el mes de Marzo es de 6 dolares")
print("El elemento G_35 es 19100. El costo total de almacenamiento de la producción mensual de la planta 3 en el mes de Mayo es de 19100 dolares")

# 3)
print("---------------------")
print("Almacenar una unidad del producto en la bodega 4 durante Marzo de este año es de 4 dolares")

# 4)
print("---------------------")
print("La empresa gasta 12800 por almacenar la producción mensual de la planta 2 en el mes de Abril")