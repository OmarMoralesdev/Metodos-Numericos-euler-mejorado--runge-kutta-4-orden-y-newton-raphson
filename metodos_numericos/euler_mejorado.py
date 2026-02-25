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
