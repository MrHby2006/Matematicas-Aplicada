# 1)
import numpy as np
S = np.array([[260, 480, 180, 90],
              [320, 440, 250, 280],
              [240, 360, 380, 250]])
H = np.array([[360, 250, 300, 250],
              [450, 500, 350, 380],
              [290, 300, 460, 400]])

T = S + H
print(f"El total de ventas de la empresa es: \n\n{T}")

# 2)
print("-------------------------------")
print("Es falso, la zona sur se encuentra en la segunda columna. Podemos ver que solo en el producto 2 recaudo mas por la venta de Hardware que de Software, \nespecificamente 60 millones de pesos más. Por lo tanto, el trabajador estaba equivocado")

# 3)
print("-------------------------------")
M = 1.07*S + 1.03*H
print(f"Las ventas totales estimadas para el mes siguiente son: \n\n{M}")

# 4)
print("-------------------------------")
print("El elemento T_24 es 660. Este mes se recaudó un total de 660 millones de pesos por la venta de Software y Hardware del producto 2 en la zona Oeste")
print("El elemento M_31 es 555,5. Se estima que para el mes siguiente se recaudará un total de 555,5 millones de pesos por la venta de Software y Hardware \ndel producto 3 en la zona Norte")

# 5)
print("-------------------------------")
M_T = M.T
print(f"La matriz transpuesta de M es: \n\n{M_T}")
print("El elemento MT_41 es 353,8. Se estima que para el mes siguiente se recaudará un total de 353,8 millones de pesos por la venta de Software y Hardware \ndel producto 1 en la zona Oeste")