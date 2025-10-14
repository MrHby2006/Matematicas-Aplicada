# 1)
a_1 = 12000
d = 2000

print(f"Los depositos del primer año son: ")

ahorro = []
for i in range(12):
    n = i + 1
    ahorro.append(a_1 + (n - 1)*d)
    print(f"Mes {n} = ${ahorro[i]}")
    
# 2)
print("----------------------------------------------------------------------")
n = 14
print(f"En Febrero del segundo año el estudiante depositó ${a_1 + (n-1)*d}")

# 3)
print("----------------------------------------------------------------------")
print(f"Los ahorros de los dos primeros años son: ")

ahorro_total = []
ahorro = []
for i in range(24):
    n = i + 1
    ahorro_total.append(a_1 + (n - 1)*d)
    print(f"Mes {n} = ${ahorro_total[i]}")
    
total = sum(ahorro_total)
print(f"El dinero total ahorrado en dos años es ${total}")