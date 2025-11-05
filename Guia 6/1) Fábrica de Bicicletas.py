# 1)
print("Orden A = 2 X 2")
print("Orden B = 2 X 2")
print("Si es posible multiplicar porque la cantidad de filas de la matriz A coincide con el número de columnas de la matriz B")

# 2)
print("-----------------------------------")
import numpy as np
A = np.array([[1, 2], [3, 2]])
B = np.array([[290, 312], [345, 413]])
C = np.dot(A,B)
print(C)

# 3)
print("-----------------------------------")
print("El elemento C_21 es 1560. Representa que en Enero se utilizaron 1560 kg de aluminio para la construcción de ambos modelos de bicicletas")
print("El elemento C_11 es 980. Representa que en Enero se utilizaron 980 kg de acero para la construcción de ambos modelos de bicicletas")