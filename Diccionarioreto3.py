instructores2557861 = {}

def agregar_modificar():
    nombre = input("Ingrese el nombre del instructor: ")
    if nombre in instructores2557861:
        print("Nombre: ", nombre)
        print("Materia: ", instructores2557861[nombre]["materia"])
        print("Teléfono: ", instructores2557861[nombre]["telefono"])
        modificar = input("¿Desea modificar la materia y el teléfono? (s/n): ")
        if modificar.lower() == "s":
            materia = input("Ingrese la nueva materia: ")
            telefono = input("Ingrese el nuevo teléfono: ")
            instructores2557861[nombre]["materia"] = materia
            instructores2557861[nombre]["telefono"] = telefono
            print("Instructor modificado con éxito.")
    else:
        materia = input("Ingrese la materia: ")
        telefono = input("Ingrese el teléfono: ")
        instructores2557861[nombre] = {"materia": materia, "telefono": telefono}
        print("Instructor agregado con éxito.")

def buscar():
    texto_busqueda = input("Ingrese el texto de búsqueda: ")
    resultados = [nombre for nombre in instructores2557861.keys() if nombre.startswith(texto_busqueda)]
    print("Resultados de la búsqueda:")
    for resultado in resultados:
        print("Nombre: ", resultado)
        print("Materia: ", instructores2557861[resultado]["materia"])
        print("Teléfono: ", instructores2557861[resultado]["telefono"])

def borrar():
    nombre = input("Ingrese el nombre del instructor que desea borrar: ")
    if nombre in instructores2557861:
        confirmar = input("¿Está seguro de que desea borrar a este instructor? (s/n): ")
        if confirmar.lower() == "s":
            del instructores2557861[nombre]
            print("Instructor borrado con éxito.")
    else:
        print("El instructor no existe en la agenda.")

def listar():
    print("Lista de instructores:")
    for nombre, datos in instructores2557861.items():
        print("Nombre: ", nombre)
        print("Materia: ", datos["materia"])
        print("Teléfono: ", datos["telefono"])

# Función principal del programa
def main():
    while True:
        print("\n----- Menú -----\n")
        print("1. Agregar/Modificar")
        print("2. Buscar")
        print("3. Borrar")
        print("4. Listar")
        print("5. Salir")
        opcion = input("\nSeleccione una opción: ")

        if opcion == "1":
            agregar_modificar()
        elif opcion == "2":
            buscar()
        elif opcion == "3":
            borrar()
        elif opcion == "4":
            listar()
        elif opcion == "5":
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")

# Ejecutar el programa
main()
