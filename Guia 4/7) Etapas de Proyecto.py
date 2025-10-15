# 1)
a_1 = 3
r = 0.9
n = 0
duracion = []

for i in range(5):
    n = i + 1
    duracion.append(a_1 * r**(n-1))

print(f"La quinta fase tien una duración de {duracion[i]:.0f} meses")

# 2)
print("-------------------------------------------")
total = []
for i in range(10):
    n = i + 1
    total.append(a_1 * r**(n-1))
suma = sum(total)

print(f"La duración total proyecto despues de 10 fases fue de {suma:.1f} meses")