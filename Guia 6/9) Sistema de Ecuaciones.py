# 1)
import numpy as np

A = np.array(([2, 1],
              [3, -2]))

B = np.array(([7],
              [21]))

A_inv = np.linalg.inv(A)

C = np.dot(A_inv, B)

print(f"La matriz de las incognitas es: \n\n{C}")
print("Los valores de X e Y que dan a la solución al sistema de ecuación 1 son X = 5 e Y = -3")

# 2)
print("----------------------")
D = np.array(([1, 1],
              [0.16, 0.2]))

E = np.array(([60],
              [11]))

D_inv = np.linalg.inv(D)

F = np.dot(D_inv, E)

print(f"La matriz de las incognitas es: \n\n{F}")
print("Los valores de H y M que dan a la solución al sistema de ecuación 2 son H = 25 e M = 35")
