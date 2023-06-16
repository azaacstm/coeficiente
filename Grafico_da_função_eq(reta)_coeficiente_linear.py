import numpy as np
import matplotlib.pyplot as plt
# Dados para o gráfico
x = np.array([])
y = np.array([])
# Ajuste da linha de tendência (regressão linear)
coefficients = np.polyfit(x, y, 1)
m = coefficients[0]  # Coeficiente angular (inclinação)
b = coefficients[1]  # Coeficiente linear (intercepto)
# Cálculo do coeficiente de determinação (R²)
y_pred = m * x + b
ss_total = np.sum((y - np.mean(y))**2)
ss_residual = np.sum((y - y_pred)**2)
r_squared = 1 - (ss_residual / ss_total)
# Plotar pontos de dados
plt.scatter(x, y, label='Dados')
# Plotar a linha de tendência
plt.plot(x, m * x + b, color='red', label='Linha de Tendência')
# Adicionar legenda com os valores
legenda = "{:.3f}x + {:.3f}  R² = {:.4f}".format(m, b, r_squared)
plt.text(2750, 0.25, legenda)  # Ajuste as coordenadas (24, 200)   conforme necessário
# Configurações do gráfico
plt.xlabel()
plt.ylabel()
plt.title()
plt.legend()
# Exibir o gráfico
plt.show()
