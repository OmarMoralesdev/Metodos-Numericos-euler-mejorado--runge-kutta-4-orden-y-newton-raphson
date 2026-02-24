import numpy as np
import matplotlib.pyplot as plt

def runge_kutta4(f, t0, y0, t_end, h):
    """Método RK4"""
    n = int((t_end - t0) / h)
    t = np.linspace(t0, t_end, n+1)
    y = np.zeros(n+1)
    y[0] = y0
    
    for i in range(n):
        k1 = h * f(t[i], y[i])
        k2 = h * f(t[i] + h/2, y[i] + k1/2)
        k3 = h * f(t[i] + h/2, y[i] + k2/2)
        k4 = h * f(t[i] + h, y[i] + k3)
        y[i+1] = y[i] + (k1 + 2*k2 + 2*k3 + k4) / 6
        
    return t, y

def mostrar_tabla(t, y):
    """Muestra tabla de resultados"""
    print("\n" + "="*45)
    print(f"{'t':<20} {'y':<20}")
    print("="*45)
    for ti, yi in zip(t, y):
        print(f"{ti:<20.4f} {yi:<20.4f}")
    print("="*45 + "\n")

def mostrar_grafica(t, y):
    """Muestra gráfica de la solución"""
    plt.figure(figsize=(10, 6))
    plt.plot(t, y, 'r-o', linewidth=2, markersize=5)
    plt.grid(True)
    plt.xlabel('t', fontsize=12)
    plt.ylabel('y', fontsize=12)
    plt.title('Solución usando Método de Runge-Kutta 4', fontsize=14)
    plt.show()