# Generador de Códigos QR 🔲

Un generador de códigos QR en Python con múltiples opciones de personalización.

## 📋 Características

- ✅ Generar códigos QR simples
- ✅ Códigos QR personalizados con colores
- ✅ Códigos QR con logo central
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
├── qr_generator.py      # Script principal
├── requirements.txt     # Dependencias
├── README.md           # Este archivo
└── qr_codes/           # Carpeta donde se guardan los QR (se crea automáticamente)
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
