# 1)
print("Orden de M = 2 X 2")
print("Orden de Q = 2 X 3")

# 2)
print("------------------------------")
print("Solo es posible calcular la matriz G. La cantidad de columnas de M y la cantidad de filas de Q son iguales, en cambio no tienen las mismas cantidades de filas y columnas si quieres sacar H")

# 3)
print("------------------------------")
import numpy as np
M = np.array([[9, 14],
              [4, 5]])
Q = np.array([[200, 240, 220],
              [175, 210, 215]])
G = np.dot(M, Q)
print(G)
print("El elemento G_23 es 1955. Representando que durante la tercera semana se utilizaron 1955 resistores para la fabricación de ambos modelos")
print("El elemento G_12 es 5100. Representando que durante la segunda semana se utilizaron 5100 transistores para la fabricación de ambos modelos")

# 4)
print("------------------------------")
resistores = np.sum(G[1,:])
print(f"e utilizaron {resistores} resistores durante las tres semanas")