import numpy as np
import matplotlib.pyplot as plt

xpoints = np.array([0, 1, 2, 3, 5])
ypoints = np.array([3, 8, 1, 10, 7])

plt.plot(xpoints, ypoints,'p:r', ms = 30, mfc = 'g', mec = 'b')
plt.show()