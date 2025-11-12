# 1)
import numpy as np

A = np.array(([3, 1, 2],
              [1, 2, 1],
              [4, 1, 3]))

A_inv = np.linalg.inv(A)

print(f"La matriz inversa de A es: \n\n{A_inv}")

# 2)
print("------------------------")
I = np.round(np.dot(A, A_inv))

print(f"La matriz I es: \n\n{I}")

# 3)
print("------------------------")
I_inv = np.linalg.inv(I)

print(f"La matriz inversa de I es: \n\n{I_inv}")

print("La matriz I y su inversa son iguales ya que esta matriz identidad actua como el 1 en la multiplicación de numeros y por ende el inverso de esta matriz neutra es la misma matriz")