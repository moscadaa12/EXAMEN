"""
Gestor de Tareas Académicas "EstudIA"
Aplicación principal para gestionar tareas académicas de estudiantes universitarios

Autor: EstudIA Team
Versión: 1.0
Fecha: 2025
"""

import sys
import os
from interfaz_usuario import InterfazUsuario


def verificar_requisitos():
    """
    Verifica que se cumplan los requisitos mínimos para ejecutar la aplicación.
    """
    try:
        # Verificar versión de Python
        if sys.version_info < (3, 6):
            print("❌ Error: Se requiere Python 3.6 o superior")
            print(f"   Versión actual: {sys.version}")
            return False
        
        # Verificar que los módulos necesarios estén disponibles
        import json
        import datetime
        from typing import List, Optional, Dict, Any
        
        print("✅ Requisitos del sistema verificados correctamente")
        return True
        
    except ImportError as e:
        print(f"❌ Error: Módulo requerido no encontrado: {e}")
        return False


def mostrar_informacion_aplicacion():
    """
    Muestra información sobre la aplicación.
    """
    print("=" * 70)
    print("🎓 GESTOR DE TAREAS ACADÉMICAS 'ESTUDIA' 🎓")
    print("=" * 70)
    print("📚 Versión: 1.0")
    print("👥 Desarrollado para estudiantes universitarios")
    print("🎯 Objetivo: Organizar y gestionar tareas académicas de manera eficiente")
    print("=" * 70)
    print()
    print("🔧 CARACTERÍSTICAS PRINCIPALES:")
    print("  • Registro de tareas con título, materia, fecha límite y prioridad")
    print("  • Sistema de recordatorios para tareas próximas a vencer")
    print("  • Filtros avanzados (por materia, prioridad, estado)")
    print("  • Estadísticas y reportes de progreso")
    print("  • Persistencia de datos en archivos JSON locales")
    print("  • Interfaz de usuario intuitiva y amigable")
    print()
    print("📋 REQUERIMIENTOS FUNCIONALES IMPLEMENTADOS:")
    print("  ✅ Registrar tareas con todos los campos requeridos")
    print("  ✅ Listar tareas con múltiples filtros")
    print("  ✅ Marcar tareas como completadas/pendientes")
    print("  ✅ Editar y eliminar tareas")
    print("  ✅ Recordatorios de tareas próximas a vencer")
    print("  ✅ Persistencia ligera con archivos JSON")
    print()
    print("🏗️ CONCEPTOS DE PROGRAMACIÓN IMPLEMENTADOS:")
    print("  ✅ Estructuras secuenciales")
    print("  ✅ Estructuras repetitivas (bucles)")
    print("  ✅ Modularidad (separación en clases y módulos)")
    print("  ✅ Programación Orientada a Objetos (POO)")
    print("  ✅ Sin uso de base de datos (solo archivos locales)")
    print("=" * 70)


def main():
    """
    Función principal de la aplicación.
    """
    try:
        # Verificar requisitos del sistema
        if not verificar_requisitos():
            input("\nPresiona Enter para salir...")
            return
        
        # Mostrar información de la aplicación
        mostrar_informacion_aplicacion()
        
        # Confirmar inicio de la aplicación
        print("\n🚀 ¿Deseas iniciar la aplicación? (s/n): ", end="")
        respuesta = input().lower().strip()
        
        if respuesta not in ['s', 'si', 'sí', 'y', 'yes']:
            print("\n👋 ¡Hasta luego! Gracias por tu interés en EstudIA.")
            return
        
        # Inicializar y ejecutar la aplicación
        print("\n🔄 Iniciando EstudIA...")
        print("📁 Cargando datos de tareas...")
        
        app = InterfazUsuario()
        app.ejecutar()
        
    except KeyboardInterrupt:
        print("\n\n👋 ¡Aplicación interrumpida por el usuario!")
        print("   Gracias por usar EstudIA. ¡Hasta pronto!")
        
    except Exception as e:
        print(f"\n❌ Error inesperado en la aplicación: {e}")
        print("   Por favor, reporta este error para mejorar la aplicación.")
        input("\nPresiona Enter para salir...")
    
    finally:
        print("\n🎓 ¡Gracias por usar EstudIA!")
        print("   ¡Que tengas un excelente rendimiento académico!")


if __name__ == "__main__":
    main()
