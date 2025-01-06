import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.metrics import mean_squared_error, r2_score

# 1. Datos: Cuatro puntos de ejemplo
X = np.array([25,50,75,90, 100,150]).reshape(-1, 1)  # Variables independientes (reshape para ser columna)
y = np.array([43, 84,125,152, 170,252])  # Variable dependiente

# 2. Regresión Lineal
modelo_lineal = LinearRegression()
modelo_lineal.fit(X, y)
y_pred_lineal = modelo_lineal.predict(X)

# 3. Regresión Polinomial de grado 2
poly_features_2 = PolynomialFeatures(degree=2)
X_poly_2 = poly_features_2.fit_transform(X)
modelo_poly_2 = LinearRegression()
modelo_poly_2.fit(X_poly_2, y)
y_pred_poly_2 = modelo_poly_2.predict(X_poly_2)

# 4. Regresión Polinomial de grado 3
poly_features_3 = PolynomialFeatures(degree=3)
X_poly_3 = poly_features_3.fit_transform(X)
modelo_poly_3 = LinearRegression()
modelo_poly_3.fit(X_poly_3, y)
y_pred_poly_3 = modelo_poly_3.predict(X_poly_3)

# 5. Evaluación de los modelos
mse_lineal = mean_squared_error(y, y_pred_lineal)
r2_lineal = r2_score(y, y_pred_lineal)

mse_poly_2 = mean_squared_error(y, y_pred_poly_2)
r2_poly_2 = r2_score(y, y_pred_poly_2)

mse_poly_3 = mean_squared_error(y, y_pred_poly_3)
r2_poly_3 = r2_score(y, y_pred_poly_3)

print(f"Regresión Lineal: MSE = {mse_lineal}, R^2 = {r2_lineal}")
print(f"Regresión Polinomial (grado 2): MSE = {mse_poly_2}, R^2 = {r2_poly_2}")
print(f"Regresión Polinomial (grado 3): MSE = {mse_poly_3}, R^2 = {r2_poly_3}")

# 6. Gráfica de los resultados
plt.scatter(X, y, color='black', label='Datos originales')

plt.plot(X, y_pred_lineal, color='blue', label='Regresión Lineal')
plt.plot(X, y_pred_poly_2, color='red', label='Regresión Polinomial (Grado 2)')
plt.plot(X, y_pred_poly_3, color='green', label='Regresión Polinomial (Grado 3)')

plt.xlabel('Cantidad de estacionamiento')
plt.ylabel('Cantidad optima de Vehiculos')
plt.legend()
plt.title('Comparación de Modelos de Regresión')
plt.show()


# Coeficiente (pendiente) y la intersección para la regresión lineal
pendiente = modelo_lineal.coef_[0]
interseccion = modelo_lineal.intercept_

print(f"Ecuación de la regresión lineal: y = {pendiente}x + {interseccion}")
# Con dos decimales
print(f"Ecuación de la regresión lineal: y = {pendiente:.2f}x + {interseccion:.2f}")

# Coeficientes y la intersección para la regresión polinomial de grado 2
coeficientes_poly_2 = modelo_poly_2.coef_
interseccion_poly_2 = modelo_poly_2.intercept_

# El primer coeficiente corresponde al término de mayor grado (en este caso x^2)
print(f"Ecuación de la regresión polinomial de grado 2: y = {coeficientes_poly_2[2]}x^2 + {coeficientes_poly_2[1]}x + {interseccion_poly_2}")
# Con dos decimales
print(f"Ecuación de la regresión polinomial de grado 2: y = {coeficientes_poly_2[2]:.2f}x^2 + {coeficientes_poly_2[1]:.2f}x + {interseccion_poly_2:.2f}")

# Coeficientes y la intersección para la regresión polinomial de grado 3
coeficientes_poly_3 = modelo_poly_3.coef_
interseccion_poly_3 = modelo_poly_3.intercept_

# El primer coeficiente corresponde al término de mayor grado (en este caso x^3)
print(f"Ecuación de la regresión polinomial de grado 3: y = {coeficientes_poly_3[3]}x^3 + {coeficientes_poly_3[2]}x^2 + {coeficientes_poly_3[1]}x + {interseccion_poly_3}")
# Con dos decimales
print(f"Ecuación de la regresión polinomial de grado 3: y = {coeficientes_poly_3[3]:.2f}x^3 + {coeficientes_poly_3[2]:.2f}x^2 + {coeficientes_poly_3[1]:.2f}x + {interseccion_poly_3:.2f}")