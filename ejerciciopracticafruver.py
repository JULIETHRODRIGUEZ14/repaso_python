fruver = {}

def agregar_modificar():
    nombre = input("Ingrese el nombre de la fruta: ")
    if nombre in fruver:
        print("La fruta ya está registrada. Precio:", fruver[nombre])
    else:
        precio = input("Ingrese el precio de la fruta: ")
        fruver[nombre] = precio
        print("Fruta agregada correctamente.")

def buscar():
    texto_busqueda = input("Ingrese el texto de búsqueda: ")
    frutas_encontradas = [fruta for fruta in fruver.keys() if fruta.startswith(texto_busqueda)]
    if len(frutas_encontradas) > 0:
        print("Frutas encontradas:")
        for fruta in frutas_encontradas:
            print(fruta, "- Precio:", fruver[fruta])
    else:
        print("No se encontraron frutas con ese texto de búsqueda.")

def borrar():
    nombre = input("Ingrese el nombre de la fruta a borrar: ")
    if nombre in fruver:
        confirmacion = input("¿Está seguro de que desea borrar {} del fruver? (s/n) ".format(nombre))
        if confirmacion.lower() == "s":
            del fruver[nombre]
            print("Fruta borrada correctamente.")
        else:
            print("No se ha borrado la fruta.")
    else:
        print("La fruta no existe en el fruver.")

def listar():
    print("Artículos del fruver:")
    if len(fruver) > 0:
        for fruta, precio in fruver.items():
            print(fruta, "- Precio:", precio)
    else:
        print("El fruver está vacío.")

while True:
    print("\nOpciones disponibles:")
    print("1. Agregar/modificar")
    print("2. Buscar")
    print("3. Borrar")
    print("4. Listar")
    print("5. Salir")

    opcion = input("Ingrese el número de la opción deseada: ")

    if opcion == "1":
        agregar_modificar()
    elif opcion == "2":
        buscar()
    elif opcion == "3":
        borrar()
    elif opcion == "4":
        listar()
    elif opcion == "5":
        break
    else:
        print("Opción inválida. Por favor, seleccione una opción válida.")
