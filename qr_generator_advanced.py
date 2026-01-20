#!/usr/bin/env python3
"""
Generador Avanzado de Códigos QR con Estilos
Permite crear códigos QR con diferentes formas de módulos y esquinas
"""

import qrcode
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.moduledrawers import (
    SquareModuleDrawer,
    GappedSquareModuleDrawer,
    CircleModuleDrawer,
    RoundedModuleDrawer,
    VerticalBarsDrawer,
    HorizontalBarsDrawer
)
from qrcode.image.styles.colormasks import (
    SolidFillColorMask,
    SquareGradiantColorMask,
    RadialGradiantColorMask,
    HorizontalGradiantColorMask,
    VerticalGradiantColorMask
)
from PIL import Image
import os


def generar_qr_con_estilo(datos, nombre_archivo="qr_estilo.png", 
                          estilo_modulo="cuadrado", 
                          color_frente="black", 
                          color_fondo="white"):
    """
    Genera un código QR con diferentes estilos de módulos (puntas)
    
    Args:
        datos (str): Texto o URL para codificar
        nombre_archivo (str): Nombre del archivo de salida
        estilo_modulo (str): Tipo de módulo: 'cuadrado', 'cuadrado_gap', 
                            'circulo', 'redondeado', 'barras_v', 'barras_h'
        color_frente (str): Color del código QR
        color_fondo (str): Color de fondo
    """
    
    # Mapeo de estilos
    estilos = {
        'cuadrado': SquareModuleDrawer(),
        'cuadrado_gap': GappedSquareModuleDrawer(),
        'circulo': CircleModuleDrawer(),
        'redondeado': RoundedModuleDrawer(),
        'barras_v': VerticalBarsDrawer(),
        'barras_h': HorizontalBarsDrawer()
    }
    
    # Crear el QR
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )
    
    qr.add_data(datos)
    qr.make(fit=True)
    
    # Seleccionar el drawer
    drawer = estilos.get(estilo_modulo, SquareModuleDrawer())
    
    # Crear imagen con estilo
    img = qr.make_image(
        image_factory=StyledPilImage,
        module_drawer=drawer,
        color_mask=SolidFillColorMask(
            back_color=color_fondo,
            front_color=color_frente
        )
    )
    
    img.save(nombre_archivo)
    print(f"✓ QR con estilo '{estilo_modulo}' generado: {nombre_archivo}")


def generar_qr_gradiente(datos, nombre_archivo="qr_gradiente.png",
                         tipo_gradiente="radial",
                         color_centro="blue",
                         color_borde="purple",
                         color_fondo="white",
                         estilo_modulo="redondeado"):
    """
    Genera un código QR con gradiente de color
    
    Args:
        datos (str): Texto o URL para codificar
        nombre_archivo (str): Nombre del archivo de salida
        tipo_gradiente (str): 'radial', 'horizontal', 'vertical', 'cuadrado'
        color_centro (str): Color del centro/inicio
        color_borde (str): Color del borde/fin
        color_fondo (str): Color de fondo
        estilo_modulo (str): Estilo de los módulos
    """
    
    # Mapeo de estilos de módulos
    estilos = {
        'cuadrado': SquareModuleDrawer(),
        'cuadrado_gap': GappedSquareModuleDrawer(),
        'circulo': CircleModuleDrawer(),
        'redondeado': RoundedModuleDrawer(),
        'barras_v': VerticalBarsDrawer(),
        'barras_h': HorizontalBarsDrawer()
    }
    
    # Mapeo de gradientes
    gradientes = {
        'radial': RadialGradiantColorMask(
            back_color=color_fondo,
            center_color=color_centro,
            edge_color=color_borde
        ),
        'horizontal': HorizontalGradiantColorMask(
            back_color=color_fondo,
            left_color=color_centro,
            right_color=color_borde
        ),
        'vertical': VerticalGradiantColorMask(
            back_color=color_fondo,
            top_color=color_centro,
            bottom_color=color_borde
        ),
        'cuadrado': SquareGradiantColorMask(
            back_color=color_fondo,
            center_color=color_centro,
            edge_color=color_borde
        )
    }
    
    # Crear el QR
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )
    
    qr.add_data(datos)
    qr.make(fit=True)
    
    # Crear imagen con gradiente
    img = qr.make_image(
        image_factory=StyledPilImage,
        module_drawer=estilos.get(estilo_modulo, RoundedModuleDrawer()),
        color_mask=gradientes.get(tipo_gradiente, RadialGradiantColorMask(
            back_color=color_fondo,
            center_color=color_centro,
            edge_color=color_borde
        ))
    )
    
    img.save(nombre_archivo)
    print(f"✓ QR con gradiente '{tipo_gradiente}' generado: {nombre_archivo}")


def generar_qr_con_logo_y_estilo(datos, ruta_logo, nombre_archivo="qr_logo_estilo.png",
                                  estilo_modulo="redondeado",
                                  color_frente="black",
                                  color_fondo="white"):
    """
    Genera un código QR estilizado con logo en el centro
    
    Args:
        datos (str): Texto o URL para codificar
        ruta_logo (str): Ruta de la imagen del logo
        nombre_archivo (str): Nombre del archivo de salida
        estilo_modulo (str): Estilo de los módulos
        color_frente (str): Color del QR
        color_fondo (str): Color de fondo
    """
    
    estilos = {
        'cuadrado': SquareModuleDrawer(),
        'cuadrado_gap': GappedSquareModuleDrawer(),
        'circulo': CircleModuleDrawer(),
        'redondeado': RoundedModuleDrawer(),
        'barras_v': VerticalBarsDrawer(),
        'barras_h': HorizontalBarsDrawer()
    }
    
    # Crear el QR con estilo
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )
    
    qr.add_data(datos)
    qr.make(fit=True)
    
    drawer = estilos.get(estilo_modulo, RoundedModuleDrawer())
    
    img_qr = qr.make_image(
        image_factory=StyledPilImage,
        module_drawer=drawer,
        color_mask=SolidFillColorMask(
            back_color=color_fondo,
            front_color=color_frente
        )
    ).convert('RGB')
    
    # Agregar logo
    try:
        logo = Image.open(ruta_logo)
        
        # Calcular tamaño del logo
        qr_width, qr_height = img_qr.size
        logo_size = qr_width // 5
        
        # Redimensionar logo
        logo = logo.resize((logo_size, logo_size), Image.Resampling.LANCZOS)
        
        # Calcular posición central
        logo_pos = ((qr_width - logo_size) // 2, (qr_height - logo_size) // 2)
        
        # Si el logo tiene transparencia, respetarla
        if logo.mode == 'RGBA':
            img_qr.paste(logo, logo_pos, logo)
        else:
            img_qr.paste(logo, logo_pos)
        
        img_qr.save(nombre_archivo)
        print(f"✓ QR estilizado con logo generado: {nombre_archivo}")
    except FileNotFoundError:
        print(f"✗ Error: No se encontró el archivo de logo: {ruta_logo}")
    except Exception as e:
        print(f"✗ Error al procesar el logo: {e}")


def mostrar_estilos_disponibles():
    """Muestra los estilos disponibles"""
    print("\n📐 ESTILOS DE MÓDULOS DISPONIBLES:")
    print("  1. cuadrado       - Cuadrados sólidos (clásico)")
    print("  2. cuadrado_gap   - Cuadrados con espacios")
    print("  3. circulo        - Círculos")
    print("  4. redondeado     - Cuadrados con esquinas redondeadas")
    print("  5. barras_v       - Barras verticales")
    print("  6. barras_h       - Barras horizontales")
    
    print("\n🎨 TIPOS DE GRADIENTE:")
    print("  1. radial         - Del centro hacia afuera")
    print("  2. horizontal     - De izquierda a derecha")
    print("  3. vertical       - De arriba hacia abajo")
    print("  4. cuadrado       - Gradiente cuadrado")


def menu_avanzado():
    """
    Menú interactivo para generar códigos QR con estilos
    """
    print("=" * 60)
    print("       GENERADOR AVANZADO DE CÓDIGOS QR")
    print("=" * 60)
    print("\n1. QR con estilo de módulos personalizado")
    print("2. QR con gradiente de colores")
    print("3. QR con logo y estilo")
    print("4. Ver estilos disponibles")
    print("5. Volver al menú principal")
    
    opcion = input("\nSelecciona una opción (1-5): ")
    
    if opcion == "1":
        datos = input("\nIngresa el texto o URL: ")
        nombre = input("Nombre del archivo (Enter para 'qr_estilo.png'): ") or "qr_estilo.png"
        if not nombre.endswith('.png'):
            nombre += '.png'
        
        print("\nEstilos: cuadrado, cuadrado_gap, circulo, redondeado, barras_v, barras_h")
        estilo = input("Estilo de módulo (Enter para 'redondeado'): ") or "redondeado"
        
        color_frente = input("Color del QR (Enter para 'black'): ") or "black"
        color_fondo = input("Color de fondo (Enter para 'white'): ") or "white"
        
        generar_qr_con_estilo(datos, nombre, estilo, color_frente, color_fondo)
        
    elif opcion == "2":
        datos = input("\nIngresa el texto o URL: ")
        nombre = input("Nombre del archivo (Enter para 'qr_gradiente.png'): ") or "qr_gradiente.png"
        if not nombre.endswith('.png'):
            nombre += '.png'
        
        print("\nTipos: radial, horizontal, vertical, cuadrado")
        tipo_grad = input("Tipo de gradiente (Enter para 'radial'): ") or "radial"
        
        color_centro = input("Color del centro/inicio (Enter para 'blue'): ") or "blue"
        color_borde = input("Color del borde/fin (Enter para 'purple'): ") or "purple"
        color_fondo = input("Color de fondo (Enter para 'white'): ") or "white"
        
        print("\nEstilos: cuadrado, cuadrado_gap, circulo, redondeado, barras_v, barras_h")
        estilo = input("Estilo de módulo (Enter para 'redondeado'): ") or "redondeado"
        
        generar_qr_gradiente(datos, nombre, tipo_grad, color_centro, color_borde, color_fondo, estilo)
        
    elif opcion == "3":
        datos = input("\nIngresa el texto o URL: ")
        ruta_logo = input("Ruta del logo: ")
        nombre = input("Nombre del archivo (Enter para 'qr_logo_estilo.png'): ") or "qr_logo_estilo.png"
        if not nombre.endswith('.png'):
            nombre += '.png'
        
        print("\nEstilos: cuadrado, cuadrado_gap, circulo, redondeado, barras_v, barras_h")
        estilo = input("Estilo de módulo (Enter para 'redondeado'): ") or "redondeado"
        
        color_frente = input("Color del QR (Enter para 'black'): ") or "black"
        color_fondo = input("Color de fondo (Enter para 'white'): ") or "white"
        
        generar_qr_con_logo_y_estilo(datos, ruta_logo, nombre, estilo, color_frente, color_fondo)
        
    elif opcion == "4":
        mostrar_estilos_disponibles()
        
    elif opcion == "5":
        return False
    else:
        print("Opción no válida")
    
    return True


def main():
    """
    Función principal
    """
    # Crear carpeta de salida si no existe
    if not os.path.exists("qr_codes"):
        os.makedirs("qr_codes")
        print("✓ Carpeta 'qr_codes' creada\n")
    
    # Cambiar al directorio de salida
    os.chdir("qr_codes")
    
    # Ejemplos de uso (comentados)
    # generar_qr_con_estilo("https://github.com", "github_redondeado.png", "redondeado", "darkblue", "lightblue")
    # generar_qr_gradiente("Hola Mundo", "hola_gradiente.png", "radial", "red", "orange", "white", "circulo")
    
    # Menú interactivo
    while True:
        continuar = menu_avanzado()
        if not continuar:
            break
        
        otro = input("\n¿Generar otro código QR? (s/n): ")
        if otro.lower() != 's':
            print("\n¡Gracias por usar el generador avanzado de códigos QR!")
            break
        print("\n")


if __name__ == "__main__":
    main()
