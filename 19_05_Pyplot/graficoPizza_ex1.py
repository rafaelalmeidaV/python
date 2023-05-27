import matplotlib.pyplot as plt
import numpy as np

y = np.array([18440, 13778, 4553, 8230])
rotulos = ['Carro', 'Caminhão', 'Motocicletas', 'Outros']
des = [0.05, 0.01, 0.02, 0.03]
color = ['purple', 'magenta', 'red', 'pink']




plt.pie(y, labels = rotulos, startangle=98, explode=des , shadow=True, colors= color, autopct="%1.1f%%")

plt.title("Porcentagem de mortes em acidentes de transito")

plt.legend(rotulos, title="Titulo da legenda", loc='center', bbox_to_anchor=(1.1, 0.5))
plt.show()

