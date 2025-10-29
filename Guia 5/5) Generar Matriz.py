import numpy as np
M = np.fromfunction(lambda i, j: 8*(i +1) + 12*(j + 1), (8, 9))
M_t = M.T

print(f"La matriz M es: \n{M}\n")
print(f"La matriz transpuesta de M es: \n{M_t}")