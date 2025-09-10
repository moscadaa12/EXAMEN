"""
Archivo de ejemplo para crear datos de prueba en EstudIA
Este archivo puede ejecutarse para poblar la aplicación con tareas de ejemplo
"""

from datetime import datetime, timedelta
from gestor_tareas import GestorTareas


def crear_datos_ejemplo():
    """
    Crea datos de ejemplo para demostrar la funcionalidad de EstudIA.
    """
    print("🎓 Creando datos de ejemplo para EstudIA...")
    
    # Crear gestor con archivo de ejemplo
    gestor = GestorTareas("tareas_ejemplo.json")
    
    # Limpiar datos existentes
    gestor.tareas.clear()
    
    # Fechas de ejemplo
    hoy = datetime.now()
    mañana = hoy + timedelta(days=1)
    en_3_dias = hoy + timedelta(days=3)
    en_1_semana = hoy + timedelta(days=7)
    en_2_semanas = hoy + timedelta(days=14)
    ayer = hoy - timedelta(days=1)
    
    # Tareas de ejemplo
    tareas_ejemplo = [
        {
            "titulo": "Ensayo sobre Inteligencia Artificial",
            "materia": "Inteligencia Artificial",
            "fecha_limite": mañana,
            "prioridad": "Alta",
            "descripcion": "Ensayo de 5 páginas sobre el impacto de la IA en la sociedad moderna"
        },
        {
            "titulo": "Proyecto de Base de Datos",
            "materia": "Base de Datos",
            "fecha_limite": en_3_dias,
            "prioridad": "Alta",
            "descripcion": "Diseñar e implementar una base de datos para un sistema de biblioteca"
        },
        {
            "titulo": "Examen de Cálculo Diferencial",
            "materia": "Cálculo Diferencial",
            "fecha_limite": en_1_semana,
            "prioridad": "Media",
            "descripcion": "Examen parcial sobre derivadas y aplicaciones"
        },
        {
            "titulo": "Presentación de Historia del Arte",
            "materia": "Historia del Arte",
            "fecha_limite": en_2_semanas,
            "prioridad": "Baja",
            "descripcion": "Presentación sobre el Renacimiento italiano"
        },
        {
            "titulo": "Laboratorio de Química Orgánica",
            "materia": "Química Orgánica",
            "fecha_limite": ayer,
            "prioridad": "Alta",
            "descripcion": "Reporte de laboratorio sobre síntesis de compuestos orgánicos"
        },
        {
            "titulo": "Tarea de Programación Web",
            "materia": "Programación Web",
            "fecha_limite": en_3_dias,
            "prioridad": "Media",
            "descripcion": "Crear una página web responsiva usando HTML, CSS y JavaScript"
        },
        {
            "titulo": "Lectura de Filosofía",
            "materia": "Filosofía",
            "fecha_limite": en_1_semana,
            "prioridad": "Baja",
            "descripcion": "Leer y resumir 'El mundo de Sofía' - Capítulos 1-5"
        },
        {
            "titulo": "Proyecto de Investigación",
            "materia": "Metodología de la Investigación",
            "fecha_limite": en_2_semanas,
            "prioridad": "Alta",
            "descripcion": "Proyecto final: Investigación sobre el impacto de las redes sociales en estudiantes universitarios"
        }
    ]
    
    # Agregar tareas al gestor
    for tarea_data in tareas_ejemplo:
        gestor.agregar_tarea(
            tarea_data["titulo"],
            tarea_data["materia"],
            tarea_data["fecha_limite"],
            tarea_data["prioridad"],
            tarea_data["descripcion"]
        )
    
    # Marcar algunas tareas como completadas
    gestor.marcar_completada("Lectura de Filosofía")
    gestor.marcar_completada("Tarea de Programación Web")
    
    print(f"✅ Se crearon {len(tareas_ejemplo)} tareas de ejemplo")
    print("📁 Datos guardados en 'tareas_ejemplo.json'")
    
    # Mostrar estadísticas
    stats = gestor.obtener_estadisticas()
    print(f"\n📊 Estadísticas de las tareas de ejemplo:")
    print(f"   Total: {stats['total']}")
    print(f"   Completadas: {stats['completadas']}")
    print(f"   Pendientes: {stats['pendientes']}")
    print(f"   Vencidas: {stats['vencidas']}")
    print(f"   Urgentes: {stats['urgentes']}")
    
    # Mostrar recordatorios
    recordatorios = gestor.obtener_recordatorios(3)
    if recordatorios:
        print(f"\n🚨 Recordatorios ({len(recordatorios)} tareas próximas a vencer):")
        for tarea in recordatorios:
            dias = tarea.dias_restantes()
            if dias == 0:
                print(f"   ⚠️  HOY: {tarea.titulo}")
            elif dias == 1:
                print(f"   ⚠️  MAÑANA: {tarea.titulo}")
            else:
                print(f"   ⚠️  EN {dias} DÍAS: {tarea.titulo}")
    
    print("\n🎯 Para usar estos datos de ejemplo:")
    print("   1. Ejecuta: python main.py")
    print("   2. La aplicación cargará automáticamente 'tareas_ejemplo.json'")
    print("   3. Explora las diferentes funcionalidades con datos realistas")


if __name__ == "__main__":
    crear_datos_ejemplo()
