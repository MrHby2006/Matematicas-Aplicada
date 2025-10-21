# 1)
# Sabemos que:
# a_1 = 30
# a_2 = 60
# a_3 = 120
# Entonces
# 30 = a_1 * r**(1 - 1)
# 60 = a_1 * r**(2 - 1)
# 120 = a_1 * r**(3 - 1)

# 30 = a_1 * r**0
# 60 = a_1 * r**1
# 120 = a_1 * r**2

# 60/30 = a_1/a_1 * r**1/r**0
# 120/60 = a_1/a-1 * r**2/r**1
a_1 = 30
a_2 = 60
a_3= 120
r_1 = a_2 / a_1
r_2 = a_3 / a_2
print(f"La primera razón es {r_1:.0f}") # Confirmación de que
print(f"La primera razón es {r_2:.0f}") # tienen el mismo resultado
r = 2
n = 8

a_8 = a_1 * r**(n - 1)

print(f"Al octavo trimestre la empresa habra capacitado {a_8:.0f} trabajadores")

# 2)
print("-------------------------------------------------------------------------")
# 3 años = 12 trimestres
trabajadores = []
a_1 = 30
n = 12
r = 2
for i in range(1, 13):
    n = i + 1
    trabajadores.append(a_1 * r**(n - 1))

total = sum(trabajadores)

print(f"La cantidad total de trabajadores capacitados despues de 3 años será de {total:.0f}")