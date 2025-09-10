# 🎓 Gestor de Tareas Académicas "EstudIA"

## 📋 Descripción

**EstudIA** es una aplicación desarrollada en Python para ayudar a estudiantes universitarios a organizar y gestionar sus tareas académicas de manera eficiente. La aplicación está diseñada específicamente para resolver el problema común de olvido de fechas de entrega y eventos importantes en la vida académica.

## 🎯 Problema que Resuelve

- **Olvido de fechas de entrega** de tareas y exámenes
- **Falta de organización** en actividades académicas
- **Estrés y ansiedad** por tareas acumuladas
- **Pérdida de puntos** en evaluaciones por entregas tardías
- **Falta de hábitos** de gestión del tiempo académico

## 👥 Usuario Objetivo

- **Edad**: 18 a 30 años
- **Ocupación**: Estudiantes universitarios de pregrado
- **Necesidades**: Recordar entregas y organizar actividades de manera simple
- **Comportamiento**: Usuarios de computadora y celular que necesitan una herramienta confiable

## ✨ Características Principales

### 📝 Gestión de Tareas
- **Registro completo**: Título, materia, fecha límite, prioridad y descripción
- **Sistema de prioridades**: Alta, Media y Baja con indicadores visuales
- **Estados de tarea**: Pendiente y Completada
- **Edición y eliminación** de tareas existentes

### 🔍 Filtros y Búsquedas
- **Listar todas las tareas** o filtradas por:
  - Materia específica
  - Prioridad (Alta/Media/Baja)
  - Estado (Pendientes/Completadas/Vencidas)
  - Tareas próximas a vencer (configurable por días)

### 🚨 Sistema de Recordatorios
- **Recordatorios automáticos** al iniciar la aplicación
- **Alertas visuales** para tareas que vencen hoy, mañana o en los próximos días
- **Identificación de tareas vencidas**

### 📊 Estadísticas y Reportes
- **Dashboard con estadísticas** completas
- **Contadores por prioridad** y estado
- **Exportación de reportes** a archivos de texto
- **Seguimiento del progreso** académico

### 💾 Persistencia de Datos
- **Almacenamiento local** en archivos JSON
- **Carga automática** de datos al iniciar
- **Guardado automático** de cambios
- **Sin dependencias** de bases de datos externas

## 🏗️ Arquitectura del Sistema

### 📁 Estructura de Archivos
```
EstudIA/
├── main.py              # Punto de entrada principal
├── tarea.py             # Clase Tarea (modelo de datos)
├── gestor_tareas.py     # Clase GestorTareas (lógica de negocio)
├── interfaz_usuario.py  # Clase InterfazUsuario (presentación)
├── tareas_estudia.json  # Archivo de datos (generado automáticamente)
└── README.md           # Este archivo
```

### 🎨 Conceptos de Programación Implementados

#### ✅ Estructuras Secuenciales
- Flujo lineal de ejecución en la interfaz de usuario
- Secuencia de operaciones en el menú principal

#### ✅ Estructuras Repetitivas
- Bucles `for` para iterar sobre listas de tareas
- Bucles `while` para menús interactivos
- Comprensiones de listas para filtros

#### ✅ Modularidad
- **Separación de responsabilidades** en módulos independientes
- **Clases especializadas** para diferentes aspectos del sistema
- **Funciones reutilizables** y bien definidas

#### ✅ Programación Orientada a Objetos (POO)
- **Clase Tarea**: Modelo de datos con encapsulación
- **Clase GestorTareas**: Lógica de negocio y persistencia
- **Clase InterfazUsuario**: Presentación y control de flujo
- **Herencia implícita** de object
- **Polimorfismo** en métodos como `__str__` y `__repr__`

## 🚀 Instalación y Uso

### 📋 Requisitos del Sistema
- **Python 3.6 o superior**
- **Módulos estándar**: json, datetime, os, sys, typing
- **Sistema operativo**: Windows, macOS o Linux

### 🔧 Instalación
1. **Descargar** todos los archivos del proyecto
2. **Verificar** que Python esté instalado en el sistema
3. **Ubicar** todos los archivos en la misma carpeta

### ▶️ Ejecución
```bash
python main.py
```

### 📱 Uso de la Aplicación

#### 🎬 Primera Ejecución
1. La aplicación verificará los requisitos del sistema
2. Mostrará información sobre EstudIA
3. Cargará datos existentes o creará un archivo nuevo
4. Presentará recordatorios y estadísticas

#### 📋 Menú Principal
```
1. 📝 Agregar nueva tarea
2. 📋 Listar tareas
3. ✏️  Editar tarea
4. ✅ Marcar como completada
5. ⏰ Marcar como pendiente
6. 🗑️  Eliminar tarea
7. 🔍 Buscar tarea
8. 📊 Ver estadísticas
9. 📤 Exportar tareas
10. 🚨 Ver recordatorios
0. 🚪 Salir
```

#### 📝 Agregar Tarea
- **Título**: Nombre descriptivo de la tarea
- **Materia**: Curso o asignatura
- **Fecha límite**: Formato DD/MM/YYYY
- **Prioridad**: Alta (🔴), Media (🟡), Baja (🟢)
- **Descripción**: Detalles adicionales (opcional)

#### 🔍 Filtros Disponibles
- **Todas las tareas**: Lista completa
- **Pendientes**: Tareas no completadas
- **Completadas**: Tareas finalizadas
- **Vencidas**: Tareas con fecha límite pasada
- **Por materia**: Filtrar por curso específico
- **Por prioridad**: Filtrar por nivel de importancia
- **Próximas a vencer**: Tareas urgentes (configurable)

## 📊 Ejemplo de Uso

### 🎯 Escenario Típico
1. **Estudiante inicia** la aplicación
2. **Ve recordatorios** de tareas próximas a vencer
3. **Agrega nueva tarea**: "Ensayo de Literatura" para mañana
4. **Marca como Alta prioridad** por la urgencia
5. **Lista tareas pendientes** para ver el panorama general
6. **Completa tarea** cuando la termina
7. **Exporta reporte** para compartir con tutor

### 📈 Beneficios Obtenidos
- ✅ **Organización mejorada** de actividades académicas
- ✅ **Reducción del estrés** por olvidos
- ✅ **Mejor gestión del tiempo** académico
- ✅ **Aumento del rendimiento** en evaluaciones
- ✅ **Hábitos positivos** de planificación

## 🔧 Personalización

### ⚙️ Configuraciones Disponibles
- **Días de recordatorio**: Cambiar en `obtener_recordatorios(dias)`
- **Archivo de datos**: Modificar en `GestorTareas(archivo_datos)`
- **Formatos de fecha**: Agregar en `obtener_fecha()`
- **Prioridades**: Extender en `obtener_prioridad_numerica()`

## 🐛 Solución de Problemas

### ❌ Errores Comunes
1. **"Módulo no encontrado"**: Verificar que todos los archivos estén en la misma carpeta
2. **"Error de fecha"**: Usar formato DD/MM/YYYY (ej: 25/12/2024)
3. **"Archivo no se guarda"**: Verificar permisos de escritura en la carpeta
4. **"Tarea no encontrada"**: Verificar que el título coincida exactamente

### 🔍 Debugging
- Los errores se muestran con emojis descriptivos
- Mensajes de error incluyen sugerencias de solución
- Logs de operaciones en la consola

## 📈 Mejoras Futuras

### 🚀 Funcionalidades Potenciales
- **Notificaciones del sistema** (Windows/macOS/Linux)
- **Sincronización en la nube** (Google Drive, Dropbox)
- **Aplicación móvil** complementaria
- **Integración con calendarios** (Google Calendar, Outlook)
- **Análisis de patrones** de productividad
- **Recordatorios por email** o SMS
- **Colaboración en grupo** para proyectos

### 🎨 Mejoras de Interfaz
- **Interfaz gráfica** con tkinter o PyQt
- **Temas personalizables** (claro/oscuro)
- **Atajos de teclado** para usuarios avanzados
- **Búsqueda avanzada** con múltiples criterios

## 👥 Contribuciones

### 🤝 Cómo Contribuir
1. **Reportar bugs** con descripción detallada
2. **Sugerir mejoras** con casos de uso
3. **Proponer nuevas funcionalidades**
4. **Compartir experiencias** de uso

### 📝 Código de Conducta
- **Respeto** hacia todos los usuarios
- **Colaboración** constructiva
- **Enfoque** en mejorar la experiencia estudiantil

## 📄 Licencia

Este proyecto está desarrollado con fines educativos para estudiantes universitarios. El código es de libre uso para propósitos académicos.

## 📞 Contacto

Para reportar problemas, sugerir mejoras o compartir experiencias de uso, puedes contactar al equipo de desarrollo de EstudIA.

---

**🎓 ¡EstudIA - Tu compañero para el éxito académico! 🎓**

*Desarrollado con ❤️ para estudiantes universitarios*
