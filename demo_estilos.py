#!/usr/bin/env python3
"""
Script de demostración de estilos de QR
Genera ejemplos de todos los estilos disponibles
"""

from qr_generator_advanced import (
    generar_qr_con_estilo,
    generar_qr_gradiente,
    mostrar_estilos_disponibles
)
import os


def generar_ejemplos():
    """Genera ejemplos de todos los estilos"""
    
    # Crear carpeta de demostración
    demo_folder = "demos"
    if not os.path.exists(demo_folder):
        os.makedirs(demo_folder)
    
    os.chdir(demo_folder)
    
    print("=" * 60)
    print("  GENERANDO EJEMPLOS DE CÓDIGOS QR CON DIFERENTES ESTILOS")
    print("=" * 60)
    print()
    
    texto_ejemplo = "https://github.com/naye-gg/qrs_generator"
    
    # Ejemplos con diferentes estilos de módulos
    print("📐 Generando QR con diferentes estilos de módulos...\n")
    
    estilos = [
        ('cuadrado', 'navy', 'lightblue'),
        ('cuadrado_gap', 'darkgreen', 'lightgreen'),
        ('circulo', 'darkred', 'lightyellow'),
        ('redondeado', 'purple', 'lavender'),
        ('barras_v', 'darkorange', 'lightyellow'),
        ('barras_h', 'darkblue', 'lightcyan')
    ]
    
    for estilo, color_frente, color_fondo in estilos:
        nombre = f"ejemplo_{estilo}.png"
        generar_qr_con_estilo(texto_ejemplo, nombre, estilo, color_frente, color_fondo)
    
    print("\n🎨 Generando QR con gradientes...\n")
    
    # Ejemplos con gradientes
    gradientes = [
        ('radial', 'blue', 'purple', 'redondeado'),
        ('horizontal', 'red', 'orange', 'circulo'),
        ('vertical', 'green', 'yellow', 'redondeado'),
        ('cuadrado', 'navy', 'cyan', 'cuadrado_gap')
    ]
    
    for tipo_grad, color1, color2, estilo in gradientes:
        nombre = f"gradiente_{tipo_grad}.png"
        generar_qr_gradiente(texto_ejemplo, nombre, tipo_grad, color1, color2, 'white', estilo)
    
    print("\n" + "=" * 60)
    print("✅ ¡Todos los ejemplos generados en la carpeta 'demos'!")
    print("=" * 60)
    print("\n📁 Archivos generados:")
    print("\nEstilos básicos:")
    for estilo, _, _ in estilos:
        print(f"  - ejemplo_{estilo}.png")
    
    print("\nGradientes:")
    for tipo_grad, _, _, _ in gradientes:
        print(f"  - gradiente_{tipo_grad}.png")
    
    print("\n💡 Tip: Abre los archivos para ver las diferencias entre estilos")


if __name__ == "__main__":
    # Volver a la carpeta qr_codes si existe
    if os.path.exists("../qr_codes"):
        os.chdir("../qr_codes")
    elif not os.path.exists("qr_codes"):
        os.makedirs("qr_codes")
        os.chdir("qr_codes")
    
    generar_ejemplos()
