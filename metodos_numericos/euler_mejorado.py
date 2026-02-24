import numpy as np
import matplotlib.pyplot as plt

def euler_mejorado(f, x0, y0, h, x_final):
    """
    Resuelve dy/dx = f(x, y) con y(x0) = y0 usando Euler Mejorado.
    """
    x = np.arange(x0, x_final + h, h)
    y = np.zeros(len(x))
    y[0] = y0
    
    for i in range(0, len(x) - 1):
        k1 = f(x[i], y[i])
        y_pred = y[i] + h * k1
        k2 = f(x[i+1], y_pred)
        y[i+1] = y[i] + (h / 2) * (k1 + k2)
        
    return x, y

def mostrar_tabla(x, y):
    """Muestra tabla de resultados"""
    print("\n" + "="*40)
    print(f"{'x':<15} {'y':<15}")
    print("="*40)
    for xi, yi in zip(x, y):
        print(f"{xi:<15.4f} {yi:<15.4f}")
    print("="*40 + "\n")

def mostrar_grafica(x, y):
    """Muestra gráfica de la solución"""
    plt.figure(figsize=(10, 6))
    plt.plot(x, y, 'b-o', linewidth=2, markersize=5)
    plt.grid(True)
    plt.xlabel('x', fontsize=12)
    plt.ylabel('y', fontsize=12)
    plt.title('Solución usando Método de Euler Mejorado', fontsize=14)
    plt.show()