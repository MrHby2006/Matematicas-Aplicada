# 1)
# Sabemos que:
# b_2 = 1,2
# b_5 = 2,7
# entonces
# 1,2 = b_1 * r**(2 - 1)
# 2,7 = b_1 * r**(5 - 1)

# 1,2 = b_1 * r**1
# 2,7 = b_1 * r**4

# 2,7/1,2 = b_1/b_1 * r**4/r**1
# 2,25 = 1 * r**3
# raiz cubica de 2,25 = r
# 1,5 = r

# Ademas:
# b_2 = b_1 * r**1
# b_2/r**1 = b_1
b_2 = 1.2
r = 1.5
b_1 = b_2/r**1
print(f"El primer término de la sucesión es {b_1:.2f}")
print("El primer término de la sucesión es 0,80")
# Con eso dicho:
b_1 = 0.80
n = 9
r = 1.5

b_9 = b_1 * r**(n - 1)
print(f"El rendimiento del noveno mes es de {b_9:.2f}")

# 2)
print("-------------------------------------------")
final = 23.4
termino = 0
b_1 = 0.80
n = 9
r = 1.5
diferencia = final - termino

while diferencia > 0:
    n + 1
    termino = b_1 * r**(n - 1)
    diferencia = final - termino
    
if diferencia == 0:
    print(f"El término {final} pertenece a la sucesión y esta en la posición {n}")
else:
    print(f"El término {final} no pertenece a la sucesión")