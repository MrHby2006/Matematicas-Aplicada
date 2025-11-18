# 1)
print("X representa la cantidad de monedas de $10 y la Y representa la cantidad de modes de $50")

# 2)
print("---------------------------")
print("X + Y = 200 represenat la suma de la cantidad de monedas de cadatipo, totalizando 200 monedas")
print("10X + 50X = 8000 corresponde a la cantidad de monedas con el valor de cada moneda que totalizan $8000")

# 3)
print("---------------------------")
import numpy as np

A = np.array([[1,  1],
              [10, 50]])

B = np.array([[200],
              [8000]])

A_inv = np.linalg.inv(A)

C = np.dot(A_inv, B)

print(f"La matriz de las incognitas es: \n\n{C}")