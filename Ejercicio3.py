corriente=10800
diesel=9800
total=10800*9800

tipogasolina=input("vas a tanquear corriente o diesel \n")
valor=int(input("ingresa el valor a tanquear \n"))

if tipogasolina==corriente:
    total=tipogasolina/corriente
    print("los galones tanqueados son" ,total)
elif tipogasolina==diesel:
    total=tipogasolina/diesel
    print("los galones tanqueados son" ,total)
else:
    print("los galones tanqueados por gasolina es " ,total)
    


