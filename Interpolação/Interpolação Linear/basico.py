import numpy as np
import matplotlib.pyplot as plt

# Definindo os pontos conhecidos
x_known = [1, 3]
y_known = [2, 6]

# Definindo o ponto onde queremos estimar o valor
x_to_estimate = 2

# Fazendo a interpolação linear
y_estimated = np.interp(x_to_estimate, x_known, y_known)

print(f'O valor estimado para x = {x_to_estimate} é y = {y_estimated}')

# Plotando para visualizar a interpolação
plt.plot(x_known, y_known, 'o', label='Pontos conhecidos')
plt.plot(x_to_estimate, y_estimated, 'x', label='Valor estimado')
plt.plot([x_known[0], x_to_estimate, x_known[1]], [y_known[0], y_estimated, y_known[1]], '--', label='Interpolação linear')
plt.legend()
plt.show()
