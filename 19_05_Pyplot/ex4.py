import numpy as np
import matplotlib.pyplot as plt

xpoints = np.array([0, 1, 2, 3 ])
ypoints = np.array([3, 8, 1, 10])

x1points = np.array([0, 1, 2, 3])
x2points = np.array([6, 2, 7, 11])

plt.plot(xpoints, ypoints, '*:m', x1points, x2points, 'o-m')

plt.ylabel("Eixo Y")
plt.xlabel("Eixo X")

plt.show()