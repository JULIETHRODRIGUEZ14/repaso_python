
baul = []

while True:
    print("*****Menu del baul*****")
    print("1.Agregar un articulo al baul ")
    print("2. Listar articulos del baul de forma ascendente")
    print("3. Borrar el ultimo elemento de la lista")
    print("4. Borrar un articulo del baul")

    opcion=int(input("Ingresa el numero de la opcion que deseas realizar\n"))

    if opcion==1:
        articulo= input("Ingresa el articulo que deseas agregar\n")
        baul.append(articulo)
        print("el articulo '{}' ha sido agregado al baul".format(articulo))
    elif opcion==2:
        if len(baul)==0:
            print("el baul esta vacio\n")
        else:
            print("articulos en el baul\n")
            for index, articulo in enumerate(sorted(baul)):
                print("{}: {}".format(index,articulo))
    elif opcion==3:
        if len (baul)==0:
            print("el  baul esta vacio\n")
        else:
            articulo_eliminado =baul.pop()
            print("el articulo '{}' ha sido eliminado del baul.".format(articulo_eliminado))
    elif opcion==4:
        if len (baul)==0:
            print("el baul esta vacio\n")
        else:
            print("articulos en el baul\n")
            for index, articulo in enumerate(baul):
                print("{}:{}".format(index,articulo))

                index_borrar=int(input("ingrese el indice del articulo que desea borrar\n"))
                if index_borrar <0 or index_borrar >= len(baul):
                    print("indice invalido")
                else:
                    articulo_eliminado =baul.pop(index_borrar)
                    print("el articulo '{}' ha sido eliminado del baul".format(articulo_eliminado))
            else:
                print("opcion invalida")
            continuar =input("¿desea realizar otra operacion? (S/n):\n")
            if continuar.lower() != "s":
                break
