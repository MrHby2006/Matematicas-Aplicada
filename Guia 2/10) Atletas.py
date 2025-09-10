# 1)
import numpy as np
import matplotlib.pyplot as plt
def g(t):
    return 0.7*t ** 2
def f(t):
    return 10*t

t = np.arange(0, 15, 0.1)
plt.plot(t, g(t), color = "purple", label = 'Atleta 1')
plt.plot(t, f(t), color = "orange", label = 'Atleta 2')
plt.title('Relación entre la distancia recorrida y el tiempo')
plt.ylabel('Distancia recorrido (en Metros)')
plt.xlabel('Tiempo (en Segundos)')
plt.grid(True)
plt.legend()
plt.show()

print("El atleta 2 es el que mantuvó una veloicidad constante ya que en el gráfico se observa que para mismo interval de tiempo la distancia recorrida aumenta en el mismo valor")

# 2)
print("Si la meta se encontraba a 100 metros, el atleta 2 llegó primero ya que en ele gráfico se observa que tard 10 segundos mientras que el atleta 1 tarda 20 segundos")

# 3)
def g(t):
    return 0.7*t ** 2
def f(t):
    return 10*t

print(f"Distancia del atleta 1 a los 8 segundos = {g(8)}")
print(f"Distancia del atleta 2 a los 8 segundos = {f(8)}")
print(f"Distancia del atleta 1 a los 10 segundos = {g(10)}")
print(f"Distancia del atleta 2 a los 10 segundos = {f(10)}")

print("Transcurridos 8 segundos los atletas se encuentran a 35.2 metros de distancia")
print("Transcurridos 10 segundos los atletas se encuentran a 30 metros de distancia")

# 4)
print(f"{g(10)-g(8):.1f}")
print(f"{f(10)-f(8)}")

print("Entre los 8 y 10 segundos el atleta 2 recorrió 20 metros, mientras que el atleta 1 recorrió 25.2 metros, por lo tanto, el atleta 1 iba más rapido")