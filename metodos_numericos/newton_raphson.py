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

def mostrar_tabla(iteraciones):
    """Muestra tabla de iteraciones"""
    print("\n" + "="*50)
    print(f"{'Iteración':<15} {'x':<35}")
    print("="*50)
    for i, xi in enumerate(iteraciones):
        print(f"{i:<15} {xi:<35.10f}")
    print("="*50 + "\n")

def mostrar_grafica(iteraciones, f, x_range):
    """Muestra gráfica de la función y las iteraciones"""
    x = np.linspace(x_range[0], x_range[1], 1000)
    y = [f(xi) for xi in x]
    
    plt.figure(figsize=(10, 6))
    plt.plot(x, y, 'b-', linewidth=2, label='f(x)')
    plt.axhline(y=0, color='k', linestyle='--', linewidth=0.5)
    plt.axvline(x=0, color='k', linestyle='--', linewidth=0.5)
    
    y_iter = [f(xi) for xi in iteraciones]
    plt.plot(iteraciones, y_iter, 'ro-', linewidth=2, markersize=8, label='Iteraciones Newton-Raphson')
    
    plt.grid(True)
    plt.xlabel('x', fontsize=12)
    plt.ylabel('f(x)', fontsize=12)
    plt.title('Método de Newton-Raphson', fontsize=14)
    plt.legend(fontsize=10)
    plt.show()