import json
import os
from tarea import Tarea

ARCHIVO = "tareas.json"

def cargar_tareas():
    if not os.path.exists(ARCHIVO):
        return []
    with open(ARCHIVO, "r", encoding="utf-8") as f:
        data = json.load(f)
        return [Tarea.from_dict(t) for t in data]

def guardar_tareas(tareas):
    with open(ARCHIVO, "w", encoding="utf-8") as f:
        json.dump([t.to_dict() for t in tareas], f, ensure_ascii=False, indent=2)

def siguiente_id(tareas):
    return max([t.id for t in tareas], default=0) + 1