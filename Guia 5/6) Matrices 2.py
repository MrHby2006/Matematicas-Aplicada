import numpy as np
A = np.fromfunction(lambda i, j: (i + 1) * (j + 1), (5, 7))
B = np.fromfunction(lambda i, j: 15*(i + 1) - 2*(j + 1), (7, 5))
print(f"A = {A}\n\nB = {B}\n")

A_T = A.T
C = A_T + 0.5*B
print(f"La matriz C es: {C}")