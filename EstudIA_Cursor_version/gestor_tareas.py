"""
Clase GestorTareas para el Gestor de Tareas Académicas "EstudIA"
Maneja todas las operaciones CRUD y la persistencia de datos
"""

import json
import os
from datetime import datetime, timedelta
from typing import List, Optional, Dict, Any
from tarea import Tarea


class GestorTareas:
    """
    Clase que gestiona las tareas académicas.
    
    Atributos:
        tareas (List[Tarea]): Lista de tareas
        archivo_datos (str): Ruta del archivo JSON para persistencia
    """
    
    def __init__(self, archivo_datos: str = "tareas_estudia.json"):
        """
        Inicializa el gestor de tareas.
        
        Args:
            archivo_datos (str): Ruta del archivo JSON para guardar datos
        """
        self.tareas: List[Tarea] = []
        self.archivo_datos = archivo_datos
        self.cargar_tareas()
    
    def agregar_tarea(self, titulo: str, materia: str, fecha_limite: datetime, 
                     prioridad: str, descripcion: Optional[str] = None) -> bool:
        """
        Agrega una nueva tarea al gestor.
        
        Args:
            titulo (str): Título de la tarea
            materia (str): Materia o curso
            fecha_limite (datetime): Fecha límite de entrega
            prioridad (str): Prioridad (Alta/Media/Baja)
            descripcion (str, opcional): Descripción adicional
            
        Returns:
            bool: True si se agregó correctamente, False en caso contrario
        """
        try:
            # Validar prioridad
            if prioridad not in ["Alta", "Media", "Baja"]:
                print("❌ Error: La prioridad debe ser 'Alta', 'Media' o 'Baja'")
                return False
            
            # Crear nueva tarea
            nueva_tarea = Tarea(titulo, materia, fecha_limite, prioridad, descripcion)
            self.tareas.append(nueva_tarea)
            
            # Guardar cambios
            self.guardar_tareas()
            print(f"✅ Tarea '{titulo}' agregada exitosamente")
            return True
            
        except Exception as e:
            print(f"❌ Error al agregar tarea: {e}")
            return False
    
    def listar_tareas(self, filtro: Optional[str] = None, 
                     valor_filtro: Optional[str] = None) -> List[Tarea]:
        """
        Lista las tareas según el filtro especificado.
        
        Args:
            filtro (str, opcional): Tipo de filtro ('materia', 'prioridad', 'proximas', 'completadas', 'vencidas')
            valor_filtro (str, opcional): Valor del filtro
            
        Returns:
            List[Tarea]: Lista de tareas filtradas
        """
        tareas_filtradas = self.tareas.copy()
        
        if filtro == "materia" and valor_filtro:
            tareas_filtradas = [t for t in tareas_filtradas 
                              if t.materia.lower() == valor_filtro.lower()]
        
        elif filtro == "prioridad" and valor_filtro:
            tareas_filtradas = [t for t in tareas_filtradas 
                              if t.prioridad == valor_filtro]
        
        elif filtro == "proximas":
            dias = int(valor_filtro) if valor_filtro else 7
            tareas_filtradas = [t for t in tareas_filtradas 
                              if t.es_urgente(dias) and not t.completada]
        
        elif filtro == "completadas":
            tareas_filtradas = [t for t in tareas_filtradas if t.completada]
        
        elif filtro == "vencidas":
            tareas_filtradas = [t for t in tareas_filtradas if t.esta_vencida()]
        
        elif filtro == "pendientes":
            tareas_filtradas = [t for t in tareas_filtradas if not t.completada]
        
        # Ordenar por prioridad (Alta primero) y luego por fecha
        tareas_filtradas.sort(key=lambda t: (-t.obtener_prioridad_numerica(), t.fecha_limite))
        
        return tareas_filtradas
    
    def buscar_tarea(self, titulo: str) -> Optional[Tarea]:
        """
        Busca una tarea por título.
        
        Args:
            titulo (str): Título de la tarea a buscar
            
        Returns:
            Tarea o None: La tarea encontrada o None si no existe
        """
        for tarea in self.tareas:
            if tarea.titulo.lower() == titulo.lower():
                return tarea
        return None
    
    def editar_tarea(self, titulo: str, **kwargs) -> bool:
        """
        Edita una tarea existente.
        
        Args:
            titulo (str): Título de la tarea a editar
            **kwargs: Campos a actualizar (titulo, materia, fecha_limite, prioridad, descripcion)
            
        Returns:
            bool: True si se editó correctamente, False en caso contrario
        """
        tarea = self.buscar_tarea(titulo)
        if not tarea:
            print(f"❌ No se encontró la tarea '{titulo}'")
            return False
        
        try:
            # Actualizar campos si se proporcionan
            if "titulo" in kwargs:
                tarea.titulo = kwargs["titulo"]
            if "materia" in kwargs:
                tarea.materia = kwargs["materia"]
            if "fecha_limite" in kwargs:
                tarea.fecha_limite = kwargs["fecha_limite"]
            if "prioridad" in kwargs:
                if kwargs["prioridad"] not in ["Alta", "Media", "Baja"]:
                    print("❌ Error: La prioridad debe ser 'Alta', 'Media' o 'Baja'")
                    return False
                tarea.prioridad = kwargs["prioridad"]
            if "descripcion" in kwargs:
                tarea.descripcion = kwargs["descripcion"]
            
            # Guardar cambios
            self.guardar_tareas()
            print(f"✅ Tarea '{titulo}' editada exitosamente")
            return True
            
        except Exception as e:
            print(f"❌ Error al editar tarea: {e}")
            return False
    
    def marcar_completada(self, titulo: str) -> bool:
        """
        Marca una tarea como completada.
        
        Args:
            titulo (str): Título de la tarea
            
        Returns:
            bool: True si se marcó correctamente, False en caso contrario
        """
        tarea = self.buscar_tarea(titulo)
        if not tarea:
            print(f"❌ No se encontró la tarea '{titulo}'")
            return False
        
        tarea.marcar_completada()
        self.guardar_tareas()
        print(f"✅ Tarea '{titulo}' marcada como completada")
        return True
    
    def marcar_pendiente(self, titulo: str) -> bool:
        """
        Marca una tarea como pendiente.
        
        Args:
            titulo (str): Título de la tarea
            
        Returns:
            bool: True si se marcó correctamente, False en caso contrario
        """
        tarea = self.buscar_tarea(titulo)
        if not tarea:
            print(f"❌ No se encontró la tarea '{titulo}'")
            return False
        
        tarea.marcar_pendiente()
        self.guardar_tareas()
        print(f"✅ Tarea '{titulo}' marcada como pendiente")
        return True
    
    def eliminar_tarea(self, titulo: str) -> bool:
        """
        Elimina una tarea del gestor.
        
        Args:
            titulo (str): Título de la tarea a eliminar
            
        Returns:
            bool: True si se eliminó correctamente, False en caso contrario
        """
        tarea = self.buscar_tarea(titulo)
        if not tarea:
            print(f"❌ No se encontró la tarea '{titulo}'")
            return False
        
        self.tareas.remove(tarea)
        self.guardar_tareas()
        print(f"✅ Tarea '{titulo}' eliminada exitosamente")
        return True
    
    def obtener_recordatorios(self, dias: int = 3) -> List[Tarea]:
        """
        Obtiene tareas que vencen en los próximos N días.
        
        Args:
            dias (int): Número de días para considerar en recordatorios
            
        Returns:
            List[Tarea]: Lista de tareas próximas a vencer
        """
        return [t for t in self.tareas if t.es_urgente(dias)]
    
    def obtener_estadisticas(self) -> Dict[str, Any]:
        """
        Obtiene estadísticas de las tareas.
        
        Returns:
            Dict[str, Any]: Diccionario con estadísticas
        """
        total = len(self.tareas)
        completadas = len([t for t in self.tareas if t.completada])
        pendientes = total - completadas
        vencidas = len([t for t in self.tareas if t.esta_vencida()])
        urgentes = len(self.obtener_recordatorios())
        
        # Estadísticas por prioridad
        por_prioridad = {"Alta": 0, "Media": 0, "Baja": 0}
        for tarea in self.tareas:
            if not tarea.completada:
                por_prioridad[tarea.prioridad] += 1
        
        return {
            "total": total,
            "completadas": completadas,
            "pendientes": pendientes,
            "vencidas": vencidas,
            "urgentes": urgentes,
            "por_prioridad": por_prioridad
        }
    
    def cargar_tareas(self) -> None:
        """
        Carga las tareas desde el archivo JSON.
        """
        try:
            if os.path.exists(self.archivo_datos):
                with open(self.archivo_datos, 'r', encoding='utf-8') as archivo:
                    datos = json.load(archivo)
                    self.tareas = [Tarea.from_dict(tarea_data) for tarea_data in datos]
                print(f"📁 Se cargaron {len(self.tareas)} tareas desde {self.archivo_datos}")
            else:
                print("📁 No se encontró archivo de datos. Iniciando con lista vacía.")
        except Exception as e:
            print(f"❌ Error al cargar tareas: {e}")
            self.tareas = []
    
    def guardar_tareas(self) -> None:
        """
        Guarda las tareas en el archivo JSON.
        """
        try:
            datos = [tarea.to_dict() for tarea in self.tareas]
            with open(self.archivo_datos, 'w', encoding='utf-8') as archivo:
                json.dump(datos, archivo, indent=2, ensure_ascii=False)
        except Exception as e:
            print(f"❌ Error al guardar tareas: {e}")
    
    def exportar_tareas(self, archivo_salida: str) -> bool:
        """
        Exporta las tareas a un archivo de texto.
        
        Args:
            archivo_salida (str): Ruta del archivo de salida
            
        Returns:
            bool: True si se exportó correctamente, False en caso contrario
        """
        try:
            with open(archivo_salida, 'w', encoding='utf-8') as archivo:
                archivo.write("=== GESTOR DE TAREAS ACADÉMICAS ESTUDIA ===\n")
                archivo.write(f"Fecha de exportación: {datetime.now().strftime('%d/%m/%Y %H:%M')}\n\n")
                
                # Estadísticas
                stats = self.obtener_estadisticas()
                archivo.write("ESTADÍSTICAS:\n")
                archivo.write(f"Total de tareas: {stats['total']}\n")
                archivo.write(f"Completadas: {stats['completadas']}\n")
                archivo.write(f"Pendientes: {stats['pendientes']}\n")
                archivo.write(f"Vencidas: {stats['vencidas']}\n")
                archivo.write(f"Urgentes (próximos 3 días): {stats['urgentes']}\n\n")
                
                # Tareas por prioridad
                archivo.write("TAREAS PENDIENTES POR PRIORIDAD:\n")
                for prioridad in ["Alta", "Media", "Baja"]:
                    tareas_prioridad = [t for t in self.tareas 
                                      if t.prioridad == prioridad and not t.completada]
                    if tareas_prioridad:
                        archivo.write(f"\n{prioridad}:\n")
                        for tarea in tareas_prioridad:
                            archivo.write(f"  - {tarea.titulo} ({tarea.materia}) - {tarea.fecha_limite.strftime('%d/%m/%Y')}\n")
                
                # Tareas completadas
                tareas_completadas = [t for t in self.tareas if t.completada]
                if tareas_completadas:
                    archivo.write(f"\nTAREAS COMPLETADAS ({len(tareas_completadas)}):\n")
                    for tarea in tareas_completadas:
                        archivo.write(f"  ✓ {tarea.titulo} ({tarea.materia})\n")
            
            print(f"✅ Tareas exportadas a {archivo_salida}")
            return True
            
        except Exception as e:
            print(f"❌ Error al exportar tareas: {e}")
            return False
