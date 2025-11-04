# 1)
import numpy as np
D = np.array([[20, 28, 22, 26, 24],
              [52, 57, 56, 54, 58],
              [1066, 1068, 1066, 1064, 1068]])
S = D * 0.95
print(f"Los valores correctos de temperatura, humedad y presión son: \n\n{S}")

# 2)
print("--------------------------------------------")
S_T = S.T
print(f"La matriz transpuesta de S es: \n\n{S_T}")

# 3)
print("--------------------------------------------")
print("El elemento S_24 es 51,3. El día Jueves se registró una humedad del 51,3%")
print("El elemento ST_31 es 20,9. El día Miércoles se registró una temperatura de 20,9°C")