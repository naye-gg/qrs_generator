#!/usr/bin/env python3
"""
Generador de Códigos QR
Este script permite generar códigos QR a partir de texto o URLs
"""

import qrcode
from PIL import Image
import os


def generar_qr_simple(datos, nombre_archivo="qr_code.png"):
    """
    Genera un código QR básico
    
    Args:
        datos (str): Texto o URL para codificar en el QR
        nombre_archivo (str): Nombre del archivo de salida
    """
    qr = qrcode.QRCode(
        version=1,  # Tamaño del QR (1-40)
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    
    qr.add_data(datos)
    qr.make(fit=True)
    
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(nombre_archivo)
    print(f"✓ Código QR generado: {nombre_archivo}")


def generar_qr_personalizado(datos, nombre_archivo="qr_personalizado.png", 
                             color_fondo="white", color_frente="black",
                             tamaño_caja=10, borde=4):
    """
    Genera un código QR personalizado con colores y tamaños específicos
    
    Args:
        datos (str): Texto o URL para codificar
        nombre_archivo (str): Nombre del archivo de salida
        color_fondo (str): Color de fondo
        color_frente (str): Color del código QR
        tamaño_caja (int): Tamaño de cada caja del QR
        borde (int): Tamaño del borde
    """
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,  # Mayor corrección de errores
        box_size=tamaño_caja,
        border=borde,
    )
    
    qr.add_data(datos)
    qr.make(fit=True)
    
    img = qr.make_image(fill_color=color_frente, back_color=color_fondo)
    img.save(nombre_archivo)
    print(f"✓ Código QR personalizado generado: {nombre_archivo}")


def generar_qr_con_logo(datos, ruta_logo, nombre_archivo="qr_con_logo.png"):
    """
    Genera un código QR con un logo en el centro
    
    Args:
        datos (str): Texto o URL para codificar
        ruta_logo (str): Ruta de la imagen del logo
        nombre_archivo (str): Nombre del archivo de salida
    """
    # Crear el QR con alta corrección de errores (necesaria para logo)
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )
    
    qr.add_data(datos)
    qr.make(fit=True)
    
    img_qr = qr.make_image(fill_color="black", back_color="white").convert('RGB')
    
    # Abrir y redimensionar el logo
    try:
        logo = Image.open(ruta_logo)
        
        # Calcular tamaño del logo (aproximadamente 1/5 del QR)
        qr_width, qr_height = img_qr.size
        logo_size = qr_width // 5
        
        logo = logo.resize((logo_size, logo_size), Image.Resampling.LANCZOS)
        
        # Calcular posición para centrar el logo
        logo_pos = ((qr_width - logo_size) // 2, (qr_height - logo_size) // 2)
        
        # Pegar el logo en el QR
        img_qr.paste(logo, logo_pos)
        
        img_qr.save(nombre_archivo)
        print(f"✓ Código QR con logo generado: {nombre_archivo}")
    except FileNotFoundError:
        print(f"✗ Error: No se encontró el archivo de logo: {ruta_logo}")
    except Exception as e:
        print(f"✗ Error al procesar el logo: {e}")


def menu_interactivo():
    """
    Menú interactivo para generar códigos QR
    """
    print("=" * 50)
    print("       GENERADOR DE CÓDIGOS QR")
    print("=" * 50)
    print("\n1. Generar QR simple")
    print("2. Generar QR personalizado (colores)")
    print("3. Generar QR con logo")
    print("4. QR Avanzado (estilos y gradientes) 🎨")
    print("5. Salir")
    
    opcion = input("\nSelecciona una opción (1-5): ")
    
    if opcion == "1":
        datos = input("Ingresa el texto o URL: ")
        nombre = input("Nombre del archivo (Enter para 'qr_code.png'): ") or "qr_code.png"
        if not nombre.endswith('.png'):
            nombre += '.png'
        generar_qr_simple(datos, nombre)
        
    elif opcion == "2":
        datos = input("Ingresa el texto o URL: ")
        nombre = input("Nombre del archivo (Enter para 'qr_personalizado.png'): ") or "qr_personalizado.png"
        if not nombre.endswith('.png'):
            nombre += '.png'
        color_frente = input("Color del QR (Enter para 'black'): ") or "black"
        color_fondo = input("Color de fondo (Enter para 'white'): ") or "white"
        generar_qr_personalizado(datos, nombre, color_fondo, color_frente)
        
    elif opcion == "3":
        datos = input("Ingresa el texto o URL: ")
        ruta_logo = input("Ruta del logo: ")
        nombre = input("Nombre del archivo (Enter para 'qr_con_logo.png'): ") or "qr_con_logo.png"
        if not nombre.endswith('.png'):
            nombre += '.png'
        generar_qr_con_logo(datos, ruta_logo, nombre)
        
    elif opcion == "4":
        # Importar y ejecutar el módulo avanzado
        try:
            import qr_generator_advanced
            qr_generator_advanced.menu_avanzado()
        except ImportError:
            print("✗ Error: El módulo avanzado no está disponible")
        except Exception as e:
            print(f"✗ Error: {e}")
        
    elif opcion == "5":
        print("¡Hasta pronto!")
        return
    else:
        print("Opción no válida")


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
    
    # Ejemplos rápidos (comentados por defecto)
    # generar_qr_simple("https://github.com", "github_qr.png")
    # generar_qr_personalizado("Hola Mundo", "hola_qr.png", "lightblue", "darkblue")
    
    # Menú interactivo
    while True:
        menu_interactivo()
        continuar = input("\n¿Generar otro código QR? (s/n): ")
        if continuar.lower() != 's':
            print("\n¡Gracias por usar el generador de códigos QR!")
            break
        print("\n")


if __name__ == "__main__":
    main()
