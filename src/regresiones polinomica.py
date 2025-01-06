import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Datos de ejemplo
X = np.array([25, 50, 75, 90, 100, 150]).reshape(-1, 1)  # Variables independientes
y = np.array([43, 84, 125, 152, 170, 252])  # Variable dependiente

# 1. Transformación para la Regresión Exponencial
# y = a * e^(b * x) => ln(y) = ln(a) + b * x
y_log = np.log(y)  # Tomamos el logaritmo de y
modelo_exp = LinearRegression()
modelo_exp.fit(X, y_log)
y_pred_log = modelo_exp.predict(X)
y_pred_exp = np.exp(y_pred_log)  # Convertimos de nuevo a escala original

# 2. Transformación para la Regresión Logarítmica
# y = a + b * ln(x)
X_log = np.log(X)  # Tomamos el logaritmo de X
modelo_log = LinearRegression()
modelo_log.fit(X_log, y)
y_pred_log_model = modelo_log.predict(X_log)

# 3. Evaluación de los modelos
mse_exp = mean_squared_error(y, y_pred_exp)
r2_exp = r2_score(y, y_pred_exp)

mse_log = mean_squared_error(y, y_pred_log_model)
r2_log = r2_score(y, y_pred_log_model)

print(f"Regresión Exponencial: MSE = {mse_exp}, R^2 = {r2_exp}")
print(f"Regresión Logarítmica: MSE = {mse_log}, R^2 = {r2_log}")

# 4. Gráfica de los resultados
plt.scatter(X, y, color='black', label='Datos originales')

plt.plot(X, y_pred_exp, color='blue', label='Regresión Exponencial')
plt.plot(X, y_pred_log_model, color='red', label='Regresión Logarítmica')

plt.xlabel('Cantidad de estacionamiento')
plt.ylabel('Cantidad óptima de vehículos')
plt.legend()
plt.title('Comparación de Modelos Exponencial y Logarítmico')
plt.show()

# 5. Ecuaciones de los modelos
# Regresión Exponencial
a_exp = np.exp(modelo_exp.intercept_)
b_exp = modelo_exp.coef_[0]
print(f"Ecuación de la regresión exponencial: y = {a_exp:.2f} * e^({b_exp:.2f}x)")

# Regresión Logarítmica
a_log = modelo_log.intercept_
b_log = modelo_log.coef_[0]
print(f"Ecuación de la regresión logarítmica: y = {a_log:.2f} + {b_log:.2f} * ln(x)")
