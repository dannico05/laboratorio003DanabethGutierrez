# principal.py

import gestor_estudiantes as ge


def mostrar_menu():
    print("1. Agregar estudiante")
    print("2. Buscar estudiante")
    print("3. Modificar estudiante")
    print("4. Eliminar estudiante")
    print("5. Calificar estudiante")
    print("6. Calcular promedio")
    print("7. Listar estudiantes aprobados y reprobados")
    print("8. Salir")


def main():
    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción: ")

        if opcion == '1':
            carnet = input("Carnet: ")
            nombre = input("Nombre: ")
            edad = int(input("Edad: "))
            nivel = input("Nivel: ")
            ge.agregar_estudiante(carnet, nombre, edad, nivel)
        elif opcion == '2':
            carnet = input("Carnet del estudiante a buscar: ")
            estudiante = ge.buscar_estudiante(carnet)
            if estudiante:
                print(estudiante)
            else:
                print("Estudiante no encontrado.")
        elif opcion == '3':
            carnet = input("Carnet del estudiante a modificar: ")
            nombre = input("Nuevo nombre (deja en blanco para no cambiar): ")
            edad = input("Nueva edad (deja en blanco para no cambiar): ")
            nivel = input("Nuevo nivel (deja en blanco para no cambiar): ")
            calificaciones = input("Nuevas calificaciones (deja en blanco para no cambiar): ")
            calificaciones = [] if calificaciones == "" else [float(n) for n in calificaciones.split(',')]
            ge.modificar_estudiante(carnet, nombre or None, int(edad) if edad else None, nivel or None, calificaciones or None)
        elif opcion == '4':
            carnet = input("Carnet del estudiante a eliminar: ")
            ge.eliminar_estudiante(carnet)
        elif opcion == '5':
            carnet = input("Carnet del estudiante: ")
            materia = input("Materia: ")
            nota = float(input("Nota: "))
            ge.calificar_estudiante(carnet, materia, nota)
        elif opcion == '6':
            carnet = input("Carnet del estudiante: ")
            promedio = ge.calcular_promedio(carnet)
            print(f"Promedio de calificaciones: {promedio}")
        elif opcion == '7':
            aprobados, reprobados = ge.listar_estudiantes_aprobados_y_reprobados()
            print("Aprobados:")
            for est in aprobados:
                print(est)
            print("Reprobados:")
            for est in reprobados:
                print(est)
        elif opcion == '8':
            break
        else:
            print("Opción no válida. Intente de nuevo.")


if __name__ == "__main__":
    main()
