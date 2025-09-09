from datetime import datetime

DATE_FORMAT = "%d/%m/%Y"

class Tarea:
    def __init__(self, id, titulo, materia, fecha_limite, prioridad, descripcion="", completada=False):
        self.id = id
        self.titulo = titulo
        self.materia = materia
        self.fecha_limite = fecha_limite
        self.prioridad = prioridad
        self.descripcion = descripcion
        self.completada = completada

    def dias_restantes(self):
        try:
            fecha = datetime.strptime(self.fecha_limite, DATE_FORMAT)
            return (fecha - datetime.now()).days
        except Exception:
            return None

    def to_dict(self):
        return self.__dict__

    @staticmethod
    def from_dict(data):
        return Tarea(**data)