import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import sympy as sp
import pandas as pd
from metodos_numericos.euler_mejorado import euler_mejorado
from metodos_numericos.runge_kutta4 import runge_kutta4
from metodos_numericos.newton_raphson import newton_raphson

# Estilos corporativos personalizados
st.markdown("""
    <style>
        :root {
            --color-primary: #367C2B;
            --color-accent: #FFCC00;
            --color-dark: #1a3f1f;
            --color-light: #f5f5f5;
        }
        
        * {
            font-family: 'Segoe UI', 'Trebuchet MS', sans-serif;
        }
        
        body {
            background-color: #ffffff;
            color: #2c3e50;
        }
        
        /* Encabezados */
        h1 {
            color: #367C2B;
            border-bottom: 3px solid #FFCC00;
            padding-bottom: 10px;
            font-weight: 700;
            letter-spacing: 0.5px;
        }
        
        h2 {
            color: #367C2B;
            margin-top: 20px;
            font-weight: 600;
        }
        
        h3 {
            color: #1a3f1f;
            font-weight: 600;
        }
        
        /* Botones */
        .stButton > button {
            background-color: #367C2B;
            color: white;
            border: none;
            border-radius: 4px;
            padding: 10px 24px;
            font-weight: 600;
            font-size: 15px;
            transition: all 0.3s ease;
            letter-spacing: 0.5px;
        }
        
        .stButton > button:hover {
            background-color: #1a3f1f;
            box-shadow: 0 2px 8px rgba(54, 124, 43, 0.3);
        }
        
        /* Inputs */
        .stTextInput > div > div > input,
        .stNumberInput > div > div > input {
            border-color: #367C2B;
            border-radius: 4px;
        }
        
        .stTextInput > div > div > input:focus,
        .stNumberInput > div > div > input:focus {
            border-color: #FFCC00;
            box-shadow: 0 0 0 2px rgba(54, 124, 43, 0.2);
        }
        
        /* Selectbox */
        .stSelectbox > div > div > div {
            border-color: #367C2B;
            border-radius: 4px;
        }
        
        /* Dataframe */
        .dataframe {
            border-collapse: collapse;
            width: 100%;
        }
        
        .dataframe thead th {
            background-color: #367C2B;
            color: white;
            font-weight: 600;
            padding: 12px;
            text-align: left;
            border: none;
        }
        
        .dataframe tbody td {
            padding: 10px 12px;
            border-bottom: 1px solid #e0e0e0;
        }
        
        .dataframe tbody tr:hover {
            background-color: #f0f8f5;
        }
        
        /* Info, Success, Warning, Error */
        .stSuccess {
            background-color: #e8f5e9;
            border-left: 4px solid #367C2B;
            border-radius: 4px;
        }
        
        .stInfo {
            background-color: #e3f2fd;
            border-left: 4px solid #367C2B;
            border-radius: 4px;
        }
        
        .stWarning {
            background-color: #fff3e0;
            border-left: 4px solid #f57c00;
            border-radius: 4px;
        }
        
        .stError {
            background-color: #ffebee;
            border-left: 4px solid #c62828;
            border-radius: 4px;
        }
        
        /* Línea divisora */
        hr {
            border-color: #FFCC00;
            margin: 30px 0;
        }
        
        /* Sidebar */
        .sidebar .sidebar-content {
            background-color: #f5f5f5;
        }
        
        /* Contenedor principal */
        .main {
            background-color: #ffffff;
        }
    </style>
""", unsafe_allow_html=True)

# Función para resolver ODE analíticamente con SymPy
def resolver_con_sympy(ecuacion_str, x0, y0):
    """Intenta resolver la ODE analíticamente usando SymPy."""
    try:
        x_sym = sp.symbols('x')
        y_sym = sp.Function('y')(x_sym)
        
        # Parsear la expresión con y como símbolo
        f_sym = sp.sympify(ecuacion_str, locals={'x': x_sym, 'y': y_sym})
        
        # Definir la ecuación diferencial: dy/dx = f(x,y)
        diffeq = sp.Eq(y_sym.diff(x_sym), f_sym)
        
        # Resolver con condición inicial
        sol = sp.dsolve(diffeq, y_sym, ics={y_sym.subs(x_sym, x0): y0})
        
        # Retornar una función lambda para evaluar rápido
        solucion_lambda = sp.lambdify(x_sym, sol.rhs, modules=['numpy', 'sympy'])
        
        # Validar que la función funciona
        try:
            test = float(solucion_lambda(x0))
        except:
            return None
        
        return solucion_lambda
    except:
        return None

st.set_page_config(page_title="Métodos Numéricos", layout="wide", initial_sidebar_state="expanded")

# Forzar tema claro
st.markdown("""
    <script>
        const htmlElement = document.documentElement;
        htmlElement.setAttribute('data-theme', 'light');
    </script>
""", unsafe_allow_html=True)

# Encabezado corporativo
st.markdown("""
    <div style='background: linear-gradient(135deg, #367C2B 0%, #1a3f1f 100%); padding: 40px; text-align: center; border-radius: 8px; margin-bottom: 30px;'>
        <h1 style='color: white; border: none; margin: 0; font-size: 2.5em; letter-spacing: 2px;'>METODOS NUMERICOS</h1>
        <p style='color: #FFCC00; margin: 10px 0 0 0; font-size: 1.1em; letter-spacing: 1px;'>Jesus Omar Morales Valenzuela - Grupo 8 B</p>
    </div>
""", unsafe_allow_html=True)

st.markdown("---")

# Menú lateral
metodo = st.sidebar.selectbox(
    "Selecciona un método:",
    ["Euler Mejorado", "Runge-Kutta 4", "Newton-Raphson"]
)

# EULER MEJORADO
if metodo == "Euler Mejorado":
    st.markdown("""
        <div style='background-color: #f5f5f5; padding: 20px; border-left: 4px solid #367C2B; border-radius: 4px; margin-bottom: 20px;'>
            <h2 style='margin-top: 0; color: #367C2B;'>Metodo de Euler Mejorado</h2>
            <p style='color: #555; margin: 5px 0; font-size: 1.02em;'>Resuelve ecuaciones diferenciales de la forma: <strong>dy/dx = f(x, y)</strong></p>
        </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
            <div style='background-color: #f9f9f9; padding: 15px; border-radius: 4px;'>
                <h3 style='color: #367C2B; margin-top: 0;'>Parametros</h3>
            </div>
        """, unsafe_allow_html=True)
        ecuacion = st.text_input(
            "Ecuación f(x, y):",
            value="x + 2*y",
            help="Ejemplos: x + 2*y, x - y, y*sin(x), exp(y)"
        )
        x0 = st.number_input("x inicial (x0):", value=0.0)
        y0 = st.number_input("y inicial (y0):", value=1.0)
        h = st.number_input("Paso (h):", value=0.1, min_value=0.01)
        x_final = st.number_input("x final:", value=2.0)
    
    with col2:
        st.markdown("""
            <div style='background-color: #f9f9f9; padding: 15px; border-radius: 4px;'>
                <h3 style='color: #367C2B; margin-top: 0;'>Ejemplos</h3>
            </div>
        """, unsafe_allow_html=True)
        st.code("x + 2*y\nx - y\ny*sin(x)")
    
    if st.button("Calcular", key="euler"):
        try:
            # Convertir ecuación a función con SymPy
            x_sym, y_sym = sp.symbols('x y')
            ecuacion_sym = sp.sympify(ecuacion)
            f_lambda = sp.lambdify((x_sym, y_sym), ecuacion_sym, 'numpy')
            
            def f(x, y):
                return f_lambda(x, y)
            
            # Intentar obtener la solución exacta
            f_exacta = resolver_con_sympy(ecuacion, x0, y0)
            
            # Calcular Euler Mejorado
            x_vals, y_vals = euler_mejorado(f, x0, y0, h, x_final)
            
            # Construir tabla con detalles
            datos_tabla = []
            for i in range(len(x_vals)):
                x_i = x_vals[i]
                y_i = y_vals[i]
                
                # Cálculo de una fila (k1, k2, y predictor, y mejorado)
                if i < len(x_vals) - 1:
                    k1 = f(x_i, y_i)
                    y_pred = y_i + h * k1
                    k2 = f(x_vals[i+1], y_pred)
                    y_mej = y_i + (h/2) * (k1 + k2)
                    err_abs = abs(y_mej - y_i)
                    
                    datos_tabla.append({
                        "x": round(x_i, 4),
                        "y": round(y_i, 10),
                        "y*": round(y_pred, 10),
                        "y_next": round(y_mej, 10),
                        "Error Absoluto": round(err_abs, 10)
                    })
                else:
                    datos_tabla.append({
                        "x": round(x_i, 4),
                        "y": round(y_i, 10),
                        "y*": np.nan,"y_next": np.nan,
                        "Error Absoluto": np.nan
                    })
            
            # Mostrar tabla
            st.markdown("""
                <div style='background-color: #f9f9f9; padding: 15px; border-radius: 4px; margin-top: 20px; margin-bottom: 20px;'>
                    <h3 style='color: #367C2B; margin-top: 0;'>Resultados</h3>
                </div>
            """, unsafe_allow_html=True)
            st.dataframe(pd.DataFrame(datos_tabla), width='stretch')
            
            if f_exacta is None:
                st.markdown("""
                    <div style='background-color: #e3f2fd; border-left: 4px solid #367C2B; border-radius: 4px; padding: 15px;'>
                        <p style='margin: 0; color: #555;'>SymPy no pudo encontrar solucion analitica exacta. El error relativo no está disponible.</p>
                    </div>
                """, unsafe_allow_html=True)
            
            # Mostrar gráfica
            fig, ax = plt.subplots(figsize=(10, 6))
            ax.plot(x_vals, y_vals, 'r-o', linewidth=2, markersize=6, label='Euler Mejorado')
  
            
            ax.grid(True, alpha=0.3)
            ax.set_xlabel('x', fontsize=12)
            ax.set_ylabel('y', fontsize=12)
            ax.set_title('Solución - Método de Euler Mejorado', fontsize=14)
            st.pyplot(fig)
            
        except Exception as e:
            st.markdown(f"""
                <div style='background-color: #ffebee; border-left: 4px solid #c62828; border-radius: 4px; padding: 20px;'>
                    <p style='margin: 0; color: #c62828; font-weight: 600;'>Error en el calculo</p>
                    <p style='margin: 8px 0 0 0; color: #555; font-size: 0.95em;'>{str(e)}</p>
                </div>
            """, unsafe_allow_html=True)

# RUNGE-KUTTA 4
elif metodo == "Runge-Kutta 4":
    st.markdown("""
        <div style='background-color: #f5f5f5; padding: 20px; border-left: 4px solid #367C2B; border-radius: 4px; margin-bottom: 20px;'>
            <h2 style='margin-top: 0; color: #367C2B;'>Metodo de Runge-Kutta 4</h2>
            <p style='color: #555; margin: 5px 0; font-size: 1.02em;'>Resuelve ecuaciones diferenciales: <strong>dy/dx = f(x, y)</strong> (Alta precision)</p>
        </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
            <div style='background-color: #f9f9f9; padding: 15px; border-radius: 4px;'>
                <h3 style='color: #367C2B; margin-top: 0;'>Parametros</h3>
            </div>
        """, unsafe_allow_html=True)
        ecuacion = st.text_input(
            "Ecuación f(x, y):",
            value="y - x**2 + 1",
            help="Ejemplos: y - x**2 + 1, -2*x*y, y*sin(x)"
        )
        x0 = st.number_input("x inicial (x0):", value=0.0, key="rk4_x0")
        y0 = st.number_input("y inicial (y0):", value=0.5, key="rk4_y0")
        h = st.number_input("Paso (h):", value=0.1, min_value=0.01, key="rk4_h")
        x_end = st.number_input("x final:", value=2.0, key="rk4_xend")
    
    with col2:
        st.markdown("""
            <div style='background-color: #f9f9f9; padding: 15px; border-radius: 4px;'>
                <h3 style='color: #367C2B; margin-top: 0;'>Ejemplos</h3>
            </div>
        """, unsafe_allow_html=True)
        st.code("y - x**2 + 1\n-2*x*y\ny*sin(x)\nx + y")
    
    if st.button("Calcular", key="rk4"):
        try:
            # Convertir ecuación a función con SymPy
            x_sym, y_sym = sp.symbols('x y')
            ecuacion_sym = sp.sympify(ecuacion)
            f_lambda = sp.lambdify((x_sym, y_sym), ecuacion_sym, 'numpy')
            
            def f(x, y):
                return f_lambda(x, y)
            
            x, y, k1, k2, k3, k4 = runge_kutta4(f, x0, y0, x_end, h)
            
            # Mostrar tabla
            st.markdown("""
                <div style='background-color: #f9f9f9; padding: 15px; border-radius: 4px; margin-top: 20px; margin-bottom: 20px;'>
                    <h3 style='color: #367C2B; margin-top: 0;'>Resultados</h3>
                </div>
            """, unsafe_allow_html=True)
            df_data = {
                "x": x,
                "y": y,
                "y(n+1)": list(y[1:]) + [np.nan],
                "K1": list(k1) + [np.nan],
                "K2": list(k2) + [np.nan],
                "K3": list(k3) + [np.nan],
                "K4": list(k4) + [np.nan],
            }
            st.dataframe(df_data, width='stretch')
            
            # Mostrar gráfica
            fig, ax = plt.subplots(figsize=(10, 6))
            ax.plot(x, y, 'b-o', linewidth=2, markersize=6)
            ax.grid(True, alpha=0.3)
            ax.set_xlabel('x', fontsize=12)
            ax.set_ylabel('y', fontsize=12)
            ax.set_title('Solución - Método de Runge-Kutta 4', fontsize=14)
            st.pyplot(fig)
            
        except Exception as e:
            st.markdown(f"""
                <div style='background-color: #ffebee; border-left: 4px solid #c62828; border-radius: 4px; padding: 20px;'>
                    <p style='margin: 0; color: #c62828; font-weight: 600;'>Error en el calculo</p>
                    <p style='margin: 8px 0 0 0; color: #555; font-size: 0.95em;'>{str(e)}</p>
                </div>
            """, unsafe_allow_html=True)

# NEWTON-RAPHSON
elif metodo == "Newton-Raphson":
    st.markdown("""
        <div style='background-color: #f5f5f5; padding: 20px; border-left: 4px solid #367C2B; border-radius: 4px; margin-bottom: 20px;'>
            <h2 style='margin-top: 0; color: #367C2B;'>Metodo de Newton-Raphson</h2>
            <p style='color: #555; margin: 5px 0; font-size: 1.02em;'>Encuentra raices de funciones: <strong>f(x) = 0</strong></p>
        </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
            <div style='background-color: #f9f9f9; padding: 15px; border-radius: 4px;'>
                <h3 style='color: #367C2B; margin-top: 0;'>Parametros</h3>
            </div>
        """, unsafe_allow_html=True)
        ecuacion = st.text_input(
            "Función f(x):",
            value="x**2 - 4",
            help="Ejemplos: x**2 - 4, x**3 - 2*x - 5, sin(x) - x/2"
        )
        x0 = st.number_input("x inicial (x0):", value=3.0, key="nr_x0")
        tol = st.number_input("Tolerancia:", value=1e-7, format="%.0e", key="nr_tol")
        max_iter = st.number_input("Máximo de iteraciones:", value=1000, key="nr_iter")
    
    with col2:
        st.markdown("""
            <div style='background-color: #f9f9f9; padding: 15px; border-radius: 4px;'>
                <h3 style='color: #367C2B; margin-top: 0;'>Ejemplos</h3>
            </div>
        """, unsafe_allow_html=True)
        st.code("x**2 - 4\nx**3 - 2*x - 5\nsin(x) - x/2\nx**2 - 2")
    
    if st.button("Calcular", key="nr"):
        try:
            # Crear variable simbólica
            x = sp.Symbol('x')
            
            # Parsear la ecuación directamente (reconoce funciones automáticamente)
            ecuacion_sym = sp.sympify(ecuacion.replace('^', '**'))
            
            # Calcular derivada automáticamente
            derivada_sym = sp.diff(ecuacion_sym, x)
            
            # Convertir a funciones evaluables
            def f(x_val):
                return float(ecuacion_sym.subs(x, x_val))
            
            def df(x_val):
                return float(derivada_sym.subs(x, x_val))
            
            raiz, iteraciones = newton_raphson(f, df, x0, tol, max_iter)
            
            if raiz is not None:
                st.markdown("""
                    <div style='background-color: #e8f5e9; border-left: 4px solid #367C2B; border-radius: 4px; padding: 20px; text-align: center; margin: 20px 0;'>
                        <p style='margin: 0; color: #555; font-size: 0.95em;'>RAIZ ENCONTRADA</p>
                        <p style='margin: 10px 0 0 0; color: #367C2B; font-size: 2em; font-weight: 700;'>{:.10f}</p>
                    </div>
                """.format(raiz), unsafe_allow_html=True)
                
                # Mostrar tabla de iteraciones con detalles
                st.markdown("""
                    <div style='background-color: #f9f9f9; padding: 15px; border-radius: 4px; margin-top: 20px; margin-bottom: 20px;'>
                        <h3 style='color: #367C2B; margin-top: 0;'>Iteraciones</h3>
                    </div>
                """, unsafe_allow_html=True)
                tabla_iteraciones = {
                    "i": list(range(len(iteraciones))),
                    "x": iteraciones,
                    "f(x)": [f(xi) for xi in iteraciones],
                    "f'(x)": [df(xi) for xi in iteraciones]
                }
                st.dataframe(tabla_iteraciones, width='stretch')
                
                # Mostrar gráfica
                x_min = min(iteraciones) - 2
                x_max = max(iteraciones) + 2
                x_vals = np.linspace(x_min, x_max, 200)
                y_vals = [f(xi) for xi in x_vals]
                
                fig, ax = plt.subplots(figsize=(10, 6))
                ax.plot(x_vals, y_vals, 'g-', linewidth=2, label='f(x)')
                ax.axhline(y=0, color='k', linestyle='--', alpha=0.3)
             #   ax.plot(iteraciones, [f(x_val) for x_val in iteraciones], 'ro-', markersize=8, label='Iteraciones')
                ax.plot(raiz, 0, 'ro', markersize=10, label=f'Raíz = {raiz:.6f}')
                ax.grid(True, alpha=0.3)
                ax.set_xlabel('x', fontsize=12)
                ax.set_ylabel('f(x)', fontsize=12)
                ax.set_title('Método de Newton-Raphson', fontsize=14)
                ax.legend()
                st.pyplot(fig)
            else:
                st.markdown("""
                    <div style='background-color: #fff3e0; border-left: 4px solid #f57c00; border-radius: 4px; padding: 20px; text-align: center;'>
                        <p style='margin: 0; color: #555; font-size: 1em;'>No se encontro raiz convergente. Intenta con otros parametros.</p>
                    </div>
                """, unsafe_allow_html=True)
            
        except Exception as e:
            st.markdown(f"""
                <div style='background-color: #ffebee; border-left: 4px solid #c62828; border-radius: 4px; padding: 20px;'>
                    <p style='margin: 0; color: #c62828; font-weight: 600;'>Error en el calculo</p>
                    <p style='margin: 8px 0 0 0; color: #555; font-size: 0.95em;'>{str(e)}</p>
                </div>
            """, unsafe_allow_html=True)

# Footer corporativo
st.markdown("---")
st.markdown("""
    <div style='background-color: #367C2B; padding: 30px; text-align: center; border-radius: 8px; margin-top: 40px;'>
        <p style='color: white; margin: 0; font-size: 1.05em; letter-spacing: 0.5px; font-weight: 500;'>
            METODOS NUMERICOS - SOLUCION INNOVADORA
        </p>
        <p style='color: #FFCC00; margin: 8px 0 0 0; font-size: 0.95em;'>
            Desarrollado por Jesus Omar Morales Valenzuela
        </p>
    </div>
""", unsafe_allow_html=True)
