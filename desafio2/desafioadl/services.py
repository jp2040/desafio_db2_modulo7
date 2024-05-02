from .models import Tarea, SubTarea

def recupera_tareas_y_sub_tareas():
    tareas = Tarea.objects.all()
    subtareas = SubTarea.objects.all()
    return tareas, subtareas

def crear_nueva_tarea(descripcion):
    tarea = Tarea.objects.create(descripcion=descripcion)
    return recupera_tareas_y_sub_tareas()

def crear_sub_tarea(descripcion, tarea_id):
    tarea = Tarea.objects.get(pk=tarea_id)
    subtarea = SubTarea.objects.create(descripcion=descripcion, tarea=tarea)
    return recupera_tareas_y_sub_tareas()

def elimina_tarea(tarea_id):
    Tarea.objects.filter(pk=tarea_id).delete()
    return recupera_tareas_y_sub_tareas()

def elimina_sub_tarea(subtarea_id):
    SubTarea.objects.filter(pk=subtarea_id).delete()
    return recupera_tareas_y_sub_tareas()

def imprimir_en_pantalla(tareas, subtareas):
    for tarea in tareas:
        print(f"[{tarea.id}] {tarea.descripcion}")
        for subtarea in tarea.subtareas.all():
            print(f".... [{subtarea.id}] {subtarea.descripcion}")
