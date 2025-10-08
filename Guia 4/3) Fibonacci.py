# 1)
n = 0
F = []
for i in range(30):
    n = i + 1
    if i == 0:
        F.append(0)
        print(f"Los 20 primeros términos de la sucesión son: ")
    elif n <= 2:
        F.append(1)
    else:
        F.append(F[i - 1] + F[i - 2])

    if n < 21:
        print(f"F{n} = {F[i]}")

# 2)
print("-------------------------------------------------------------------------------")
suma = sum(F)
print(f"La suma de los primeros 30 términs de la sucesión de Fibonacci es : {suma}")