# 1)

import numpy as np
import matplotlib.pyplot as plt

tiempo = np.arange(0, 15, 0.1)
metro = 0.4*tiempo       #Como se grafican
bus = 0.3*tiempo         #dos o más variables
plt.plot(tiempo, metro, label = 'Metro')
plt.plot(tiempo, bus, label = 'Bus')
plt.title('Distancia recorrida por minutos')
plt.ylabel('Distancia(Km)')
plt.xlabel('Tiempo (M)')
plt.legend()
plt.grid(True)
plt.show()

# 2)
#Dominio = 1.2 X 9}
#          0.5 X 8} 14.8

# 3)
# Es el metro

# 4)
t=6/0.4
g=6/0.3
print(t)
print(g)