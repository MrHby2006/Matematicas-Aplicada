print("Verificador de números")
numero = float(input("Ingrese un número: "))

if numero > 0:
    print(f"El número", numero, "es positivo")
elif numero < 0:
    print(f"El número", numero, "es negativo")
elif numero == 0:
    print(f"El número es 0")
else:
    print("Opción no valida")