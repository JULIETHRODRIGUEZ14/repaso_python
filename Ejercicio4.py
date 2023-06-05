personalizada=2950
tarjeta=int(input("ingrese si tu tarjeta sipt 1.personaliza 2.normal \n"))

if tarjeta==1:
    transbordo=int(input("ingrese 1.primer viaje 2.transbordo \n"))
    if transbordo==1:
        recarga=int(input("ingrese la recarga de la tarjeta"))
        if recarga>2950:
            saldo=recarga-personalizada
            print("el saldo de la tarjeta es" ,saldo)
        elif (recarga<2950) and (recarga>0):
            saldo=recarga-personalizada
            print("su saldo debe" ,saldo)
        else:
            print("su saldo es insuficiente")
    elif transbordo==2:
        print("transferencia realizada")
    elif tarjeta==2:
        recarga=int(input("ingrese la recarga de la tarjeta"))
        if recarga>personalizada:
            saldo=recarga-personalizada
            print("el saldo de la tarjeta es" ,saldo)
        else:
            ("su saldo es insufiente")
            
else:
        print("tarjeta invalida")
