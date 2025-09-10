"""
Clase Tarea para el Gestor de Tareas Académicas "EstudIA"
Representa una tarea académica con sus atributos y métodos básicos
"""

from datetime import datetime
from typing import Optional


class Tarea:
    """
    Clase que representa una tarea académica.
    
    Atributos:
        titulo (str): Título de la tarea
        materia (str): Materia o curso al que pertenece
        fecha_limite (datetime): Fecha límite de entrega
        prioridad (str): Prioridad de la tarea (Alta/Media/Baja)
        descripcion (str, opcional): Descripción adicional de la tarea
        completada (bool): Estado de completado de la tarea
        fecha_creacion (datetime): Fecha de creación de la tarea
    """
    
    def __init__(self, titulo: str, materia: str, fecha_limite: datetime, 
                 prioridad: str, descripcion: Optional[str] = None):
        """
        Inicializa una nueva tarea.
        
        Args:
            titulo (str): Título de la tarea
            materia (str): Materia o curso
            fecha_limite (datetime): Fecha límite de entrega
            prioridad (str): Prioridad (Alta/Media/Baja)
            descripcion (str, opcional): Descripción adicional
        """
        self.titulo = titulo
        self.materia = materia
        self.fecha_limite = fecha_limite
        self.prioridad = prioridad
        self.descripcion = descripcion or ""
        self.completada = False
        self.fecha_creacion = datetime.now()
    
    def marcar_completada(self) -> None:
        """Marca la tarea como completada."""
        self.completada = True
    
    def marcar_pendiente(self) -> None:
        """Marca la tarea como pendiente."""
        self.completada = False
    
    def esta_vencida(self) -> bool:
        """
        Verifica si la tarea está vencida.
        
        Returns:
            bool: True si la tarea está vencida, False en caso contrario
        """
        return datetime.now() > self.fecha_limite and not self.completada
    
    def dias_restantes(self) -> int:
        """
        Calcula los días restantes para la entrega.
        
        Returns:
            int: Número de días restantes (negativo si está vencida)
        """
        diferencia = self.fecha_limite.date() - datetime.now().date()
        return diferencia.days
    
    def es_urgente(self, dias_limite: int = 3) -> bool:
        """
        Verifica si la tarea es urgente (vence en los próximos N días).
        
        Args:
            dias_limite (int): Número de días para considerar urgente
            
        Returns:
            bool: True si es urgente, False en caso contrario
        """
        return 0 <= self.dias_restantes() <= dias_limite and not self.completada
    
    def obtener_prioridad_numerica(self) -> int:
        """
        Convierte la prioridad a un valor numérico para ordenamiento.
        
        Returns:
            int: 3 para Alta, 2 para Media, 1 para Baja
        """
        prioridades = {"Alta": 3, "Media": 2, "Baja": 1}
        return prioridades.get(self.prioridad, 1)
    
    def to_dict(self) -> dict:
        """
        Convierte la tarea a un diccionario para serialización.
        
        Returns:
            dict: Diccionario con los datos de la tarea
        """
        return {
            "titulo": self.titulo,
            "materia": self.materia,
            "fecha_limite": self.fecha_limite.isoformat(),
            "prioridad": self.prioridad,
            "descripcion": self.descripcion,
            "completada": self.completada,
            "fecha_creacion": self.fecha_creacion.isoformat()
        }
    
    @classmethod
    def from_dict(cls, data: dict) -> 'Tarea':
        """
        Crea una tarea desde un diccionario.
        
        Args:
            data (dict): Diccionario con los datos de la tarea
            
        Returns:
            Tarea: Nueva instancia de Tarea
        """
        tarea = cls(
            titulo=data["titulo"],
            materia=data["materia"],
            fecha_limite=datetime.fromisoformat(data["fecha_limite"]),
            prioridad=data["prioridad"],
            descripcion=data.get("descripcion", "")
        )
        tarea.completada = data.get("completada", False)
        tarea.fecha_creacion = datetime.fromisoformat(data.get("fecha_creacion", datetime.now().isoformat()))
        return tarea
    
    def __str__(self) -> str:
        """
        Representación en cadena de la tarea.
        
        Returns:
            str: Cadena formateada con la información de la tarea
        """
        estado = "✓ Completada" if self.completada else "⏰ Pendiente"
        dias = self.dias_restantes()
        
        if dias < 0:
            tiempo = f"Vencida hace {abs(dias)} días"
        elif dias == 0:
            tiempo = "Vence hoy"
        elif dias == 1:
            tiempo = "Vence mañana"
        else:
            tiempo = f"Vence en {dias} días"
        
        return f"[{self.prioridad}] {self.titulo} - {self.materia}\n" \
               f"  {tiempo} | {estado}\n" \
               f"  {self.descripcion}" if self.descripcion else f"[{self.prioridad}] {self.titulo} - {self.materia}\n" \
               f"  {tiempo} | {estado}"
    
    def __repr__(self) -> str:
        """Representación para debugging."""
        return f"Tarea(titulo='{self.titulo}', materia='{self.materia}', prioridad='{self.prioridad}')"
