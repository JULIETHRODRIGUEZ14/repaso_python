onces=["combo","sadwich","pizza"]

#agregar un elemento al final de la lista
onces.append("gaseosa");

#agregar varios elementos al final de la lista
onces.extend (["malteada","perro caliente"])

#insertar agregar elementos a la lista
onces.insert(2,"empanada")

#borrar un elemento de la lista
onces.remove("malteada")

#borrar un elemento de una posicion especifica de la lista
del onces[0]

#borrar el ultimo elemento de la lista
onces.pop()

#limpiar la lista
onces.clear()

#ordenar ascendentemente una lista
onces.sort();

#ordenar descendentemente una lista
onces.reverse();
onces.sort(reverse=True);

#devolver en que posicion esta un elemento de la lista
print(onces.index(4))