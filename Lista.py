# definir lista
lista=[1,2,3,4]

#mostrar coontenido de la lista
print(lista)

#acceder a un elemento de la lista
print(lista[0])

#acceder al ultimo elemento
print(lista[-1])

#modificar un elemento de la lista
lista[0]=7
print(lista[0])

#iterar recorrer una lista
for l in lista:
    print(l) 

#si necesitamos un index que acompañe cada dato
for index, l in enumerate(lista):
    print(index,l)

#iterar dos listas al mismo tiempo
lista1=[5,9,10]
lista2=["Jazz", "Rock", "Djent"]
for l1, l2 in zip(lista1,lista2):
    print(l1,l2)

#longitud de la lista
print(len(lista))