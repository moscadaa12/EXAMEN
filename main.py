# main.py
from tarea import Tarea, DATE_FORMAT
from storage import cargar_tareas, guardar_tareas, siguiente_id
from datetime import datetime
import os

RANGO_RECORDATORIO_DIAS = 2  # mostrar tareas que vencen en X días al iniciar

def limpiar_pantalla():
    os.system("cls" if os.name == "nt" else "clear")

def mostrar_tarea(t: Tarea):
    dias = t.dias_restantes()
    estado = "✅" if t.completada else "❌"
    vencimiento = f"{dias}d" if isinstance(dias, int) else "?"
    print(f"[{t.id}] {estado} {t.titulo} | {t.materia} | {t.fecha_limite} ({vencimiento}) | {t.prioridad}")
    if t.descripcion:
        print(f"    → {t.descripcion}")

def listar_tareas(tareas, filtro=None):
    filtradas = tareas
    if filtro == "activas":
        filtradas = [t for t in tareas if not t.completada]
    elif filtro == "completadas":
        filtradas = [t for t in tareas if t.completada]
    elif filtro and isinstance(filtro, dict):
        if "materia" in filtro:
            filtradas = [t for t in filtradas if t.materia.lower() == filtro["materia"].lower()]
        if "prioridad" in filtro:
            filtradas = [t for t in filtradas if t.prioridad.lower() == filtro["prioridad"].lower()]
    if not filtradas:
        print("No hay tareas para mostrar.")
        return
    for t in sorted(filtradas, key=lambda x: (x.completada, x.fecha_limite)):
        mostrar_tarea(t)

def crear_tarea(tareas):
    titulo = input("Título: ").strip()
    materia = input("Materia: ").strip()
    while True:
        fecha = input(f"Fecha límite ({DATE_FORMAT}): ").strip()
        try:
            datetime.strptime(fecha, DATE_FORMAT)
            break
        except Exception:
            print("Formato de fecha inválido. Intenta de nuevo.")
    prioridad = input("Prioridad (Alta/Media/Baja): ").strip().capitalize()
    if prioridad not in ("Alta", "Media", "Baja"):
        prioridad = "Media"
    descripcion = input("Descripción (opcional): ").strip()
    tid = siguiente_id(tareas)
    t = Tarea(id=tid, titulo=titulo, materia=materia, fecha_limite=fecha,
              prioridad=prioridad, descripcion=descripcion)
    tareas.append(t)
    guardar_tareas(tareas)
    print("Tarea creada correctamente.")

def editar_tarea(tareas):
    try:
        tid = int(input("ID de la tarea a editar: "))
    except ValueError:
        print("ID inválido.")
        return
    t = next((x for x in tareas if x.id == tid), None)
    if not t:
        print("Tarea no encontrada.")
        return
    print("Dejar vacío para mantener el valor actual.")
    nuevo_titulo = input(f"Título [{t.titulo}]: ").strip()
    if nuevo_titulo:
        t.titulo = nuevo_titulo
    nueva_materia = input(f"Materia [{t.materia}]: ").strip()
    if nueva_materia:
        t.materia = nueva_materia
    nueva_fecha = input(f"Fecha límite [{t.fecha_limite}]: ").strip()
    if nueva_fecha:
        try:
            datetime.strptime(nueva_fecha, DATE_FORMAT)
            t.fecha_limite = nueva_fecha
        except Exception:
            print("Formato de fecha inválido. Se mantiene la anterior.")
    nueva_prio = input(f"Prioridad [{t.prioridad}]: ").strip().capitalize()
    if nueva_prio in ("Alta", "Media", "Baja"):
        t.prioridad = nueva_prio
    nueva_desc = input(f"Descripción [{t.descripcion}]: ").strip()
    if nueva_desc:
        t.descripcion = nueva_desc
    guardar_tareas(tareas)
    print("Tarea actualizada.")

def eliminar_tarea(tareas):
    try:
        tid = int(input("ID de la tarea a eliminar: "))
    except ValueError:
        print("ID inválido.")
        return
    t = next((x for x in tareas if x.id == tid), None)
    if not t:
        print("Tarea no encontrada.")
        return
    confirm = input(f"Confirmar eliminación de '{t.titulo}' (s/n): ").strip().lower()
    if confirm == "s":
        tareas.remove(t)
        guardar_tareas(tareas)
        print("Tarea eliminada.")

def marcar_completada(tareas):
    try:
        tid = int(input("ID de la tarea a marcar como completada: "))
    except ValueError:
        print("ID inválido.")
        return
    t = next((x for x in tareas if x.id == tid), None)
    if not t:
        print("Tarea no encontrada.")
        return
    t.completada = True
    guardar_tareas(tareas)
    print("Tarea marcada como completada.")

def mostrar_recordatorios(tareas, dias=RANGO_RECORDATORIO_DIAS):
    proximas = [t for t in tareas if (not t.completada) and isinstance(t.dias_restantes(), int) and t.dias_restantes() <= dias]
    if proximas:
        print(f"--- Recordatorios: tareas que vencen en los próximos {dias} días ---")
        for t in sorted(proximas, key=lambda x: x.dias_restantes()):
            mostrar_tarea(t)
        print("---------------------------------------------------------------")
    else:
        print(f"No hay tareas que venzan en los próximos {dias} días.")

def menu():
    tareas = cargar_tareas()
    limpiar_pantalla()
    print("=== EstudIA: Gestor de Tareas Académicas (Prototipo) ===")
    mostrar_recordatorios(tareas)
    while True:
        print("\nMenú:")
        print("1) Crear tarea")
        print("2) Listar todas las tareas")
        print("3) Listar tareas activas")
        print("4) Listar tareas completadas")
        print("5) Filtrar por materia")
        print("6) Filtrar por prioridad")
        print("7) Editar tarea")
        print("8) Eliminar tarea")
        print("9) Marcar tarea como completada")
        print("0) Salir")
        opt = input("Selecciona una opción: ").strip()
        if opt == "1":
            crear_tarea(tareas)
        elif opt == "2":
            listar_tareas(tareas)
        elif opt == "3":
            listar_tareas(tareas, filtro="activas")
        elif opt == "4":
            listar_tareas(tareas, filtro="completadas")
        elif opt == "5":
            materia = input("Materia a filtrar: ").strip()
            listar_tareas(tareas, filtro={"materia": materia})
        elif opt == "6":
            prioridad = input("Prioridad a filtrar (Alta/Media/Baja): ").strip().capitalize()
            listar_tareas(tareas, filtro={"prioridad": prioridad})
        elif opt == "7":
            editar_tarea(tareas)
        elif opt == "8":
            eliminar_tarea(tareas)
        elif opt == "9":
            marcar_completada(tareas)
        elif opt == "0":
            print("Saliendo... ¡Éxitos con tus estudios!")
            break
        else:
            print("Opción inválida. Intenta otra vez.")

if __name__ == "__main__":
    menu()
