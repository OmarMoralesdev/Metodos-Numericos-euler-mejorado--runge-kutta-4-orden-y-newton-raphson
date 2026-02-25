# Métodos Numéricos

Una aplicación interactiva en Python para resolver problemas matemáticos usando diferentes métodos numéricos.

## 📋 Métodos Incluidos

### 1. **Euler Mejorado** (Ecuaciones Diferenciales)
Resuelve ecuaciones diferenciales ordinarias de la forma:
```
dy/dx = f(x, y)
```

**Ejemplo:**
- Ecuación: `x + 2*y`
- Punto inicial: x₀ = 0, y₀ = 1
- Paso: h = 0.1
- Punto final: x = 2

### 2. **Runge-Kutta 4** (Ecuaciones Diferenciales)
Método más preciso para resolver ecuaciones diferenciales:
```
dy/dt = f(t, y)
```

**Ejemplo:**
- Ecuación: `y - t**2 + 1`
- Punto inicial: t₀ = 0, y₀ = 0.5
- Paso: h = 0.1
- Punto final: t = 2

### 3. **Newton-Raphson** (Búsqueda de Raíces)
Encuentra raíces de funciones no lineales de la forma:
```
f(x) = 0
```

**Ejemplo:**
- Función: `x**2 - 4`
- Derivada: `2*x`
- Valor inicial: x₀ = 3
- Tolerancia: 1e-7

## 🚀 Instalación

### Requisitos
- Python 3.7+
- pip

### Pasos

1. **Clonar o descargar el proyecto**
```bash
cd "Metodos Numericos"
```

2. **Crear un entorno virtual** (opcional pero recomendado)
```bash
python -m venv venv
```

3. **Activar el entorno virtual**

En Windows:
```bash
venv\Scripts\activate
```

En macOS/Linux:
```bash
source venv/bin/activate
```

4. **Instalar dependencias**
```bash
pip install -r requirements.txt
```

## 🎯 Uso

Ejecuta el programa:
```bash
python metodos_numericos/main.py
```

Verás un menú interactivo donde puedes seleccionar:
1. Euler Mejorado
2. Runge-Kutta 4
3. Newton-Raphson
4. Salir

### Ejemplo de Uso

```
==================================================
MÉTODOS NUMÉRICOS
==================================================
1. Euler Mejorado (ED)
2. Runge-Kutta 4 (ED)
3. Newton-Raphson (Raíces)
4. Salir
==================================================
Selecciona una opción (1-4): 1

--- MÉTODO DE EULER MEJORADO ---
Tu ecuación: x + 2*y
x inicial (x0): 0
y inicial (y0): 1
Paso (h): 0.1
x final: 2
```

## 📊 Salida

Cada método genera:
- **Tabla de resultados** con los valores calculados
- **Gráfica visual** para analizar los resultados

## 📦 Estructura del Proyecto

```
Metodos Numericos/
├── metodos_numericos/
│   ├── main.py                 # Programa principal
│   ├── euler_mejorado.py       # Implementación Euler Mejorado
│   ├── runge_kutta4.py         # Implementación Runge-Kutta 4
│   ├── newton_raphson.py       # Implementación Newton-Raphson
│   └── __pycache__/
├── requirements.txt            # Dependencias del proyecto
├── .gitignore                  # Archivos ignorados por Git
└── README.md                   # Este archivo
```

## 📚 Dependencias

- **numpy**: Cálculos numéricos
- **matplotlib**: Visualización de gráficos

## 🛠️ Desarrollo

Para modificar o extender los métodos:

1. Edita los archivos correspondientes en `metodos_numericos/`
2. Prueba los cambios ejecutando el programa
3. Asegúrate de que los cambios no rompan la funcionalidad existente

##  Notas Importantes

- Usa sintaxis Python estándar en las ecuaciones
- Reemplaza `^` con `**` para potencias
- Usa `np.sin()`, `np.cos()`, etc. para funciones trigonométricas
- Los valores iniciales deben ser números reales (float)

## 📝 Ejemplos de Ecuaciones Válidas

```
x + 2*y
x**2 - y
y * np.sin(x)
-2*t*y
np.exp(x) + y
```

## 👤 Autor

Métodos Numéricos - Proyecto Educativo

## 📄 Licencia

Este proyecto es de código abierto para propósitos educativos.
