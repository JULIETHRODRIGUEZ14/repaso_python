instructores =[]

def agregar_instructor():
    nombre=input("Ingrese el nombre del instructor")
    instructores.append(nombre)
    print("instructor agregado correctamente")

def listar_instructores():  
    print("lista de instructores")
    for instructor in instructores:
        print(instructor)

def modificar_instructor():
    if len (instructores) ==0:
        print("no hay instructores en la lista")
    else:
        listar_instructores()
        indice =int(input("ingrese el indice del instructor a modifica"))
        if indice <= len(instructores):
            nuevo_nombre=input("ingrese el nuevo nombre del instructor")
            instructores[indice]=nuevo_nombre
            print("instructor modificado correctamnete")
        else:
            print("indice no es valido")

def borrar_instructor():
    if len (instructores) == 0:
        print("no hay instructores en la lista")
        return
    listar_instructores()
    indice =int(input("ingrese el indice del instructor a borrar"))
    if indice < 0 or indice >= len(instructores):
        print("indice invalido")
        return
    instructores.pop(indice)
    print("instructor borrado correctamente")

def bucar_instructor():
    if len (instructores)==0:
        print("no hay instructores en la lista")
        return
    nombre_buscar=input("ingrese el nombre del instructor a buscar").lower()
    for instructor in instructores:
        if nombre_buscar.lower() ==instructor.lower():
            print("instructor encontrado")
            return
        print("instructor no encontrado")

def ordenar_instructores():
    instructores.sort()
    print("lista de instructores ordenada correctamente")

while True:
    print("\n***** Menú*****")
    print("1. Agregar instructor")
    print("2. Listar instructores")
    print("3. Modificar instructor")
    print("4. Borrar instructor")
    print("5. Buscar instructor")
    print("6. Ordenar instructores")
    print("7. Salir")

    opcion=input("selecciona una opcion")

    if opcion=="1":
        agregar_instructor()
    elif opcion=="2":
        listar_instructores()
    elif opcion=="3":
        modificar_instructor()
    elif opcion=="4":
        borrar_instructor()
    elif opcion=="5":
        bucar_instructor()
    elif opcion=="6":
        ordenar_instructores()
    elif opcion=="7":
        print("HASTA LUEGO")
        break
    else:
        print("opcion invalida. intente nuevamnete")