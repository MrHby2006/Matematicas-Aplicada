# 1)
import numpy as np

# a)
# (2 4) (m) = (2900)
# (3 3) (p) = (3150)

# b)
# (1 1)    (n) = (160)
# (50 300) (v) = (23000)

A = np.array(([2, 4],
              [4, 3]))

B = np.array(([2900],
              [3150]))

A_inv = np.linalg.inv(A)

C = np.dot(A_inv, B)

D = np.array(([1, 1],
              [50, 300]))

E = np.array(([160],
              [23000]))

D_inv = np.linalg.inv(D)

F = np.dot(D_inv, E)

print(f"La matriz del sistema A es: \n\n{C}\n")
print(f"La matriz del sistema B es: \n\n{F}")

# 2)
print("----------------------------")
