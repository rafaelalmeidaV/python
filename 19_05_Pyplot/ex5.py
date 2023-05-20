import numpy as np
import matplotlib.pyplot as plt

xpoints = np.array([0, 1, 2, 3 ])
ypoints = np.array([3, 8, 1, 10])

x1points = np.array([0, 1, 2, 3])
x2points = np.array([6, 2, 7, 11])

plt.plot(xpoints, ypoints, label = 'Linha 1')
plt.plot( x1points, x2points, label= 'Linha 2')

plt.ylabel("Eixo Y")
plt.xlabel("Eixo X")

plt.axis((-1,4,1,12)) #define o minimo e o maximo dos eixos xInicial = -1 e xFinal = 4

plt.grid(True) #abilita as grids "traços" do grafico

plt.legend() #coloca a legenda no grafico com label la no plot

plt.title("Grafico de linhas", color = 'm', fontsize = 32 , style = 'italic')

plt.show()