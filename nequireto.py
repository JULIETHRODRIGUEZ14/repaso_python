import random

continua=1
print("Estas ingresando a la plataforma nequi colombia")
print("No dudamos que seas tu...Pero es mejor confirmar ;)")

celular=input("Ingresa tu numero celular \n")
password=input("Escribe tu clave \n")
if(len(celular)==10 and len(password)==4):

    print("Usted ha ingresado correctamente")
    valor=4500
    while continua==1:
        opcion=int(input("Ingresa la funcionalidad que deseas realizar \n 1.Saca \n 2.Envia \n 3.Recarga \n 4.Salir \n"))
        if opcion==1:
            puntos=int(input("Opciones para sacar\n 1.Punto fisico \n 2.Cajero \n"))

            if puntos==1 and valor>2000:
                codigo=random.randint(000000,999999)
                valorR=int(input("Ingresa cuanto deseas retirar \n"))
                valor=valor-valorR
                
                print("Para sacar,confirmale este codigo a la persona encargada del punto fisico" ,codigo)
                print("Usted acaba de retirar" ,valorR, "el saldo de la cuenta es" ,valor)
            elif puntos==2 and valor>2000:
                codigo=random.randint(000000,999999)
                valorR=int(input("Ingresa cuanto deseas retirar \n"))
                valor=valor-valorR
                print("Para sacar, confirma el codigo en el cajero" ,codigo)
                
                print("RETIRO EXITOSO")
                print("El retiro es de" ,valorR, " el saldo de la cuenta es" ,valor)

            elif(puntos==1 or puntos==2) and valor<2000:
                print("No te alcanza")
            else:
                print("Transaccion invalida")

        elif opcion==2:
            envio=int(input("Ingresa el numero al que deseas enviar el dinero \n"))
            valorE=int(input("Ingresa el valor que deseas enviar \n"))
            if valorE<valor:
                valor=valor-valorE
                print("Usted acaba de enviar" ,valorE, "el saldo en su cuenta es",valor)
            elif valorE>valor:
                print("Proceso invalido, saldo insuficiente \n")

            elif opcion==3:
                recarga=int(input("Ingrese el valor que va a recargar en su cuenta \n"))
                print("Usted va a recargar" ,recarga)
                seguro=int(input("Estas seguro? Ingresa el numero correspondiente \n 1.SI \n 2.NO \n"))
                if seguro==1:
                    valor=valor+recarga
                    print("RECARGA EXITOSA \n")
                    print("Usted recargo" ,recarga, "el valor disponible en la cuenta es de" ,valor)
                elif opcion==2:
                    print("transaccion cancelada")
                else:
                    print("transaccion invalida")
            elif opcion==4:
                print("Vas a salir de nequi")

                avanza=int(input("Ingresa \n 1.para seguir en nequi \n 2. para salir \n"))
            elif (len(celular)!=10 and len(password)!=4):
                print("UPPS, Tus datos son incorrectos, tienes 3 intentos mas \n")
                contadorintentos=1
                while contadorintentos<3:
                    contadorintentos=contadorintentos+1
                    celular=input("Ingrese su numero celular \n")
                    password=input("Ingrese su password \n")
                    if len(celular)==10 and len(password)==4:
                        print("Usted ha ingresado exitosamente")
                    elif len(celular)==10 and len(password)==4:
                        print("UPPS, Tus datos son incorrectos, intenta nuevamente")






