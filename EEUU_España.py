# 1)
def f(x):
    return 1.85 * x

# 2)
#Variable dependiente : Cantidad de cable instalado(km)
#Variable independiente : Tiempo (horas)

# 3)
# Para determina el dominio necesitamos el tiempo maximo para completar los 6600 km de cable instalado, enconces:
# f(x)= 6600
# 6600= 1.85x
#x= 6600 / 1.85
#Dom F(x)= [0, 3567.6]

# 4)
import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0, 3567.6, 1)
plt.plot(x, f(x), label = 'f(x)') #Acordar de poner el nombre de la función, asi que ojito
plt.title('Cantidad de cable instalado por hora')
plt.ylabel('Cantidad de cable instalada (km)')
plt.xlabel('Tiempo (horas)')
plt.grid(True)
plt.show()

# 5)
print(f"Trancusrridas 148 horas, se han instalado {f(148)} km de cable")
print(f"Trancusrridas 2300 horas, se han instalado {f(2300)} km de cable")

# 6)
t = 3480/1.85
print(t)
#1881.1
print(f"Al instalar 2480 km de cable trabajaron {t:.1f} horas")

# 7)
#Para completar el trabajo se requieren 3567,6 horas