import numpy as np
import matplotlib.pyplot as plt


def runge_kutta4(f, x0, y0, x_final, h):
    # Generamos los puntos de x (usamos linspace para evitar errores de precisión en el stop)
    pasos = int(round((x_final - x0) / h))
    x = np.linspace(x0, x_final, pasos + 1)
    y = np.zeros(len(x))
    y[0] = y0
    
    k1_list, k2_list, k3_list, k4_list = [], [], [], []
    
    for i in range(len(x) - 1):
        k1 = f(x[i], y[i])
        k2 = f(x[i] + h/2, y[i] + (h/2) * k1)
        k3 = f(x[i] + h/2, y[i] + (h/2) * k2)
        k4 = f(x[i] + h, y[i] + h * k3)
        
        k1_list.append(k1)
        k2_list.append(k2)
        k3_list.append(k3)
        k4_list.append(k4)
        
        y[i+1] = y[i] + (h / 6) * (k1 + 2*k2 + 2*k3 + k4)
    
    return x, y, k1_list, k2_list, k3_list, k4_list
