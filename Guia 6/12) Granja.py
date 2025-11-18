# 1)
print("P representa la cantidad de patos que hay en la granja y V representa la cantidad de vacas que hay en la granja")

# 2)
print("----------------------")
import numpy as np

A = np.array([[1, 1],
              [2, 4]])

B = np.array([[132],
              [402]])

A_inv = np.linalg.inv(A)

C = np.dot(A_inv, B)

print(f"La matriz de las incognitas es: \n\n{C}")
print("La cantidad de patos que hay es 63")