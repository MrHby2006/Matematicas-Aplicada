# 1)
# Sabemos que:
# a_3 = 500
# a_10 = 1501

# a_n = a_1 + (n - 1) * d
# 1501 = a_1 + (10 - 1) * d
# 500 = a_1 + (3 - 1) * d
# (1501 - 500) = (a_1 - a_1) + (9 - 2) * d
# 1001 = 7d
# 1001 / 7 = d

# Entonces:
d = 1001/7
print(f"d = {d:.0f}")

a_3 = 500
a_1 = a_3 - 2*d
print(f"La aplicación inicio con {a_1:.0f} usuarios")

# 2)
print("-----------------------------------------------")
a_1 = 214
d = 143
n = 31
a_31 = a_1 + (n - 1) * d

print(f"La aplicación tendrá {a_31:.0f} usuarios el 31 de Enero")

# 3)
print("-----------------------------------------------")
final = 5505
termino = 0
dif = final - termino
n = 0
a_1 = 214
d = 143

while dif > 0:
    n += 1
    termino = a_1 + (n - 1) * d
    dif = final - termino

print(f"Si la aplicación tiene 5505 usuarios es porque lleva funcionando {n} dias")