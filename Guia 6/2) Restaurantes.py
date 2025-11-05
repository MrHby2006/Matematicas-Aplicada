# 1)
print("Orden V = 3 X 3")
print("Orden P = 3 X 1")

# 2)
print("------------------------------")
import numpy as np
            #  Sant Conce Anto
V = np.array([[1300, 900, 800], # Hamburguesa
              [2100, 1700, 1500], # Completo
              [1500, 1200, 900]]) # Malteada
            #  H      C     M
P = np.array([[4200, 1500, 3200]]) # Precio
I = np.dot(P, V)
print(f"La matriz I es: \n{I}")

# 3)
print("------------------------------")
print("El elemento V_32 es 1200. Representa que en Concepción se vendieron 1200 malteadas en un fin de semana")
print("El elemento P_12 es 1500. Representa que el precio de un completo es de 1500 pesos")
print("El elemento I_13 es 8490000. Representa que en la sucursal de Antofagasta se vendieron 8490000 por la venta de los tres productos")