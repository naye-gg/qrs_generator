# Generador de Códigos QR 🔲

Un generador de códigos QR en Python con múltiples opciones de personalización y estilos avanzados.

## 📋 Características

- ✅ Generar códigos QR simples
- ✅ Códigos QR personalizados con colores
- ✅ Códigos QR con logo central
- ✅ **NUEVO:** Diferentes estilos de módulos (cuadrados, círculos, redondeados, barras)
- ✅ **NUEVO:** Gradientes de colores (radial, horizontal, vertical)
- ✅ **NUEVO:** Combinación de estilos y logos
- ✅ Menú interactivo fácil de usar
- ✅ Corrección de errores configurable

## 🚀 Instalación

1. Asegúrate de tener Python 3.7 o superior instalado

2. Instala las dependencias:
```bash
pip install -r requirements.txt
```

## 💻 Uso

### Modo Interactivo (Recomendado)

Ejecuta el script y sigue el menú:
```bash
python qr_generator.py
```

### Generador Avanzado con Estilos

Para acceder directamente a las funciones avanzadas:
```bash
python qr_generator_advanced.py
```

### Ver Demostración de Estilos

Genera ejemplos de todos los estilos disponibles:
```bash
python demo_estilos.py
```

### Uso Programático

También puedes importar las funciones en tu propio código:

```python
from qr_generator import generar_qr_simple, generar_qr_personalizado, generar_qr_con_logo

# QR simple
generar_qr_simple("https://www.ejemplo.com", "mi_qr.png")

# QR personalizado
generar_qr_personalizado("Texto", "qr_azul.png", 
                         color_fondo="lightblue", 
                         color_frente="darkblue")

# QR con logo
generar_qr_con_logo("https://miempresa.com", "logo.png", "qr_empresa.png")
```

## 📂 Estructura

```
qrs_generator/
├── qr_generator.py           # Script principal con menú
├── qr_generator_advanced.py  # Generador con estilos avanzados ✨
├── demo_estilos.py           # Script de demostración
├── requirements.txt          # Dependencias
├── README.md                 # Este archivo
└── qr_codes/                 # Carpeta de códigos QR generados
    └── demos/                # Ejemplos de estilos
```

## 🎨 Ejemplos de Uso

### 1. Código QR para una URL
```python
generar_qr_simple("https://github.com", "github_qr.png")
```

### 2. Código QR con colores personalizados
```python
generar_qr_personalizado(
    "¡Hola Mundo!", 
    "hola_qr.png",
    color_fondo="yellow",
    color_frente="purple"
)
```

### 3. Código QR con logo de empresa
```python
generar_qr_con_logo(
    "https://miempresa.com",
    "logo_empresa.png",
    "qr_empresa.png"
)
```

### 4. Código QR con esquinas redondeadas ✨
```python
from qr_generator_advanced import generar_qr_con_estilo

generar_qr_con_estilo(
    "https://ejemplo.com",
    "qr_redondeado.png",
    estilo_modulo="redondeado",
    color_frente="darkblue",
    color_fondo="lightblue"
)
```

### 5. Código QR con gradiente radial 🌈
```python
from qr_generator_advanced import generar_qr_gradiente

generar_qr_gradiente(
    "¡Hola!",
    "qr_gradiente.png",
    tipo_gradiente="radial",
    color_centro="blue",
    color_borde="purple",
    color_fondo="white",
    estilo_modulo="circulo"
)
```

## 📐 Estilos de Módulos Disponibles

- **cuadrado** - Cuadrados sólidos (clásico)
- **cuadrado_gap** - Cuadrados con espacios entre ellos
- **circulo** - Puntos circulares
- **redondeado** - Cuadrados con esquinas redondeadas (recomendado)
- **barras_v** - Barras verticales
- **barras_h** - Barras horizontales

## 🎨 Tipos de Gradiente

- **radial** - Del centro hacia los bordes
- **horizontal** - De izquierda a derecha
- **vertical** - De arriba hacia abajo
- **cuadrado** - Gradiente en forma de cuadrado

## 🔧 Parámetros de Corrección de Errores

El código QR puede tener diferentes niveles de corrección de errores:

- `ERROR_CORRECT_L`: ~7% de corrección
- `ERROR_CORRECT_M`: ~15% de corrección (por defecto)
- `ERROR_CORRECT_Q`: ~25% de corrección
- `ERROR_CORRECT_H`: ~30% de corrección (necesario para logos)

## 📱 Colores Soportados

Puedes usar cualquier color HTML/CSS válido:
- Nombres: `"red"`, `"blue"`, `"green"`, `"yellow"`, etc.
- Hexadecimal: `"#FF5733"`, `"#3498DB"`, etc.
- RGB: `"rgb(255, 87, 51)"`, etc.

## 🤝 Contribuciones

¡Las contribuciones son bienvenidas! Siéntete libre de mejorar el código.

## 📄 Licencia

Este proyecto es de código abierto y está disponible para uso libre.

## ⚠️ Notas

- Los códigos QR se guardan en la carpeta `qr_codes/`
- Para QR con logo, asegúrate de usar imágenes PNG con fondo transparente para mejores resultados
- El logo debe ser aproximadamente 1/5 del tamaño del código QR

## 🐛 Solución de Problemas

### Error: "No module named 'qrcode'"
```bash
pip install qrcode[pil]
```

### Error: "No module named 'PIL'"
```bash
pip install Pillow
```

### El código QR no se escanea correctamente
- Aumenta el nivel de corrección de errores
- Asegúrate de que haya suficiente contraste entre colores
- Si usas logo, no debe ser demasiado grande
