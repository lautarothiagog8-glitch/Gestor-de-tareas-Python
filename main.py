import json
with open("tareas.json", "r") as archivo:
    datos_guardados = json.load(archivo)

tareas = datos_guardados


class Tarea:
    def __init__(self, titulo, descripcion, completo = False):
        self.titulo = titulo
        self.descripcion = descripcion
        self.completo = completo
    def mostrar_info(self):
        return f"""
        -------TAREA-------
            {self.titulo}
            
        *{self.descripcion}
        
        |--{self.completo}--|
        """


def agregar_tareas():
    print("Creando tarea...")
    titulo = input("Introduce el titulo de la tarea: ")
    descripcion = input("Introduce la descripcion de la tarea: ")
    tarea = Tarea(titulo, descripcion)
    diccionario_tarea = {
        "Titulo": tarea.titulo,
        "Descripcion": tarea.descripcion,
        "Completada": tarea.completo
    }
    print("Tarea creada con exito")
    tareas.append(diccionario_tarea)

def mostrar_tarea():
    print("Cargando datos....")
    with open(r"C:\Users\lauta\OneDrive\Escritorio\Gestor de Tareas-PYTHON.json", "r") as archivoss:
        datos_cargados = json.load(archivoss)
    print("Datos cargados")
    print(datos_cargados)


#Bucle principal
while True:
    print("Bienvenido a el Gestor de tareas")
    desicion = input("""
    -----MENU-----
    (1)- Agregar tareas
    (2)- Ver tareas
    (3)- Eliminar tareas
    (4)- Guardar todo
    (5)- Salir
    respuesta: """)
    if desicion == "1":
        agregar_tareas()
        print("Tarea añadida")
        continue
    elif desicion == "2":
        with open("tareas.json", "r") as archivo:
            archivo_cargado = json.load(archivo)
            print(archivo_cargado)
    elif desicion == "3":
        pass
    elif desicion == "4":
        with open("tareas.json","w") as archivo:
            json.dump(tareas,archivo)
            print("Guardado con exito")
    elif desicion == "5":
        break
