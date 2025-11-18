# 1)
print("X representa el precio unitario de un cable USB y Y representa el precio unitario de un Pendrive")

# 2)
print("--------------------")
import numpy as np

A = np.array([[5, 6],
              [3, 7]])

B = np.array([[82890],
              [59900]])

A_inv = np.linalg.inv(A)

C = np.dot(A_inv, B)

print(f"La matriz de las incognitas es: \n\n{C}")

print("Luis y Pablo pagaron $12990 por cada cable USB")