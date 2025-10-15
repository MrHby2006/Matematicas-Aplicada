# 1)
# d = 4
# a_10 = -20
# entonces
# a_10 = a_1 + (19 - 1) X d
# -20 = a_1 + 9 *4
# -20 - 36 = a_1
# -56 = a_1
print("A1 = -56")

# 2)
print("-------------------------------------------")
print("An = -56 + (n - 1) X 4")

# 3)
print("-------------------------------------------")
a_1 = -56
d = 4
a_100 = a_1 + (100 - 1) * 4
print(f"El término que ocupa el pueso 100 es: {a_100}")

# 4)
print("-------------------------------------------")
final = 1680
termino = 0
n = 0
diferencia = final - termino

while diferencia > 0:
    n + 1
    termino = -56 + (n - 1) * 4
    diferencia = final - termino
    
if diferencia == 0:
    print(f"El término {final} pertenece a la sucesión y esta en la posición {n}")
else:
    print(f"El término {final} no pertenece a la sucesión")