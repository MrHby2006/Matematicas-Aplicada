# 1)
import numpy as np
#           Laptop Monitor Teclado Mouse Disco duro
F = np.array([[7,      6,     15,    17,      18],# Sucursal 1
              [5,      10,    20,    13,      12],# Sucursal 2
              [8,      4,     12,    18,      9]])# Sucursal 3
#             Proveedor 1 Proveedor 2 Proveedor 3
G = np.array([[1700,         1750,        1800],# Laptop
              [868,          803,         840],# Monitor
              [165,          160,         150],# Teclado
              [70,           73,          65],# Mouse
              [110,          124,         115]])# Disco duro
D = np.dot(F,G)
print(f"La matriz D es: \n\n{D}")

# 2)
print("---------------------")
print("El elemento D_33 es 21765. El costo de la renovación de equipos para la sucursal 3 con el porveedor 3 es de $21.765.000 pesos")
print("El elemendo D_21 es 22710. El costo de la renovación de equipos para la sucursal 2 con el proveedor 1 es de $22.710.000 pesos")

# 3)
print("---------------------")
P1 = D[0,0] + D[1,0] + D[2,0]
P2 = D[0,1] + D[1,1] + D[2,1]
P3 = D[0,2] + D[1,2] + D[2,2]
print(f"El costo con el proveedor 1 es: {P1}")
print(f"El costo con el proveedor 2 es: {P2}")
print(f"El costo con el proveedor 3 es: {P3}")
print("El proveedor mas conveniente para realizar la compras es el proveedor 1 con un total de $66.765.000 pesos")

# 4)
print("---------------------")
print("Si escoge al proveedor más conveniente deberá invertir más dinero por la renovación de los implementos en la sucursal 1")