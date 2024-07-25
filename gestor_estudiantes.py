estudiantes = []


def agregar_estudiante(carnet, nombre, edad, nivel, calificaciones=[]):
    estudiante = {
        "carnet": carnet,
        "nombre": nombre,
        "edad": edad,
        "nivel": nivel,
        "calificaciones": calificaciones
    }
    estudiantes.append(estudiante)


def buscar_estudiante(carnet):
    for estudiante in estudiantes:
        if estudiante['carnet'] == carnet:
            return estudiante
    return None


def modificar_estudiante(carnet, nombre=None, edad=None, nivel=None, calificaciones=None):
    estudiante = buscar_estudiante(carnet)
    if estudiante:
        if nombre:
            estudiante['nombre'] = nombre
        if edad:
            estudiante['edad'] = edad
        if nivel:
            estudiante['nivel'] = nivel
        if calificaciones is not None:
            estudiante['calificaciones'] = calificaciones
        return True
    return False


def eliminar_estudiante(carnet):
    global estudiantes
    estudiantes = [estudiante for estudiante in estudiantes if estudiante['carnet'] != carnet]


def calificar_estudiante(carnet, materia, nota):
    estudiante = buscar_estudiante(carnet)
    if estudiante:
        estudiante['calificaciones'].append((materia, nota))


def calcular_promedio(carnet):
    estudiante = buscar_estudiante(carnet)
    if estudiante and estudiante['calificaciones']:
        notas = [nota for materia, nota in estudiante['calificaciones']]
        return sum(notas) / len(notas)
    return 0.0


def listar_estudiantes_aprobados_y_reprobados():
    aprobados = []
    reprobados = []
    for estudiante in estudiantes:
        promedio = calcular_promedio(estudiante['carnet'])
        if promedio >= 7:
            aprobados.append(estudiante)
        else:
            reprobados.append(estudiante)
    return aprobados, reprobados
