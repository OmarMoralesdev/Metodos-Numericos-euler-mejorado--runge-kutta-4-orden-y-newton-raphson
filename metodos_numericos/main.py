import numpy as np
import matplotlib.pyplot as plt
from euler_mejorado import euler_mejorado, mostrar_tabla as tabla_euler, mostrar_grafica as grafica_euler
from runge_kutta4 import runge_kutta4, mostrar_tabla as tabla_rk4, mostrar_grafica as grafica_rk4
from newton_raphson import newton_raphson, mostrar_tabla as tabla_nr, mostrar_grafica as grafica_nr

def menu_principal():
    """Menú principal para seleccionar método"""
    print("\n" + "="*50)
    print("MÉTODOS NUMÉRICOS")
    print("="*50)
    print("1. Euler Mejorado (ED)")
    print("2. Runge-Kutta 4 (ED)")
    print("3. Newton-Raphson (Raíces)")
    print("4. Salir")
    print("="*50)
    
    opcion = input("Selecciona una opción (1-4): ")
    return opcion

def metodo_euler():
    """Ejecuta Euler Mejorado"""
    try:
        print("\n--- MÉTODO DE EULER MEJORADO ---")
        print("Ingresa tu ecuación diferencial dy/dx = f(x, y)")
        print("Ejemplos:")
        print("  - x + 2*y")
        print("  - x - y")
        print("  - y * np.sin(x)")
        
        ecuacion = input("Tu ecuación: ")
        
        def f(x, y):
            return eval(ecuacion)
        
        x0 = float(input("x inicial (x0): "))
        y0 = float(input("y inicial (y0): "))
        h = float(input("Paso (h): "))
        x_final = float(input("x final: "))
        
        x, y = euler_mejorado(f, x0, y0, h, x_final)
        
        tabla_euler(x, y)
        grafica_euler(x, y)
    except Exception as e:
        print(f"\n Error: {str(e)}")
        print("Verifica tu entrada e intenta de nuevo.")

def metodo_runge_kutta():
    """Ejecuta Runge-Kutta 4"""
    try:
        print("\n--- MÉTODO DE RUNGE-KUTTA 4 ---")
        print("Ingresa tu ecuación diferencial dy/dx = f(x, y)")
        print("Ejemplos:")
        print("  - y - x**2 + 1")
        print("  - -2*x*y")
        print("  - y * np.sin(x)")
        
        ecuacion = input("Tu ecuación: ")
        
        def f(x, y):
            return eval(ecuacion)
        
        x0 = float(input("x inicial (x0): "))
        y0 = float(input("y inicial (y0): "))
        h = float(input("Paso (h): "))
        x_end = float(input("x final: "))
        
        x, y, k1, k2, k3, k4, k = runge_kutta4(f, x0, y0, x_end, h)
        
        tabla_rk4(x, y, k1, k2, k3, k4, k)
        grafica_rk4(x, y)
    except Exception as e:
        print(f"\n Error: {str(e)}")
        print("Verifica tu entrada e intenta de nuevo.")

def metodo_newton_raphson():
    """Ejecuta Newton-Raphson"""
    try:
        print("\n--- MÉTODO DE NEWTON-RAPHSON ---")
        print("Ingresa tu función f(x)")
        print("Ejemplos:")
        print("  - x**2 - 4")
        print("  - x**3 - 2*x - 5")
        print("  - np.sin(x) - x/2")
        
        ecuacion = input("Tu función f(x): ")
        ecuacion = ecuacion.replace("^", "**")
        
        derivada = input("Tu derivada f'(x): ")
        derivada = derivada.replace("^", "**")
        
        def f(x):
            return eval(ecuacion)
        
        def df(x):
            return eval(derivada)
        
        x0 = float(input("x inicial (x0): "))
        tol = float(input("Tolerancia (default 1e-7): ") or "1e-7")
        max_iter = int(input("Máximo de iteraciones (default 1000): ") or "1000")
        
        raiz, iteraciones = newton_raphson(f, df, x0, tol, max_iter)
        
        if raiz is not None:
            print(f"\nRaíz encontrada: {raiz:.10f}")
            tabla_nr(iteraciones)
            
            x_min = min(iteraciones) - 2
            x_max = max(iteraciones) + 2
            grafica_nr(iteraciones, f, (x_min, x_max))
        else:
            print(" No se encontró raíz. Intenta con otros parámetros.")
    except Exception as e:
        print(f"\n Error: {str(e)}")
        print("Verifica tu entrada e intenta de nuevo.")

def main():
    """Función principal"""
    while True:
        opcion = menu_principal()
        
        if opcion == "1":
            metodo_euler()
        elif opcion == "2":
            metodo_runge_kutta()
        elif opcion == "3":
            metodo_newton_raphson()
        elif opcion == "4":
            print("\n¡Hasta luego!")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")
        
        input("\nPresiona Enter para continuar...")

if __name__ == "__main__":
    main()