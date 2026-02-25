import numpy as np
import matplotlib.pyplot as plt

def newton_raphson(f, df, x0, tol=1e-7, max_iter=1000):
    """Método de Newton-Raphson"""
    x = x0
    iteraciones = [x0]
    
    for i in range(max_iter):
        fx = f(x)
        dfx = df(x)
        
        if dfx == 0:
            print("Derivada es cero. No se puede continuar.")
            return None, None
        
        x_new = x - fx / dfx
        iteraciones.append(x_new)
        
        if abs(x_new - x) < tol:
            print(f"Convergencia alcanzada después de {i+1} iteraciones.")
            return x_new, iteraciones
        
        x = x_new
    
    print("Número máximo de iteraciones alcanzado sin convergencia.")
    return x, iteraciones
