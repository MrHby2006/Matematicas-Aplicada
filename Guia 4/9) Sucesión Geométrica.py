# 1)
# Sabemos que:
# b_3 = 5
# b_6 = 40
# entonces
# 5 = b_1 * r**(3 - 1)
# 40 = b_1 * r**(6 - 1)

# 5 = b_1 * r**2
# 40 = b_1 * r**5

# 40/5 = b_1/b_1 * r**5/r**2
# 8 = 1 * r**3
# raiz cubica de 8 = r
# 2 = r

b_3 = 5
b_6 = 40
r = (b_6/b_3)**(1/3)
print(f"La razón constante de la sucesión geométrica es {r:.0f}")

# 2)
print("-------------------------------------------")
# b_3 = b_1 * r**2
# b_3/r**2 = b_1
b_3 = 5
r = 2
b_1 = b_3/r**2
print(f"El primer término de la sucesión es {b_1}")

# 3)
print("-------------------------------------------")
print("Formula general: b_n = 1.25 * 2**(n - 1)")

# 4)
print("-------------------------------------------")
n = 8
b_1 = 1.25
r = 2
b_8 = b_1 * r**(n-1)
print(f"El término de la posición 8 en la sucesión es {b_8:.0f}")

# 5)
print("-------------------------------------------")
final = 20480
termino = 0
b_1 = 1.25
r = 2
n = 0
diferencia = final - termino

while diferencia > 0:
    n + 1
    termino = b_1 * r**(n - 1)
    diferencia = final - termino
    
if diferencia == 0:
    print(f"El término {final} pertenece a la sucesión y esta en la posición {n}")
else:
    print(f"El término {final} no pertenece a la sucesión")