# 1
print("EL orden de la matriz A y B es 3 X 4")

# 2
print("------------------------------")
import numpy as np
A = np.array([[2.6, 4.8, 1.8, 0.9],
              [3.2, 4.4, 2.5, 2.8],
              [2.4, 3.6, 3.8, 2.5]])
B = np.array([[3.6, 2.5, 3.0, 2.5],
              [4.5, 5.0, 3.5, 3.8],
              [2.9, 3.0, 4.6, 4.0]])
S = A + B
print(f"La matriz S es: \n{S}")

# 3
print("------------------------------")
D = B - A
print(f"La matriz D es: \n{D}")

# 4
print("------------------------------")
print("S_24 = 6.6 Las ventas totales de ambos años del producto 2 en 4 región fueron de 6.6 millones de dolares")
print("D_24 = 1 El segundo año las ventas del producto 2 en la 4 región aumentaron en 1 millón de dolares con respecto al primer año")

# 5
print("------------------------------")
print("EL orden de la matriz E es 3 X 6, por lo tanto, no es posible determinar la matriz T ya que no tiene el mismo orden que las matrices A y B")