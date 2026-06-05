import json
from json import JSONDecodeError
#verificar que el JSON tenga contenido adentro y cargarlo y si no lo tiene crear uno
try:
    with open("tareas.json", "r") as archivo:
        datos_guardados = json.load(archivo)
        tareas = datos_guardados
except FileNotFoundError:
    tareas = []
except JSONDecodeError:
    tareas = []

#Clase que representa una tarea
class Tarea:
    def __init__(self, titulo, descripcion, completo = False):
        self.titulo = titulo
        self.descripcion = descripcion
        self.completo = completo

#funcion para agregar una nueva tarea a tareas
def agregar_tareas():
    print("Creando tarea...")
    titulo = input("Introduce el titulo de la tarea: ")
    descripcion = input("Introduce la descripcion de la tarea: ")

    if not titulo.strip() or not descripcion.strip():
        print("Debes colocar al menos un titulo o descripcion")
        return

    tarea = Tarea(titulo, descripcion)
    diccionario_tarea = {
        "Titulo": tarea.titulo,
        "Descripcion": tarea.descripcion,
        "Completada": tarea.completo
    }

    print("Tarea creada con exito")
    tareas.append(diccionario_tarea)

#funcion para eliminar una tarea del JSON
def eliminar_tarea():
    tarea_eliminar = input("Introduce el nombre de la tarea a eliminar: ")
    for tarea in tareas:
        if tarea["Titulo"] == tarea_eliminar:
            tareas.remove(tarea)
            print("Tarea eliminada correctamente")
            return

    print("Tarea no encontrada")
    return

#funcion para marcar como completado una tarea del JSON
def completar_tarea():
    marcar_tarea = input("Introduce el nombre de la tarea: ")
    encontrada = False
    for tarea in tareas:
        if tarea["Titulo"] == marcar_tarea:
            if tarea["Completada"]:
                print("La tarea ya estaba completa")
                encontrada = True
            else:
                tarea["Completada"] = True
                print(f"La tarea {tarea['Titulo']}, se ah completado")
                encontrada = True

    if not encontrada:
        print("Tarea no encontrada")


#Bucle principal

while True:
    print("Bienvenido a el Gestor de tareas")
    desicion = input("""
    -----MENU-----
    (1)- Agregar tareas
    (2)- Ver tareas
    (3)- Eliminar tareas
    (4)- Guardar todo
    (5)- Completar tarea
    (6)- Salir
    respuesta: """)

    if desicion not in ["1","2","3","4","5","6"]:
        print("Introduce un digito valido")
        continue

    elif desicion == "1":
        agregar_tareas()
        print("Tarea añadida")
        continue

    elif desicion == "2":
        print(json.dumps(tareas, indent=4, ensure_ascii=False))

    elif desicion == "3":
        eliminar_tarea()

    elif desicion == "4":
        with open("tareas.json", "w") as archivo:
            json.dump(tareas, archivo, indent=4, ensure_ascii=False)
            print("Guardado con exito")
    elif desicion == "5":
        completar_tarea()

    elif desicion == "6":
        pregunta = input("Queres guardar cambios?(si/no): ").lower()
        if pregunta not in ["si","no"]:
            print("Solo introduce SI o NO")
        elif pregunta == "si":
            with open("tareas.json", "w") as archivo:
                json.dump(tareas, archivo, indent=4, ensure_ascii=False)
                print("Guardado con exito")
                break
        elif pregunta == "no":
            print("Saliendo sin guardar...")
            break