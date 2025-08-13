def IMC(p, a):
    return p/a**2

print("Calculo de IMC")

p = float(input("Ingrese su peso en kilogramos: "))
a = float(input("Ingrese su altura en metros: "))


if IMC(p,a) < 18.5:
    print(f"El IMC de una persona de peso {p:.1f} kg y altura {a:.1f} m es {IMC(p,a):.1f}, por lo tanto su categoria es Bajo Peso")
elif IMC(p,a) > 18.5 and IMC(p,a) < 24.9:
    print(f"El IMC de una persona de peso {p:.1f} kg y altura {a:.1f} m es {IMC(p,a):.1f}, por lo tanto su categoria es Peso Normal")
elif IMC(p,a) > 25 and IMC(p,a) < 29.9:
    print(f"El IMC de una persona de peso {p:.1f} kg y altura {a:.1f} m es {IMC(p,a):.1f}, por lo tanto su categoria es SobrePeso")
else:
    print(f"El IMC de una persona de peso {p:.1f} kg y altura {a:.1f} m es {IMC(p,a):.1f}, por lo tanto su categoria es Obesidad")