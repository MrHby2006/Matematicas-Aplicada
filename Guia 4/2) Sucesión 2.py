# 1)
g = []
for i in range(4):
    n = i + 1
    g.append(5*n**3)
    print(f"g_{n} = {g[i]}")

# 2)
print("------------------------------------------------")
g = []
for i in range(4):
    n = i + 9
    g.append(5*n**3)
    print(f"g_{n} = {g[i]}")

# 3)
print("------------------------------------------------")
final = 40000
termino = 0
n = 0
diferencia = final - termino

while diferencia > 0:
    n + 1
    termino = 5*n**3
    diferencia = final - termino

if diferencia == 0:
    print(f"El término {final} le pertenece a la sucesión, se encuentra en la pocisión {n}")
else:
    print(f"El término {final} no pertenece a la sucesión")