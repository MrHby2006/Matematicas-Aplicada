# 1)
# Sabemos que:
# a_2 = 402000
# a_3 = 404010
# Entonces
# 402000 = a_1 * r**(2 - 1)
# 404010 = a_1 * r**(3 - 1)

# 402000 = a_1 * r**1
# 404010 = a_1 * r**2

# 404010/402000 = a_1/a_1 * r**2/r**1
a_2 = 402000
a_3 = 404010
r = a_3 / a_2
print(f"La razón es {r}")
r = 1.005
a_1 = a_2 / r

print(f"El primer término de la sucesión es: {a_1:.0f}")
a_1 = 400000
r = 1.005
n = 10
a_10 = a_1 * r**(n - 1)

print(f"Al decimo mes el sueldo de Javier será de ${a_10:.0f}")

# 2)
print("---------------------------------------------------------")
sueldo = []
a_1 = 400000
r = 1.005
for i in range(25, 37):
    n = i + 1
    sueldo.append(a_1 * r**(n - 1))

total = sum(sueldo)

print(f"El sueldo total que a recibido javier durante su tercer año sera de {total:.0f}")