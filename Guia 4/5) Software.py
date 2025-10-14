# 1)
b_0 = 500
r = 1.15
b_1 = b_0 * r
b_3 = b_1 * r**(3-1)
b_6 = b_1 * r**(6-1)
print(f"AL cabo de tres meses la cantidad de usuarios sera {(b_3):.0f}")
print(f"AL cabo de seis meses la cantidad de usuarios sera {(b_6):.0f}")

# 2)
print("-------------------------------------------------------------------------")
print("La cantidad de usuarios que tendrá el software durante cada mes del año")
b_0 = 500
r = 1.15
b_1 = b_0 * r
usuario = []
n = 0
for i in range(12):
    n = i + 1
    usuario.append(b_1 * r**(n-1))
    print(f"Mes {n} = {usuario[i]:.0f} usuarios")
    
# 3)
print("-------------------------------------------------------------------------")
total_usuarios_año = b_0 * r**12
print(f"Luego de un año el software tendrá {(total_usuarios_año):.0f} usuarios")