import matplotlib.pyplot as plt
import numpy as np

y = np.array([18440, 13778, 4553, 823])
rotulos = ['Carro', 'Caminhão', 'Motocicletas', 'Outros']
des = [0.05, 0.01, 0.02, 0.03]


plt.pie(y, labels = rotulos, startangle=98, explode=des)

plt.show()

