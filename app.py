import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from metodos_numericos.euler_mejorado import euler_mejorado
from metodos_numericos.runge_kutta4 import runge_kutta4
from metodos_numericos.newton_raphson import newton_raphson

st.set_page_config(page_title="Métodos Numéricos", layout="wide")

# Título principal
st.title("Métodos Numéricos")
st.markdown("---")

# Menú lateral
metodo = st.sidebar.selectbox(
    "Selecciona un método:",
    ["Euler Mejorado", "Runge-Kutta 4", "Newton-Raphson"]
)

# EULER MEJORADO
if metodo == "Euler Mejorado":
    st.header("Método de Euler Mejorado")
    st.write("Resuelve ecuaciones diferenciales de la forma: **dy/dx = f(x, y)**")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Parámetros")
        ecuacion = st.text_input(
            "Ecuación f(x, y):",
            value="x + 2*y",
            help="Ejemplos: x + 2*y, x - y, y * np.sin(x)"
        )
        x0 = st.number_input("x inicial (x0):", value=0.0)
        y0 = st.number_input("y inicial (y0):", value=1.0)
        h = st.number_input("Paso (h):", value=0.1, min_value=0.01)
        x_final = st.number_input("x final:", value=2.0)
    
    with col2:
        st.subheader("Ejemplos")
        st.code("x + 2*y\nx - y\ny * np.sin(x)\nx**2 + y")
    
    if st.button("Calcular", key="euler"):
        try:
            def f(x, y):
                return eval(ecuacion)
            
            x, y = euler_mejorado(f, x0, y0, h, x_final)
            
            # Calcular y(n+1) - valor predictor y mejorado
            y_pred = []
            y_mejorado = []
            error_abs = []
            for i in range(len(x) - 1):
                k1 = f(x[i], y[i])
                y_pred_val = y[i] + h * k1
                y_pred.append(y_pred_val)
                k2 = f(x[i+1], y_pred_val)
                y_mej = y[i] + (h / 2) * (k1 + k2)
                y_mejorado.append(y_mej)
                error_abs.append(abs(y_mej - y[i]))
            y_pred.append("-")
            y_mejorado.append("-")
            error_abs.append("-")
            
            # Mostrar tabla
            st.subheader("Resultados")
            df_data = {"x": x, 
                       "y": y,
                       "y(n+1)": y_pred,
                       "y(n+1) Mejorado": y_mejorado,
                       "Error Absoluto": error_abs,
                       }
            st.dataframe(df_data, use_container_width=True)
            
            # Mostrar gráfica
            fig, ax = plt.subplots(figsize=(10, 6))
            ax.plot(x, y, 'r-o', linewidth=2, markersize=6)
            ax.grid(True, alpha=0.3)
            ax.set_xlabel('x', fontsize=12)
            ax.set_ylabel('y', fontsize=12)
            ax.set_title('Solución - Método de Euler Mejorado', fontsize=14)
            st.pyplot(fig)
            
        except Exception as e:
            st.error(f" Error: {str(e)}")

# RUNGE-KUTTA 4
elif metodo == "Runge-Kutta 4":
    st.header("Método de Runge-Kutta 4")
    st.write("Resuelve ecuaciones diferenciales: **dy/dx = f(x, y)** (más preciso)")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Parámetros")
        ecuacion = st.text_input(
            "Ecuación f(x, y):",
            value="y - x**2 + 1",
            help="Ejemplos: y - x**2 + 1, -2*x*y, y * np.sin(x)"
        )
        x0 = st.number_input("x inicial (x0):", value=0.0, key="rk4_x0")
        y0 = st.number_input("y inicial (y0):", value=0.5, key="rk4_y0")
        h = st.number_input("Paso (h):", value=0.1, min_value=0.01, key="rk4_h")
        x_end = st.number_input("x final:", value=2.0, key="rk4_xend")
    
    with col2:
        st.subheader("Ejemplos")
        st.code("y - x**2 + 1\n-2*x*y\ny * np.sin(x)\nx + y")
    
    if st.button("Calcular", key="rk4"):
        try:
            def f(x, y):
                return eval(ecuacion)
            
            x, y, k1, k2, k3, k4 = runge_kutta4(f, x0, y0, x_end, h)
            
            # Mostrar tabla
            st.subheader("Resultados")
            df_data = {
                "x": x,
                "y": y,
                "y(n+1)": list(y[1:]) + ["-"],
                "K1": list(k1) + ["-"],
                "K2": list(k2) + ["-"],
                "K3": list(k3) + ["-"],
                "K4": list(k4) + ["-"],
            }
            st.dataframe(df_data, use_container_width=True)
            
            # Mostrar gráfica
            fig, ax = plt.subplots(figsize=(10, 6))
            ax.plot(x, y, 'b-o', linewidth=2, markersize=6)
            ax.grid(True, alpha=0.3)
            ax.set_xlabel('x', fontsize=12)
            ax.set_ylabel('y', fontsize=12)
            ax.set_title('Solución - Método de Runge-Kutta 4', fontsize=14)
            st.pyplot(fig)
            
        except Exception as e:
            st.error(f" Error: {str(e)}")

# NEWTON-RAPHSON
elif metodo == "Newton-Raphson":
    st.header("Método de Newton-Raphson")
    st.write("Encuentra raíces de funciones: **f(x) = 0**")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Parámetros")
        ecuacion = st.text_input(
            "Función f(x):",
            value="x**2 - 4",
            help="Ejemplos: x**2 - 4, x**3 - 2*x - 5, np.sin(x) - x/2"
        )
        derivada = st.text_input(
            "Derivada f'(x):",
            value="2*x",
            help="La derivada de tu función"
        )
        x0 = st.number_input("x inicial (x0):", value=3.0, key="nr_x0")
        tol = st.number_input("Tolerancia:", value=1e-7, format="%.0e", key="nr_tol")
        max_iter = st.number_input("Máximo de iteraciones:", value=1000, key="nr_iter")
    
    with col2:
        st.subheader("Ejemplos")
        st.code("f(x) = x**2 - 4\nf'(x) = 2*x\n\nf(x) = x**3 - 2*x - 5\nf'(x) = 3*x**2 - 2")
    
    if st.button("Calcular", key="nr"):
        try:
            def f(x):
                return eval(ecuacion)
            
            def df(x):
                return eval(derivada)
            
            raiz, iteraciones = newton_raphson(f, df, x0, tol, max_iter)
            
            if raiz is not None:
                st.success(f" Raíz encontrada: **{raiz:.10f}**")
                
                # Mostrar tabla de iteraciones
                st.subheader("Iteraciones")
                df_iter = {"x": iteraciones}
                st.dataframe(df_iter, use_container_width=True)
                
                # Mostrar gráfica
                x_min = min(iteraciones) - 2
                x_max = max(iteraciones) + 2
                x_vals = np.linspace(x_min, x_max, 200)
                y_vals = [f(xi) for xi in x_vals]
                
                fig, ax = plt.subplots(figsize=(10, 6))
                ax.plot(x_vals, y_vals, 'g-', linewidth=2, label='f(x)')
                ax.axhline(y=0, color='k', linestyle='--', alpha=0.3)
                ax.plot(iteraciones, [f(x) for x in iteraciones], 'ro-', markersize=8, label='Iteraciones')
                ax.plot(raiz, 0, 'r*', markersize=20, label=f'Raíz = {raiz:.6f}')
                ax.grid(True, alpha=0.3)
                ax.set_xlabel('x', fontsize=12)
                ax.set_ylabel('f(x)', fontsize=12)
                ax.set_title('Método de Newton-Raphson', fontsize=14)
                ax.legend()
                st.pyplot(fig)
            else:
                st.warning(" No se encontró raíz. Intenta con otros parámetros.")
            
        except Exception as e:
            st.error(f" Error: {str(e)}")

# Footer
st.markdown("---")
st.markdown("""
    <div style='text-align: center'>
        <p>Métodos Numéricos • Desarrollado con Streamlit</p>
    </div>
""", unsafe_allow_html=True)
