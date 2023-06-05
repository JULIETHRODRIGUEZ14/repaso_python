persona = {
  "firstname": "Jennifer Andrea",
  "lastname": "Fajardo Bolívar",
  "age": 35.8,
  "id": 1234567890,
  "state":True
}
persona={}

#Para ver el contenido completo de un diccionario
print(persona)

#Para acceder al value de un key en particular 
print(persona['Nombre'])

#Para acceder al value de un key en particular, se puede usar el método get 
print(persona.get("Nombre"))

#####MODIFICAR ELEMENTOS

#También se pueden modificar los elementos del diccionario a través de su key en este ejemplo cambiaremos el nombre “Jennifer Andrea” por “Tatiana Lizbeth” 
persona['Nombre'] = "Tatiana Lizbeth"

#Si accedemos a un key que no existe este se añadirá automáticamente al diccionario
persona['Title'] = "Ingeniera electrónica"

#También se puede utilizar el método update, que accede al diccionario, y a través del key modifica su valor
i1.update({"Nombre": "Jennifer Andreas"})

####BORRAR ELEMENTOS

#El método pop borra un elemento del diccionario basándose en la key indicada instructor1, permitiéndonos alterar el diccionario.
instructores.pop("instructor1")

#El método popitem borra el último elemento del diccionario, en este caso instructor2. 
instructores.popitem()

#del se utiliza para apuntar al elemento a borrar de un diccionario, mediante su key
del instructores["instructor1"]

####BORRAR ELEMENTOS

#Se pueden borrar un diccionario completo
del instructores

#Se puede vaciar el contenido completo de un diccionario con el método clear()
instructores.clear()

###RECORRER ELEMENTOS

#Muestra los key del diccionario
for x in persona:
    print(x)

#Muestra los value del diccionario
for x in persona:
    print(persona[x])

#Muestra cada par key y value del diccionario
for x, y in persona.items():
    print(x,":", y)

###DICCIONARIOS ANIDADOS

i1 = {
  "Nombre": "Jennifer Andrea",
  "Apellido": "Fajardo Bolívar",
  "Title":"Ingeniera de Sistemas"
}
i2={
  "Nombre": "Tatiana Lizbeth",
  "Apellido": "Cabrera Vargas",
  "Title":"Ingeniera Electrónica"
}
#Diccionario anidado
instructores={
    "instructor1":i1,
    "instructor2":i2
    }
