"""
Interfaz de Usuario para el Gestor de Tareas Académicas "EstudIA"
Proporciona una interfaz de consola interactiva y amigable
"""

import os
import sys
from datetime import datetime, timedelta
from typing import Optional
from gestor_tareas import GestorTareas


class InterfazUsuario:
    """
    Clase que maneja la interfaz de usuario del gestor de tareas.
    
    Atributos:
        gestor (GestorTareas): Instancia del gestor de tareas
    """
    
    def __init__(self):
        """Inicializa la interfaz de usuario."""
        self.gestor = GestorTareas()
        self.limpiar_pantalla()
    
    def limpiar_pantalla(self) -> None:
        """Limpia la pantalla de la consola."""
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def mostrar_banner(self) -> None:
        """Muestra el banner de la aplicación."""
        print("=" * 60)
        print("🎓 GESTOR DE TAREAS ACADÉMICAS 'ESTUDIA' 🎓")
        print("=" * 60)
        print("Tu compañero para organizar tu vida académica")
        print("=" * 60)
    
    def mostrar_recordatorios(self) -> None:
        """Muestra recordatorios de tareas próximas a vencer."""
        recordatorios = self.gestor.obtener_recordatorios(3)
        
        if recordatorios:
            print("\n🚨 RECORDATORIOS - TAREAS PRÓXIMAS A VENCER:")
            print("-" * 50)
            for tarea in recordatorios:
                dias = tarea.dias_restantes()
                if dias == 0:
                    print(f"⚠️  HOY: {tarea.titulo} - {tarea.materia}")
                elif dias == 1:
                    print(f"⚠️  MAÑANA: {tarea.titulo} - {tarea.materia}")
                else:
                    print(f"⚠️  EN {dias} DÍAS: {tarea.titulo} - {tarea.materia}")
            print("-" * 50)
        else:
            print("\n✅ ¡Excelente! No tienes tareas urgentes en los próximos 3 días.")
    
    def mostrar_estadisticas(self) -> None:
        """Muestra estadísticas de las tareas."""
        stats = self.gestor.obtener_estadisticas()
        
        print("\n📊 ESTADÍSTICAS:")
        print("-" * 30)
        print(f"Total de tareas: {stats['total']}")
        print(f"✅ Completadas: {stats['completadas']}")
        print(f"⏰ Pendientes: {stats['pendientes']}")
        print(f"❌ Vencidas: {stats['vencidas']}")
        print(f"🚨 Urgentes: {stats['urgentes']}")
        
        if stats['pendientes'] > 0:
            print("\n📋 Pendientes por prioridad:")
            for prioridad, cantidad in stats['por_prioridad'].items():
                if cantidad > 0:
                    emoji = "🔴" if prioridad == "Alta" else "🟡" if prioridad == "Media" else "🟢"
                    print(f"  {emoji} {prioridad}: {cantidad}")
    
    def mostrar_menu_principal(self) -> None:
        """Muestra el menú principal de la aplicación."""
        print("\n📋 MENÚ PRINCIPAL:")
        print("-" * 30)
        print("1. 📝 Agregar nueva tarea")
        print("2. 📋 Listar tareas")
        print("3. ✏️  Editar tarea")
        print("4. ✅ Marcar como completada")
        print("5. ⏰ Marcar como pendiente")
        print("6. 🗑️  Eliminar tarea")
        print("7. 🔍 Buscar tarea")
        print("8. 📊 Ver estadísticas")
        print("9. 📤 Exportar tareas")
        print("10. 🚨 Ver recordatorios")
        print("0. 🚪 Salir")
        print("-" * 30)
    
    def obtener_entrada(self, mensaje: str, tipo: type = str) -> any:
        """
        Obtiene entrada del usuario con validación de tipo.
        
        Args:
            mensaje (str): Mensaje a mostrar
            tipo (type): Tipo de dato esperado
            
        Returns:
            any: Valor ingresado por el usuario
        """
        while True:
            try:
                entrada = input(f"{mensaje}: ").strip()
                if not entrada:
                    print("❌ Este campo es obligatorio. Intenta nuevamente.")
                    continue
                
                if tipo == int:
                    return int(entrada)
                elif tipo == float:
                    return float(entrada)
                else:
                    return entrada
                    
            except ValueError:
                print(f"❌ Por favor ingresa un valor válido de tipo {tipo.__name__}")
            except KeyboardInterrupt:
                print("\n\n👋 ¡Hasta luego!")
                sys.exit(0)
    
    def obtener_fecha(self, mensaje: str) -> datetime:
        """
        Obtiene una fecha del usuario.
        
        Args:
            mensaje (str): Mensaje a mostrar
            
        Returns:
            datetime: Fecha ingresada por el usuario
        """
        while True:
            try:
                fecha_str = self.obtener_entrada(f"{mensaje} (DD/MM/YYYY)")
                
                # Intentar diferentes formatos
                formatos = ["%d/%m/%Y", "%d-%m-%Y", "%d.%m.%Y"]
                for formato in formatos:
                    try:
                        fecha = datetime.strptime(fecha_str, formato)
                        # Verificar que la fecha no sea en el pasado
                        if fecha.date() < datetime.now().date():
                            print("❌ La fecha no puede ser en el pasado.")
                            continue
                        return fecha
                    except ValueError:
                        continue
                
                print("❌ Formato de fecha inválido. Usa DD/MM/YYYY")
                
            except Exception as e:
                print(f"❌ Error al procesar la fecha: {e}")
    
    def obtener_prioridad(self) -> str:
        """
        Obtiene la prioridad de una tarea.
        
        Returns:
            str: Prioridad seleccionada
        """
        print("\n📊 Prioridad:")
        print("1. 🔴 Alta")
        print("2. 🟡 Media")
        print("3. 🟢 Baja")
        
        while True:
            opcion = self.obtener_entrada("Selecciona una opción (1-3)", int)
            if opcion == 1:
                return "Alta"
            elif opcion == 2:
                return "Media"
            elif opcion == 3:
                return "Baja"
            else:
                print("❌ Opción inválida. Selecciona 1, 2 o 3.")
    
    def agregar_tarea(self) -> None:
        """Permite al usuario agregar una nueva tarea."""
        print("\n📝 AGREGAR NUEVA TAREA")
        print("-" * 30)
        
        titulo = self.obtener_entrada("Título de la tarea")
        materia = self.obtener_entrada("Materia/Curso")
        fecha_limite = self.obtener_fecha("Fecha límite")
        prioridad = self.obtener_prioridad()
        
        descripcion = input("Descripción (opcional): ").strip()
        if not descripcion:
            descripcion = None
        
        self.gestor.agregar_tarea(titulo, materia, fecha_limite, prioridad, descripcion)
        input("\nPresiona Enter para continuar...")
    
    def listar_tareas(self) -> None:
        """Permite al usuario listar tareas con diferentes filtros."""
        print("\n📋 LISTAR TAREAS")
        print("-" * 30)
        print("1. Todas las tareas")
        print("2. Tareas pendientes")
        print("3. Tareas completadas")
        print("4. Tareas vencidas")
        print("5. Tareas por materia")
        print("6. Tareas por prioridad")
        print("7. Tareas próximas a vencer")
        
        opcion = self.obtener_entrada("Selecciona una opción (1-7)", int)
        
        tareas = []
        
        if opcion == 1:
            tareas = self.gestor.listar_tareas()
        elif opcion == 2:
            tareas = self.gestor.listar_tareas("pendientes")
        elif opcion == 3:
            tareas = self.gestor.listar_tareas("completadas")
        elif opcion == 4:
            tareas = self.gestor.listar_tareas("vencidas")
        elif opcion == 5:
            materia = self.obtener_entrada("Nombre de la materia")
            tareas = self.gestor.listar_tareas("materia", materia)
        elif opcion == 6:
            prioridad = self.obtener_prioridad()
            tareas = self.gestor.listar_tareas("prioridad", prioridad)
        elif opcion == 7:
            dias = self.obtener_entrada("Número de días", int)
            tareas = self.gestor.listar_tareas("proximas", str(dias))
        else:
            print("❌ Opción inválida.")
            return
        
        self.mostrar_tareas(tareas)
        input("\nPresiona Enter para continuar...")
    
    def mostrar_tareas(self, tareas: list) -> None:
        """
        Muestra una lista de tareas formateada.
        
        Args:
            tareas (list): Lista de tareas a mostrar
        """
        if not tareas:
            print("\n📭 No se encontraron tareas.")
            return
        
        print(f"\n📋 TAREAS ENCONTRADAS ({len(tareas)}):")
        print("=" * 80)
        
        for i, tarea in enumerate(tareas, 1):
            print(f"\n{i}. {tarea}")
            print("-" * 80)
    
    def editar_tarea(self) -> None:
        """Permite al usuario editar una tarea existente."""
        print("\n✏️ EDITAR TAREA")
        print("-" * 30)
        
        titulo = self.obtener_entrada("Título de la tarea a editar")
        tarea = self.gestor.buscar_tarea(titulo)
        
        if not tarea:
            print(f"❌ No se encontró la tarea '{titulo}'")
            input("\nPresiona Enter para continuar...")
            return
        
        print(f"\n📝 Editando: {tarea.titulo}")
        print("Deja en blanco los campos que no quieras cambiar.")
        
        nuevo_titulo = input(f"Nuevo título [{tarea.titulo}]: ").strip()
        nueva_materia = input(f"Nueva materia [{tarea.materia}]: ").strip()
        
        nueva_fecha_str = input(f"Nueva fecha límite [{tarea.fecha_limite.strftime('%d/%m/%Y')}]: ").strip()
        nueva_fecha = None
        if nueva_fecha_str:
            nueva_fecha = self.obtener_fecha("Nueva fecha límite")
        
        print("\nNueva prioridad:")
        nueva_prioridad = self.obtener_prioridad()
        
        nueva_descripcion = input(f"Nueva descripción [{tarea.descripcion}]: ").strip()
        
        # Preparar cambios
        cambios = {}
        if nuevo_titulo:
            cambios["titulo"] = nuevo_titulo
        if nueva_materia:
            cambios["materia"] = nueva_materia
        if nueva_fecha:
            cambios["fecha_limite"] = nueva_fecha
        if nueva_prioridad:
            cambios["prioridad"] = nueva_prioridad
        if nueva_descripcion:
            cambios["descripcion"] = nueva_descripcion
        
        self.gestor.editar_tarea(titulo, **cambios)
        input("\nPresiona Enter para continuar...")
    
    def marcar_completada(self) -> None:
        """Permite al usuario marcar una tarea como completada."""
        print("\n✅ MARCAR COMO COMPLETADA")
        print("-" * 30)
        
        titulo = self.obtener_entrada("Título de la tarea")
        self.gestor.marcar_completada(titulo)
        input("\nPresiona Enter para continuar...")
    
    def marcar_pendiente(self) -> None:
        """Permite al usuario marcar una tarea como pendiente."""
        print("\n⏰ MARCAR COMO PENDIENTE")
        print("-" * 30)
        
        titulo = self.obtener_entrada("Título de la tarea")
        self.gestor.marcar_pendiente(titulo)
        input("\nPresiona Enter para continuar...")
    
    def eliminar_tarea(self) -> None:
        """Permite al usuario eliminar una tarea."""
        print("\n🗑️ ELIMINAR TAREA")
        print("-" * 30)
        
        titulo = self.obtener_entrada("Título de la tarea a eliminar")
        
        # Mostrar la tarea antes de eliminar
        tarea = self.gestor.buscar_tarea(titulo)
        if tarea:
            print(f"\n📋 Tarea encontrada:")
            print(tarea)
            
            confirmar = input("\n¿Estás seguro de que quieres eliminar esta tarea? (s/n): ").lower()
            if confirmar in ['s', 'si', 'sí', 'y', 'yes']:
                self.gestor.eliminar_tarea(titulo)
            else:
                print("❌ Eliminación cancelada.")
        else:
            print(f"❌ No se encontró la tarea '{titulo}'")
        
        input("\nPresiona Enter para continuar...")
    
    def buscar_tarea(self) -> None:
        """Permite al usuario buscar una tarea específica."""
        print("\n🔍 BUSCAR TAREA")
        print("-" * 30)
        
        titulo = self.obtener_entrada("Título de la tarea a buscar")
        tarea = self.gestor.buscar_tarea(titulo)
        
        if tarea:
            print(f"\n📋 Tarea encontrada:")
            print("=" * 50)
            print(tarea)
            print("=" * 50)
        else:
            print(f"❌ No se encontró la tarea '{titulo}'")
        
        input("\nPresiona Enter para continuar...")
    
    def exportar_tareas(self) -> None:
        """Permite al usuario exportar las tareas a un archivo."""
        print("\n📤 EXPORTAR TAREAS")
        print("-" * 30)
        
        nombre_archivo = self.obtener_entrada("Nombre del archivo (sin extensión)")
        archivo_completo = f"{nombre_archivo}.txt"
        
        if self.gestor.exportar_tareas(archivo_completo):
            print(f"✅ Las tareas se han exportado a '{archivo_completo}'")
        else:
            print("❌ Error al exportar las tareas.")
        
        input("\nPresiona Enter para continuar...")
    
    def ejecutar(self) -> None:
        """Ejecuta la aplicación principal."""
        while True:
            self.limpiar_pantalla()
            self.mostrar_banner()
            self.mostrar_recordatorios()
            self.mostrar_estadisticas()
            self.mostrar_menu_principal()
            
            try:
                opcion = self.obtener_entrada("Selecciona una opción (0-10)", int)
                
                if opcion == 0:
                    print("\n👋 ¡Gracias por usar EstudIA! ¡Que tengas un excelente día académico!")
                    break
                elif opcion == 1:
                    self.agregar_tarea()
                elif opcion == 2:
                    self.listar_tareas()
                elif opcion == 3:
                    self.editar_tarea()
                elif opcion == 4:
                    self.marcar_completada()
                elif opcion == 5:
                    self.marcar_pendiente()
                elif opcion == 6:
                    self.eliminar_tarea()
                elif opcion == 7:
                    self.buscar_tarea()
                elif opcion == 8:
                    self.mostrar_estadisticas()
                    input("\nPresiona Enter para continuar...")
                elif opcion == 9:
                    self.exportar_tareas()
                elif opcion == 10:
                    self.mostrar_recordatorios()
                    input("\nPresiona Enter para continuar...")
                else:
                    print("❌ Opción inválida. Por favor selecciona una opción del 0 al 10.")
                    input("\nPresiona Enter para continuar...")
                    
            except KeyboardInterrupt:
                print("\n\n👋 ¡Hasta luego!")
                break
            except Exception as e:
                print(f"❌ Error inesperado: {e}")
                input("\nPresiona Enter para continuar...")


if __name__ == "__main__":
    app = InterfazUsuario()
    app.ejecutar()
