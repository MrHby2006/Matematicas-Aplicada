# 1)
a_1 = 200
d = 24
n = 36
a_36 = a_1 + (n - 1) * d
print(f"{a_36}")

# 2)
print("---------------------------------------")
sucesion = []
for i in range(36):
    n = i + 1
    sucesion.append(a_1 + (n - 1) * d)
    
    suma = sum(sucesion)
    
print(f"{suma}")

# 4)
print("---------------------------------------")
a_1 = 2000000
r = 1.012
n = 9
a_9 = a_1 * r**n
print(f"{a_9:.0f}")

# 5)
print("---------------------------------------")
a_2 = 1066
a_5 = 8528
r = (a_5/a_2)**(1/3)
print(f"{r}")

a_1 = a_2/r
print(f"{a_1}")

a_9 = a_1 * r**(9 - 1)
print(f"{a_9}")

# 6)
print("---------------------------------------")
final = 34112
termino = 0
dif = final - termino
a_1 = 533
r = 2
n = 0
while dif > 0:
    n += 1
    termino = a_1 * r**(n - 1)
    dif = final - termino
    
print(f"El termino se encuentra en la posicion {n}")

# 7)
print("---------------------------------------")
a_4 = 1108000
a_12 = 1396000
d = (a_12 - a_4)/8
print(f"{d}")
a_1 = a_4 - 3 * d
print(f"{a_1}")

final = 1828000
termino = 0
dif = final - termino
a_1 = 1000000
d = 36000
n = 0
while dif > 0:
    n += 1
    termino = a_1 +(n - 1) * d
    dif = final - termino

print(f"El termino se encuentra en la posicion {n}")

# 8)
print("---------------------------------------")
import numpy as np
T = np.array([[300, 272, 240],
              [260, 180, 324]])

U = np.array([[1200, 1250],
              [1100, 1400],
              [1350, 1200]])

V = np.dot(T, U)
print(f"{V}")

# 12)
print("---------------------------------------")
S = np.array([[360, 260, 150, 420],
              [450, 370, 210, 130],
              [240, 260, 320, 340]])

C = np.array([[130, 310, 230, 280],
              [270, 240, 520, 370],
              [190, 290, 460, 410]])

S1 = S * 0.8
C1 = C * 1.1

T = S1 + C1

print(f"{T}")

# 13)
print("---------------------------------------")
A = np.fromfunction(lambda i, j: 2*(i + 1) + 3*(j + 1), (3, 3))
B = np.fromfunction(lambda i, j: 10*(i + 1) * (j + 1), (3, 3))
print(f"{A}\n\n{B}\n")
C = np.dot(A, B)
print(f"{C}")

# 14)
print("---------------------------------------")
A = np.array([[2, 1],
              [3, -2]])

B = np.array([[10],
              [8]])

A_inv = np.linalg.inv(A)

C = np.dot(A_inv, B)
print(f"{C}")

# 16)
print("---------------------------------------")
A = np.array([[2, 3],
              [1, 2]])

A_inv = np.linalg.inv(A)

print(f"{A_inv}")

# 17)
print("---------------------------------------")
A1 = A.T
print(f"{A1}")

# 19)
print("---------------------------------------")
B = A + A1
print(f"{B}")

# 20)
print("---------------------------------------")
A = np.array([[2, 3],
              [1, 4]])

B = np.array([[52],
              [56]])

A_inv = np.linalg.inv(A)

C = np.dot(A_inv, B)
print(f"{C}")